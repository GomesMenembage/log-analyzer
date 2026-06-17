import re

ACCESS_PATTERN = re.compile(
    r'^(\S+) .+ \[([^\]]+)\] "(\S+) (\S+) [^"]+" (\d{3}) .+'
)

APACHE_ERROR_PATTERN = re.compile(
    r'^\[([^\]]+)\] \[(\w+):(\w+)\] .+'
)

NGINX_ERROR_PATTERN = re.compile(
    r'^(\d{4}/\d{2}/\d{2} \d{2}:\d{2}:\d{2}) \[(\w+)\] .+'
)

IP_IN_MESSAGE = re.compile(r'client:? (\d+\.\d+\.\d+\.\d+)')


def parse_line(line, log_format):
    if "access" in log_format:
        m = ACCESS_PATTERN.match(line)
        if not m:
            return None
        ip, timestamp, method, path, status = m.group(1), m.group(2), m.group(3), m.group(4), m.group(5)
        if status.startswith("5"):
            level = "ERROR"
        elif status.startswith("4"):
            level = "WARN"
        else:
            level = "INFO"
        return {
            "ip": ip,
            "timestamp": timestamp,
            "level": level,
            "status": int(status),
            "method": method,
            "path": path,
        }

    if log_format == "apache_error":
        m = APACHE_ERROR_PATTERN.match(line)
        if not m:
            return None
        timestamp, level, module = m.group(1), m.group(2), m.group(3)
        ip_m = IP_IN_MESSAGE.search(line)
        ip = ip_m.group(1) if ip_m else None
        return {
            "ip": ip,
            "timestamp": timestamp,
            "level": level.upper(),
        }

    if log_format == "nginx_error":
        m = NGINX_ERROR_PATTERN.match(line)
        if not m:
            return None
        timestamp, level = m.group(1), m.group(2)
        ip_m = IP_IN_MESSAGE.search(line)
        ip = ip_m.group(1) if ip_m else None
        return {
            "ip": ip,
            "timestamp": timestamp,
            "level": level.upper(),
        }

    return None

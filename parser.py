import re

ACCESS_PATTERN = re.compile(
    r'^(\S+) .+ \[([^\]]+)\] "(\S+) (\S+) [^"]+" (\d{3}) .+'
)

ERROR_PATTERN = re.compile(
    r'^\[([^\]]+)\] \[(\w+):(\w+)\] .+'
)

NGINX_ERROR_PATTERN = re.compile(
    r'^(\d{4}/\d{2}/\d{2} \d{2}:\d{2}:\d{2}) \[(\w+)\] .+'
)


def extract_timestamp(line, log_format):
    if "access" in log_format:
        m = ACCESS_PATTERN.match(line)
        if m:
            return m.group(2)
    elif log_format == "apache_error":
        m = ERROR_PATTERN.match(line)
        if m:
            return m.group(1)
    elif log_format == "nginx_error":
        m = NGINX_ERROR_PATTERN.match(line)
        if m:
            return m.group(1)
    return None

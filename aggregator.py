from collections import defaultdict
import re

ACCESS_TS = re.compile(r"\d{2}/\w+/\d{4}:(\d{2}):\d{2}:\d{2}")
APACHE_ERROR_TS = re.compile(r"\w+ \w+ \d{2} (\d{2}):\d{2}:\d{2} \d{4}")
NGINX_ERROR_TS = re.compile(r"\d{4}/\d{2}/\d{2} (\d{2}):\d{2}:\d{2}")


def extract_hour(timestamp):
    for pattern in (ACCESS_TS, APACHE_ERROR_TS, NGINX_ERROR_TS):
        m = pattern.search(timestamp)
        if m:
            return f"{m.group(1)}:00"
    return None


def aggregate(entries):
    counts = defaultdict(lambda: defaultdict(int))
    for entry in entries:
        hour = extract_hour(entry["timestamp"])
        if hour:
            counts[hour][entry["level"]] += 1
    return counts


def generate_summary(counts):
    total = sum(sum(v.values()) for v in counts.values())
    errors = sum(v.get("ERROR", 0) for v in counts.values())
    warnings = sum(v.get("WARN", 0) for v in counts.values())

    return {
        "total": total,
        "errors": errors,
        "warnings": warnings,
        "hours": {
            hour: dict(levels) for hour, levels in sorted(counts.items())
        },
    }

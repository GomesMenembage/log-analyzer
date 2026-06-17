import re

PATTERNS = {
    "apache_access": re.compile(
        r'^(\S+) (\S+) (\S+) \[([^\]]+)\] "(\S+) (\S+) [^"]+" (\d{3}) (\S+)'
    ),
    "nginx_access": re.compile(
        r'^(\S+) - - \[([^\]]+)\] "(\S+) (\S+) [^"]+" (\d{3}) (\d+|-) "[^"]*" "[^"]*"'
    ),
    "apache_error": re.compile(
        r'^\[([^\]]+)\] \[(\w+):(\w+)\] \[pid \d+\] (.+)'
    ),
    "nginx_error": re.compile(
        r'^(\d{4}/\d{2}/\d{2} \d{2}:\d{2}:\d{2}) \[(\w+)\] (\d+#\d+): (.+)'
    ),
}

def detect_log_format(file_path, sample_size=5):
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            samples = [f.readline() for _ in range(sample_size)]
    except FileNotFoundError:
        return "file_not_found"

    samples = [s.strip() for s in samples if s.strip()]
    if not samples:
        return "empty_file"

    scores = {name: 0 for name in PATTERNS}
    for line in samples:
        for name, pattern in PATTERNS.items():
            if pattern.match(line):
                scores[name] += 1

    best_option = max(scores, key=scores.get)
    if scores[best_option] == 0:
        return "unknown_format"

    return best_option

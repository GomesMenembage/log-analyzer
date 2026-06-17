import argparse
from detector import detect_log_format
from parser import parse_line
from aggregator import aggregate

def read_log_file(path):

    if path.endswith("/"):
        print("Path is a folder, try with a file")
        return

    log_format = detect_log_format(path)
    if log_format == "file_not_found":
        print("File was not found")
        return
    if log_format == "empty_file":
        print("File is empty")
        return
    if log_format == "unknown_format":
        print("Unrecognized log format (expected Apache or Nginx)")
        return

    try:
        with open (path,"r", encoding="utf-8") as log_file:
            for line in log_file:
                valid_line = line.strip()
                if valid_line:
                    yield valid_line, log_format

    except FileNotFoundError:
        print("File was not found")

def main():
    parser = argparse.ArgumentParser(description="CLI de Análise de Logs")
    parser.add_argument("--file", required=True, help="Caminho do ficheiro de log")
    parser.add_argument("--level", choices=["ERROR", "WARN", "INFO", "DEBUG"],help="Filtrar por nivel de severidade")
    args = parser.parse_args()

    entries = []
    for line,log_format in read_log_file(args.file):
        entry = parse_line(line, log_format)
        if entry is None:
            continue
        if args.level and entry["level"]!= args.level:
            continue
        entries.append(entry)
        print(entry)

    counts = aggregate(entries)
    print("\n--- Agregação por hora ---")
    for hour in sorted(counts):
        print(f"{hour} -> {dict(counts[hour])}")

if __name__ == "__main__":
    main()

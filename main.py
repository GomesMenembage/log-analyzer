import argparse
from detector import detect_log_format
from parser import parse_line
from aggregator import aggregate, generate_summary
from exporter import export_csv
from geo_enricher import enrich_entries

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
    parser.add_argument("--output", required=True, metavar="FICHEIRO", help="Caminho do ficheiro CSV de saida")
    args = parser.parse_args()

    entries = []
    for line,log_format in read_log_file(args.file):
        entry = parse_line(line, log_format)
        if entry is None:
            continue
        if args.level and entry["level"]!= args.level:
            continue
        entries.append(entry)

    entries = enrich_entries(entries)
    for entry in entries:
        print(entry)

    counts = aggregate(entries)
    summary = generate_summary(counts)

    print("\n=== RESUMO DA ANALISE ===")
    print(f"Total de logs processados: {summary['total']}")
    print(f"Total de ERROR: {summary['errors']}")
    print(f"Total de WARN: {summary['warnings']}")
    print("Frequencia por hora:")
    for hour, levels in summary["hours"].items():
        parts = ", ".join(f"{k}: {v}" for k, v in levels.items())
        print(f"  {hour} - {parts}")

    export_csv(entries, args.output)
    print(f"\nRelatorio exportado para: {args.output}")

if __name__ == "__main__":
    main()

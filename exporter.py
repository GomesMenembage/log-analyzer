import csv


def export_csv(entries, filepath):
    with open(filepath, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["hora", "tipo", "ip", "pais", "cidade"])
        for entry in entries:
            writer.writerow([
                entry.get("timestamp", ""),
                entry.get("level", ""),
                entry.get("ip", ""),
                entry.get("pais", ""),
                entry.get("cidade", ""),
            ])

import csv


def export_csv(rows, filepath):
    with open(filepath, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["hora", "tipo", "total", "pais", "cidade"])
        for (hour, level, pais, cidade), data in sorted(rows.items()):
            writer.writerow([hour, level, data["total"], data["pais"], data["cidade"]])

import csv


def export_csv(summary, filepath):
    with open(filepath, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["hora", "tipo", "total"])
        for hour, levels in summary["hours"].items():
            for level, total in levels.items():
                writer.writerow([hour, level, total])

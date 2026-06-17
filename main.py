from detector import detect_log_format

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
                    yield line

    except FileNotFoundError:
        print("File was not found")

for line in read_log_file("/home/dm/log-analyzer/main.py"):
     print(line)

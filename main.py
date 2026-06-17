def read_log_file(path):

    if path.endswith("/"):
        print("Path is a folder, try with a file")
    try:
        with open (path,"r", encoding="utf-8") as log_file:
            for line in log_file:
                valid_line = line.strip()
                if valid_line:
                    yield line


    except FileNotFoundError:
        print("File was not founded")

for line in read_log_file("/home/dm/log-analyzer/README.md"):
     print(line)

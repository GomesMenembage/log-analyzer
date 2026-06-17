def read_log_file(path):
    try:
        with open (path,"r", encoding="utf-8") as log_file:
            for line in log_file:
                print(line)

    except FileNotFoundError:
        print("File was not founded")
from datetime import datetime

class Logger:
    def __init__(self):
        self.logs = []

    def log(self, message):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.logs.append(f"[{timestamp}] {message}")

    def write_to_file(self, path):
        with open(path, 'w') as f:
            f.write("\n".join(self.logs))

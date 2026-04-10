class FileReader:
    def read(self, path):
        with open(path, 'r') as f:
            return [line.strip() for line in f if line.strip()]

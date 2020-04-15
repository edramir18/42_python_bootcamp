class CsvReader:
    def __init__(self, filename, sep=',', header=False, skip_top=0, skip_bottom=0):
        self.separator = sep
        self.has_header = header
        self.skip_top_rows = skip_top
        self.skip_bottom_rows = skip_bottom
        self.filename = filename
        self.file = None

    def __enter__(self):
        try:
            self.file = open(self.filename, 'r')
        except FileNotFoundError:
            return None
        print(self.file)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(exc_type, exc_val, exc_tb)
        if self.file is not None:
            self.file.close()
        return exc_type is None

    def getdata(self):
        pass

    def getheader(self):
        pass

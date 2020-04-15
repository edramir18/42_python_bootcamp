class CsvReader:
    def __init__(self, filename, sep=',', header=False, skip_top=0, skip_bottom=0):
        self.separator = sep
        self.has_header = header
        if self.has_header:
            skip_top += 1
        self.skip_top_rows = skip_top
        self.skip_bottom_rows = skip_bottom
        self.filename = filename
        self.header = None
        self.data = None
        self.file = None

    def __enter__(self):
        try:
            self.file = open(self.filename, 'r')
            lines = self.file.readlines()
            rows = len(lines)
            if rows > 0:
                self.data = []
                row_size = None
                for n, line in enumerate(lines):
                    line = [x.strip() for x in line.split(self.separator)]
                    if n == 0:
                        row_size = len(line)
                        if self.has_header:
                            self.header = line
                            continue
                    if n < self.skip_top_rows:
                        continue
                    if n > rows - self.skip_bottom_rows:
                        break
                    if row_size != len(line):
                        return None
                    self.data.append(line)
        except FileNotFoundError:
            return None
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file is not None:
            self.file.close()
        return exc_type is None

    def getdata(self):
        return self.data

    def getheader(self):
        return self.header

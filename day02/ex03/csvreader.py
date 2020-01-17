
import csv

class CsvReader():
    def __init__(self, filename, sep=',', header=False, skip_top=0, skip_bottom=0):
        self.filename = filename
        self.sep = sep
        self.header = header
        self.skip_top = skip_top
        self.skip_bottom = skip_bottom
        pass

    def __enter__(self):
        self.fd = open(self.filename)
        self.reader = csv.DictReader(self.fd)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.fd.close()
        pass

    def getdata(self):
        els = [row for (row) in self.reader]
        elm = [row for row in els[self.skip_top:len(els) - self.skip_bottom]]
        return elm
    
    def getheader(self):
        if self.header:
            return self.reader.fieldnames
        else:
            return None

if __name__ == "__main__":
    with CsvReader('good.csv', header=True, skip_top=1, skip_bottom=3) as file:
        data = file.getdata()
        header = file.getheader()
        print("Header", header)
        print("Data", data)

    # with CsvReader('bad.csv') as file:
    #     if file == None:
    #         print("File is corrupted")

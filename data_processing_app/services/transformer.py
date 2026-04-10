from datetime import datetime

class Transformer:
    def __init__(self, date_format="%Y-%m-%d"):
        self.date_format = date_format

    def transform(self, records):
        for r in records:
            r.name = r.name.upper()

            if r.date:
                try:
                    d = datetime.strptime(r.date, "%Y-%m-%d")
                    r.date = d.strftime(self.date_format)
                except:
                    pass

        return records

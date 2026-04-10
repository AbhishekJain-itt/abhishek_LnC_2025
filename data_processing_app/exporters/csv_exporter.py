from exporters.base_exporter import BaseExporter

class CsvExporter(BaseExporter):
    def export(self, records, path):
        with open(path, 'w') as f:
            f.write("ID,NAME,VALUE,DATE,DOUBLED_VALUE,SQUARED_VALUE\n")
            for r in records:
                d = r.to_dict()
                f.write(f"{d['id']},{d['name']},{d['value']},{d['date']},{d['doubled_value']},{d['squared_value']}\n")

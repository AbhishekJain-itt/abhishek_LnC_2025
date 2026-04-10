from exporters.base_exporter import BaseExporter

class XmlExporter(BaseExporter):
    def export(self, records, path):
        with open(path, 'w') as f:
            f.write("<records>\n")
            for r in records:
                f.write("  <record>\n")
                for k, v in r.to_dict().items():
                    f.write(f"    <{k}>{v}</{k}>\n")
                f.write("  </record>\n")
            f.write("</records>")

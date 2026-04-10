from models.record import Record

class Parser:
    def parse(self, lines):
        records = []
        for line in lines:
            parts = line.split(',')
            if len(parts) < 3:
                continue

            record = Record(
                id=parts[0],
                name=parts[1],
                value=parts[2],
                date=parts[3] if len(parts) > 3 else None
            )
            records.append(record)

        return records

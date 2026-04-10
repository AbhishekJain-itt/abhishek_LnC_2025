class Validator:
    def validate(self, records):
        valid_records = []

        for r in records:
            if not r.id or not r.name:
                continue
            try:
                float(r.value)
                valid_records.append(r)
            except:
                continue

        return valid_records

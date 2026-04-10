class Record:
    def __init__(self, id, name, value, date=None):
        self.id = id
        self.name = name
        self.value = float(value)
        self.date = date

    @property
    def doubled_value(self):
        return self.value * 2

    @property
    def squared_value(self):
        return self.value ** 2

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "value": self.value,
            "date": self.date,
            "doubled_value": self.doubled_value,
            "squared_value": self.squared_value,
        }

class DataProcessor:
    def __init__(self, reader, parser, validator, transformer, stats, logger):
        self.reader = reader
        self.parser = parser
        self.validator = validator
        self.transformer = transformer
        self.stats = stats
        self.logger = logger

    def process(self, input_path):
        self.logger.log("Starting processing")

        lines = self.reader.read(input_path)
        records = self.parser.parse(lines)
        records = self.validator.validate(records)
        records = self.transformer.transform(records)

        statistics = self.stats.calculate(records)

        self.logger.log(f"Processed {statistics['total_records']} records")

        return records, statistics

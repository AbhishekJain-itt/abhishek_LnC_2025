from services.file_reader import FileReader
from services.parser import Parser
from services.validator import Validator
from services.transformer import Transformer
from services.statistics import StatisticsCalculator

from exporters.json_exporter import JsonExporter
from exporters.xml_exporter import XmlExporter
from exporters.csv_exporter import CsvExporter

from processor.data_processor import DataProcessor
from utils.logger import Logger

import random
from datetime import datetime, timedelta


def generate_sample_data(path, count=50):
    with open(path, 'w') as f:
        for i in range(count):
            date = datetime.now() - timedelta(days=random.randint(0, 365))
            f.write(f"ID{i},Item{i},{random.randint(10,1000)},{date.strftime('%Y-%m-%d')}\n")


def main():
    input_file = "data/input.csv"

    generate_sample_data(input_file)

    reader = FileReader()
    parser = Parser()
    validator = Validator()
    transformer = Transformer("%d-%m-%Y")
    stats = StatisticsCalculator()
    logger = Logger()

    processor = DataProcessor(reader, parser, validator, transformer, stats, logger)

    records, statistics = processor.process(input_file)

    
    CsvExporter().export(records, "data/output.csv")
    JsonExporter().export(records, "data/output.json")
    XmlExporter().export(records, "data/output.xml")

    logger.write_to_file("data/log.txt")

    print("Processing completed!")
    print(statistics)


if __name__ == "__main__":
    main()

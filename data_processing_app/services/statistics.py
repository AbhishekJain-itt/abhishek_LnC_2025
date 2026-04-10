class StatisticsCalculator:
    def calculate(self, records):
        total_value = sum(r.value for r in records)

        return {
            "total_records": len(records),
            "total_value": total_value,
            "average_value": total_value / len(records) if records else 0
        }

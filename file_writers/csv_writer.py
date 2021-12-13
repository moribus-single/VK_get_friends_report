from file_writers.base_writer import BaseWriter
import csv


class CsvWriter(BaseWriter):
    def __init__(self, data: list, output_path: str = ""):
        super().__init__(
            data=data,
            output_path=output_path,
            output_type="csv"
        )

    def write(self, titles: list, keys: list):
        with open(self.output_path, 'w', newline='', encoding="utf-8") as file:
            writer = csv.writer(file, delimiter=',')
            writer.writerow(titles)

            for user in self.data:
                dump_list = self._prepare_list(user, keys)
                writer.writerow(dump_list)

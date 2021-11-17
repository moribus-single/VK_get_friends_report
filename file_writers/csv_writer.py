from os.path import join
import utils
import csv


class CsvWriter(object):
    def __init__(self, data: list, output_path: str = ""):
        self.output_path = output_path
        self.data = data
        self.path = join(self.output_path, "report.csv")

    def write(self, titles: list, keys: list):
        with open(self.path, 'w', newline='', encoding="utf-8") as file:
            writer = csv.writer(file, delimiter=',')
            writer.writerow(titles)

            for user in self.data:
                dump_list = utils.prepare_list(user, keys)
                writer.writerow(dump_list)

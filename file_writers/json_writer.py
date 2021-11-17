from os.path import join
from utils import prepare_date
import json


class JsonWriter(object):
    def __init__(self, data: list, output_path: str = ""):
        self.output_path = output_path
        self.data = data
        self.path = join(self.output_path, "report.json")

    def write(self, keys: list):
        with open(self.path, 'w', encoding="utf-8") as file:
            for d in self.data:
                result = self.__prepare_dict(keys, d)
                json.dump(result, file, indent=4)
                file.write("\n")

    @staticmethod
    def __prepare_dict(keys: list, data: list):
        prep_dict = {}
        tmp = {}

        for i in range(len(data)):
            for k in keys:
                if k in data:
                    if k in ["first_name", "last_name"]:
                        tmp[k] = data[k]

                    elif k in ["country", "city"]:
                        tmp[k] = data[k]["title"]

                    elif k == "sex":
                        value = "Female" if data[k] == 1 else "Male"
                        tmp[k] = value

                    elif k == "bdate":
                        date = prepare_date(data[k])
                        tmp[k] = date
                else:
                    tmp[k] = ""

            prep_dict[i] = tmp

        return prep_dict

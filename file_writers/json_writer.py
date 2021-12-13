from file_writers.base_writer import BaseWriter
import json


class JsonWriter(BaseWriter):
    def __init__(self, data: list, output_path: str = ""):
        super().__init__(
            data=data,
            output_path=output_path,
            output_type="json"
        )

    def write(self, keys: list):
        with open(self.output_path, 'w', newline='', encoding="utf-8") as file:
            for d in self.data:
                result = self._prepare_dict(keys, d)
                json.dump(result, file, indent=4)
                file.write("\n")

from os.path import join
from datetime import date


class BaseWriter(object):
    def __init__(
        self,
        data: list,
        output_path: str = "",
        output_type: str = "csv"
    ):
        file_name = f"report_{date.today()}.{output_type}"

        self.output_path = join(output_path, file_name)
        self.data = data

    def _prepare_date(self, some_date: str):
        """Приведение даты в нормальный вид"""
        date_ = some_date.split('.')
        formatted_date = ""

        for i in range(len(date_)):
            if len(date_[i]) == 1:
                date_[i] = '0' + date_[i]

        if len(date_) == 3:
            formatted_date = '{0}.{1}.{2}'.format(*date_)

        elif len(date_) == 2:
            formatted_date = '{0}.{1}'.format(*date_)

        return formatted_date

    def _prepare_list(self, user: dict, keys: list) -> list:
        """Приведение данных к читабельному виду для записи в файл"""
        output = []

        for k in keys:
            if k in user:
                if k in ["first_name", "last_name"]:
                    output.append(user[k])

                elif k in ["country", "city"]:
                    output.append(user[k]["title"])

                elif k == "sex":
                    val = "Женский" if user[k] == 1 else "Мужской"
                    output.append(val)

                elif k == "bdate":
                    date = self._prepare_date(user[k])
                    output.append(date)
            else:
                output.append("")

        return output

    def _prepare_dict(self, keys: list, data: list):
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
                        date = self._prepare_date(data[k])
                        tmp[k] = date
                else:
                    tmp[k] = ""

            prep_dict[i] = tmp

        return prep_dict

def prepare_date(some_date: str) -> str:
    """Приведение даты в нормальный вид"""
    date = some_date.split('.')
    formatted_date = ""

    for i in range(len(date)):
        if len(date[i]) == 1:
            date[i] = '0' + date[i]

    if len(date) == 3:
        formatted_date = '{0}.{1}.{2}'.format(*date)

    elif len(date) == 2:
        formatted_date = '{0}.{1}'.format(*date)

    return formatted_date


def prepare_list(user: dict, keys: list) -> list:
    """Приведение данных к читабельному виду для записи в файл"""
    output = []

    for k in keys:
        if k in user:
            if k in ["first_name", "last_name"]:
                output.append(user[k].encode("utf-8"))

            elif k in ["country", "city"]:
                output.append(user[k]["title"].encode("utf-8"))

            elif k == "sex":
                val = "Женский" if user[k] == 1 else "Мужской"
                output.append(val.encode("utf-8"))

            elif k == "bdate":
                date = prepare_date(user[k])
                output.append(date.encode("utf-8"))
        else:
            output.append("")

    return output


def print_error(text: str):
    """Для вывода ошибок"""
    print("\033[31m{}".format(text))

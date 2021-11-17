from os.path import exists, join
from friends_getter.friends_getter import FriendsGetter
from data_getter.data_getter import DataGetter
from utils import print_error
import file_writers

# Поддерживаемые типы для отчетов
VALID_OUTPUT_TYPES = ['csv', 'tsv', 'json']

# Ключи для получения данных из ответа на запрос к API VK, должны быть согласованны с заголовками
KEYS = ["first_name", "last_name", "country", "city", "bdate", "sex"]

# Заголовки для отчетных файлов
TITLES = ["Имя", "Фамилия", "Страна", "Город", "Дата", "Пол"]

# Входные данные
TOKEN = ""
USER_ID = ""
OUTPUT_TYPE = "csv"
OUTPUT_PATH = ""


def validation():
    assert isinstance(TOKEN, str) and len(TOKEN) > 0, "Invalid access token"
    assert isinstance(USER_ID, (int, str)), "Invalid user id"

    assert len(KEYS) > 0, "Empty keys list, line 11"
    assert len(TITLES) > 0, "Empty titles list, line 14"
    assert len(VALID_OUTPUT_TYPES) > 0, \
        "Empty list of valid types for reporting on line 8, standart - csv, tsv, json"

    assert exists(OUTPUT_PATH), f"Path '{OUTPUT_PATH}' is not exist"
    assert OUTPUT_TYPE in VALID_OUTPUT_TYPES, \
        f"Type '{OUTPUT_TYPE}' is not supported, try one of this - {VALID_OUTPUT_TYPES}"


def main():
    print("Start getting friends list...")
    friends_getter = FriendsGetter(access_token=TOKEN, user_id=USER_ID)
    friends_list = friends_getter.get_friends_list()  # список id друзей

    if friends_list is not None:
        print("SUCCESS!\n")
        print("Start getting information about friends...")
        data_getter = DataGetter(list_id=friends_list, access_token=TOKEN)
        data_list = data_getter.get_info(KEYS)  # список словарей с необходимыми данными
    else:
        print_error("Error in finding friends id occurred, 36-37 lines")
        return

    print("SUCCESS!\n")
    print("Start making report...")
    match OUTPUT_TYPE.lower():
        case "csv":
            file_writer = file_writers.csv_writer.CsvWriter(output_path=OUTPUT_PATH, data=data_list)
            file_writer.write(titles=TITLES, keys=KEYS)  # запись в файл по указаному пути

        case "tsv":
            file_writer = file_writers.tsv_writer.TsvWriter(output_path=OUTPUT_PATH, data=data_list)
            file_writer.write(titles=TITLES, keys=KEYS)  # запись в файл по указаному пути

        case "json":
            file_writer = file_writers.json_writer.JsonWriter(output_path=OUTPUT_PATH, data=data_list)
            file_writer.write(keys=KEYS)  # запись в файл по указаному пути
    print("SUCCESS!\n")

    final_dir = join(OUTPUT_PATH, "report." + OUTPUT_TYPE.lower())
    print(f"Report was saved in the directory: '{final_dir}'")


if __name__ == "__main__":
    validation()
    main()

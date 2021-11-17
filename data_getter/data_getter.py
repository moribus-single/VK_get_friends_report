import vk_api


class DataGetter:
    def __init__(self, list_id: list, access_token: str):
        self.list_id = list_id
        self.token = access_token

    def get_info(self, keys: list) -> list:
        session = vk_api.VkApi(token=self.token)

        params = {"user_ids": self.__get_ids(), "fields": self.__get_fields(keys)}
        response = session.method("users.get", params)

        return response

    def __get_ids(self):
        return ",".join([str(acc) for acc in self.list_id])  # id пользователей через запятую

    @staticmethod
    def __get_fields(keys: list):
        return ",".join([str(acc) for acc in keys])  # поля для запроса через запятую

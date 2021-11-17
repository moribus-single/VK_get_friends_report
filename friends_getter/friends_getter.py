import vk_api
from utils import print_error


class FriendsGetter:
    """Получение списка с id друзей"""

    def __init__(self, access_token: str, user_id: str | int):
        self.session = vk_api.VkApi(token=access_token)
        self.user_id = str(user_id) if isinstance(user_id, int) else user_id

    def get_friends_list(self) -> list:
        try:
            response = self.session.method("friends.get", {"user_id": self.user_id})
        except vk_api.exceptions.ApiError:
            print_error("ERROR: Invalid authorization token or user id")
            return None
        else:
            return response['items']

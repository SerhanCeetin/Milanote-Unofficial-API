import logging
import requests
from .elements.board import Board
from .exceptions import BoardNotFoundError, NotAuthorizedError, UnknownError

BOARD_BASE_URL = "https://app.milanote.com/api/boards/"
HOME_URL = "https://app.milanote.com/api/users/me"


class MilanoteApi:
    """
    Milanote API
    """
    logger = logging.getLogger()

    def __init__(self, cookies, headers, logging_level: int = logging.WARNING):
        self.cookies = cookies
        self.headers = headers
        self.logger.setLevel(logging_level)
        self.logger.debug("MilanoteApi initialized")

    def get_home_board(self):
        """
        Get the home board of the user.
        Note: Only the top level elements are loaded.
        """

        self.logger.debug("Getting boards from home")
        response = requests.get(HOME_URL, headers=self.headers, cookies=self.cookies)
        if response.status_code == 200:
            return self.get_board_by_id(list(response.json()["elements"].keys())[0])
        else:
            self.logger.error("Error getting boards from home. Status code: %s", response.status_code)
            return None

    def get_board_by_id(self, board_id):
        """
        Get a board by its ID.
        Note: Only the top level elements are loaded. Use get_board_sub_elements to get a Board's the sub elements.
        """

        self.logger.debug("Getting board by id: %s", board_id)
        response = requests.get(BOARD_BASE_URL + board_id, headers=self.headers, cookies=self.cookies,
                                params={"loadAncestors": "false"})

        if response.status_code == 200:
            response_json = response.json()
            if "errors" in response_json:
                if board_id in response_json["errors"]:
                    if response_json["errors"][board_id]["error"]["code"] == "BOARD_NOT_FOUND":
                        raise BoardNotFoundError(response_json, "Board not found.")
                else:
                    raise UnknownError(response_json, "Unknown error.")

            if response_json["elements"][board_id]["elementType"] == "SKELETON":
                raise NotAuthorizedError(response_json, "Not authorized. Please check your cookies and headers.")

            board_json = response_json["elements"][board_id]
            response_json["elements"].pop(board_id)
            elements_json = response_json["elements"]
            comments_json = response_json["comments"]
            return Board(board_json, elements_json, comments_json)
        else:
            self.logger.error("Error getting board by id. Response status code: %s", response.status_code)
            return None

    def get_board_elements(self, board: Board):
        """
        Get the elements of a board.
        """

        self.logger.debug("Getting board sub elements")
        response = requests.get(BOARD_BASE_URL + board.id, headers=self.headers, cookies=self.cookies,
                                params={"loadAncestors": "false"})
        if response.status_code == 200:
            response_json = response.json()
            response_json["elements"].pop(board.id)
            elements_json = response_json["elements"]
            comments_json = response_json["comments"]
            board.init_elements(elements_json, comments_json)
        else:
            self.logger.error("Error getting board sub elements. Status code: %s", response.status_code)
            return None

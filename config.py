import json

token = ""


def load_config() -> None:
    # global variables
    global token

    # loading data
    data = read_json("config.json")

    # loading token from data.
    token = data['token']


def read_json(json_file) -> dict:
    with open(json_file, "r") as file:
        return json.load(file)


def get_token() -> str:
    """
    get the value of token variable.
    """
    return token


if __name__ != "__main__":
    load_config()

from pprint import pprint
from src.api.request import make_get_request


def main():
    pprint(make_get_request("https://api.tcgdex.net/v2/en/cards/swsh3-136"))


if __name__ == "__main__":
    main()

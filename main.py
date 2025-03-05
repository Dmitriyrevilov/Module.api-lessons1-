import requests
from urllib.parse import urljoin


def get_weather_of_places(place):
    base_url = "http://wttr.in/"
    payload = {
        "n": "",
        "T": "",
        "q": "",
        "m": "",
        "lang": "ru",
    }

    url = urljoin(base_url, place)
    response = requests.get(url, params=payload)
    response.raise_for_status()
    return response.text


def main():
    places = [
        "~Череповец",
        "~paris",
        "~svo",
    ]
    for place in places:
        print(get_weather_of_places(place))


if __name__ == "__main__":
    main()

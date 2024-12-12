from typing import Any
import requests as req

type ResponseValues = str | int | bool


# def make_get_request(url: str) -> dict[str, ResponseValues]:
def make_get_request(url: str) -> Any:
    res: req.Response = req.get(url)

    if res.status_code != req.codes.ok:
        res.raise_for_status()

    res_json = res.json()
    return res_json

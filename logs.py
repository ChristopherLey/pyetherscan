from typing import Dict
from typing import Union

import requests


class Logs(object):
    """
    Python endpoint wrapper for Logs api at etherscan,
    see: https://docs.etherscan.io/api-endpoints/logs for more details
    """

    def __init__(self, key: str, endpoint: str):
        self.endpoint = endpoint
        self.params = {"apikey": key, "module": "logs"}

    def _get_request(self, params: dict) -> Dict[str, Union[str, float, int]]:
        return requests.get(self.endpoint, params=params).json()

from typing import Dict
from typing import Union

import requests


class Transactions(object):
    """
    Python endpoint wrapper for Transactions api at etherscan,
    see: https://docs.etherscan.io/api-endpoints/stats for more details
    """

    def __init__(self, key: str, endpoint: str):
        self.endpoint = endpoint
        self.params = {"apikey": key, "module": "transaction"}

    def _get_request(self, params: dict) -> Dict[str, Union[str, float, int]]:
        return requests.get(self.endpoint, params=params).json()

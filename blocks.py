from typing import Dict
from typing import Union

import requests


class Blocks(object):
    """
    Python endpoint wrapper for Blocks api at etherscan,
    see: https://docs.etherscan.io/api-endpoints/blocks for more details
    """

    def __init__(self, key: str, endpoint: str):
        self.endpoint = endpoint
        self.params = {"apikey": key, "module": "block"}

    def _get_request(self, params: dict) -> Dict[str, Union[str, float, int]]:
        return requests.get(self.endpoint, params=params).json()

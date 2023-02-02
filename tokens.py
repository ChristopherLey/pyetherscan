from typing import Dict
from typing import Union

import requests


class Tokens(object):
    """
    Python endpoint wrapper for Tokens api at etherscan,
    see: https://docs.etherscan.io/api-endpoints/tokens for more details
    """

    def __init__(self, key: str, endpoint: str):
        self.endpoint = endpoint
        self.params = {"apikey": key, "module": "stats"}

    def _get_request(self, params: dict) -> Dict[str, Union[str, float, int]]:
        return requests.get(self.endpoint, params=params).json()

    def tokensupply(  # noqa
        self,
        contractaddress: str,
    ) -> Dict[str, Union[str, float, int]]:
        """
        Returns the current amount of an ERC-20 token in circulation.

        Tip: The result is returned in the token's smallest decimal representation.
            Eg. a token with a balance of 215.241526476136819398 and 18 decimal places will be returned
            as 215241526476136819398
        """
        schema = {
            **self.params,
            "action": "tokensupply",
            "contractaddress": contractaddress,
        }
        return self._get_request(schema)

    def tokenbalance(  # noqa
        self, contractaddress: str, address: str, tag: str = "latest"
    ) -> Dict[str, Union[str, float, int]]:
        """
        Returns the current balance of an ERC-20 token of an address.
        """
        schema = {
            **self.params,
            "module": "account",
            "action": "tokenbalance",
            "contractaddress": contractaddress,
            "address": address,
            "tag": tag,
        }
        return self._get_request(schema)

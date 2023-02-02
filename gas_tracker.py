from typing import Dict
from typing import Union

import requests


class GasTracker(object):
    """
    Python endpoint wrapper for Gas Tracker api at etherscan,
    see: https://docs.etherscan.io/api-endpoints/gas-tracker for more details
    """

    def __init__(self, key: str, endpoint: str):
        self.endpoint = endpoint
        self.params = {"apikey": key, "module": "gastracker"}

    def _get_request(self, params: dict) -> Dict[str, Union[str, float, int]]:
        return requests.get(self.endpoint, params=params).json()

    def gasestimate(self, gasprice: int) -> Dict[str, Union[str, float, int]]:  # noqa
        """
        Returns the estimated time, in seconds, for a transaction to be confirmed on the blockchain.
        """
        schema = {**self.params, "action": "gasestimate", "gasprice": gasprice}
        return self._get_request(schema)

    def gasoracle(  # noqa
        self,
    ) -> Dict[str, Union[str, float, int]]:
        """
        Returns the current Safe, Proposed and Fast gas prices.
        """
        schema = {
            **self.params,
            "action": "gasoracle",
        }
        return self._get_request(schema)

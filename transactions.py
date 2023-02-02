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

    def getstatus(
        self,
        txhash: str,
    ) -> Dict[str, Union[str, float, int]]:
        """
        Returns the status code of a contract execution.
        """
        schema = {**self.params, "action": "getstatus", "txhash": txhash}
        return self._get_request(schema)

    def gettxreceiptstatus(
        self,
        txhash: str,
    ) -> Dict[str, Union[str, float, int]]:
        """
        Returns the status code of a transaction execution.

        Note: Only applicable for post Byzantium Fork transactions.
        https://www.investopedia.com/news/what-byzantium-hard-fork-ethereum/
        """
        schema = {**self.params, "action": "gettxreceiptstatus", "txhash": txhash}
        return self._get_request(schema)

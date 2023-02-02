from typing import Dict
from typing import Union

import requests


class Stats(object):
    """
    Python endpoint wrapper for Stats api at etherscan,
    see: https://docs.etherscan.io/api-endpoints/stats-1 for more details
    """

    def __init__(self, key: str, endpoint: str):
        self.endpoint = endpoint
        self.params = {"apikey": key, "module": "stats"}

    def _get_request(self, params: dict) -> Dict[str, Union[str, float, int]]:
        return requests.get(self.endpoint, params=params).json()

    def ethsupply(  # noqa
        self,
    ) -> Dict[str, Union[str, float, int]]:
        """
        Returns the current amount of Ether in circulation excluding ETH2 Staking rewards and EIP1559 burnt fees.
        """
        schema = {
            **self.params,
            "action": "ethsupply",
        }
        return self._get_request(schema)

    def ethsupply2(  # noqa
        self,
    ) -> Dict[str, Union[str, float, int]]:
        """
        Returns the current amount of Ether in circulation, ETH2 Staking rewards and EIP1559 burnt fees statistics.
        """
        schema = {
            **self.params,
            "action": "ethsupply2",
        }
        return self._get_request(schema)

    def ethprice(  # noqa
        self,
    ) -> Dict[str, Union[str, float, int]]:
        """
        Returns the latest price of 1 ETH.
        """
        schema = {
            **self.params,
            "action": "ethprice",
        }
        return self._get_request(schema)

    def chainsize(  # noqa
        self,
        start_date: str,
        end_date: str,
        client_type: str = "geth",
        sync_mode: str = "default",
        sort: str = "asc",
    ) -> Dict[str, Union[str, float, int]]:
        """
        Returns the size of the Ethereum blockchain, in bytes, over a date range.
        """
        schema = {
            **self.params,
            "action": "chainsize",
            "startdate": start_date,
            "enddate": end_date,
            "clienttype": client_type,
            "syncmode": sync_mode,
            "sort": sort,
        }
        return self._get_request(schema)

    def nodecount(  # noqa
        self,
    ) -> Dict[str, Union[str, float, int]]:
        """
        Returns the total number of discoverable Ethereum nodes.
        """
        schema = {
            **self.params,
            "action": "nodecount",
        }
        return self._get_request(schema)

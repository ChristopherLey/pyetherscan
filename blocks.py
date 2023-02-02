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

    def getblockreward(  # noqa
        self, block_no: int
    ) -> Dict[str, Union[str, float, int]]:
        """
        Returns the block reward and 'Uncle' block rewards.
        """
        schema = {**self.params, "action": "getblockreward", "blockno": block_no}
        return self._get_request(schema)

    def getblockcountdown(  # noqa
        self, block_no: int
    ) -> Dict[str, Union[str, float, int]]:
        """
        Returns the estimated time remaining, in seconds, until a certain block is mined.
        """
        schema = {**self.params, "action": "getblockcountdown", "blockno": block_no}
        return self._get_request(schema)

    def getblocknobytime(  # noqa
        self, timestamp: int, closest: str = "before"
    ) -> Dict[str, Union[str, float, int]]:
        """
        Returns the block number that was mined at a certain timestamp.
        """
        schema = {
            **self.params,
            "action": "getblocknobytime",
            "timestamp": timestamp,
            "closest": closest,
        }
        return self._get_request(schema)

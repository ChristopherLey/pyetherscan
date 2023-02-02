from typing import Dict
from typing import Union
from warnings import warn

import requests

from .utils import convert_wei2ether


class Proxy(object):
    """
    Python endpoint wrapper for Geth/Parity Proxy api at etherscan,
    see: https://docs.etherscan.io/api-endpoints/geth-parity-proxy for more details
    """

    def __init__(self, key: str, endpoint: str):
        self.endpoint = endpoint
        self.params = {"apikey": key, "module": "proxy"}

    def _get_request(self, params: dict) -> Dict[str, Union[str, float, int]]:
        return requests.get(self.endpoint, params=params).json()

    def eth_blockNumber(self) -> Dict[str, Union[str, float, int]]:
        """
        Returns the number of most recent block
        """
        schema = {
            **self.params,
            "action": "eth_blockNumber",
        }
        return self._get_request(schema)

    def eth_getBlockByNumber(
        self, tag: str, boolean: bool = True
    ) -> Dict[str, Union[str, float, int]]:
        """
        Returns information about a block by block number.
        """
        schema = {
            **self.params,
            "action": "eth_getBlockByNumber",
            "tag": tag,
            "boolean": boolean,
        }
        return self._get_request(schema)

    def eth_getUncleByBlockNumberAndIndex(
        self, tag: str, index: str
    ) -> Dict[str, Union[str, float, int]]:
        """
        Returns information about a uncle by block number.
        """
        schema = {
            **self.params,
            "action": "eth_getUncleByBlockNumberAndIndex",
            "tag": tag,
            "index": index,
        }
        return self._get_request(schema)

    def eth_getBlockTransactionCountByNumber(
        self, tag: str
    ) -> Dict[str, Union[str, float, int]]:
        """
        Returns the number of transactions in a block.
        """
        schema = {
            **self.params,
            "action": "eth_getBlockTransactionCountByNumber",
            "tag": tag,
        }
        return self._get_request(schema)

    def eth_getTransactionByHash(
        self, txhash: str
    ) -> Dict[str, Union[str, float, int]]:
        """
        Returns the information about a transaction requested by transaction hash.
        """
        schema = {**self.params, "action": "eth_getTransactionByHash", "txhash": txhash}
        return self._get_request(schema)

    def eth_getTransactionByBlockNumberAndIndex(
        self, tag: str, index: str
    ) -> Dict[str, Union[str, float, int]]:
        """
        Returns information about a transaction by block number and transaction index position.
        """
        schema = {
            **self.params,
            "action": "eth_getTransactionByBlockNumberAndIndex",
            "tag": tag,
            "index": index,
        }
        return self._get_request(schema)

    def eth_getTransactionCount(
        self, address: str, tag: str = "latest"
    ) -> Dict[str, Union[str, float, int]]:
        """
        Returns the number of transactions performed by an address.
        """
        schema = {
            **self.params,
            "action": "eth_getTransactionCount",
            "address": address,
            "tag": tag,
        }
        return self._get_request(schema)

    def eth_sendRawTransaction(self, hex: str) -> Dict[str, Union[str, float, int]]:
        """
        Submits a pre-signed transaction for broadcast to the Ethereum network.
        """
        schema = {
            **self.params,
            "action": "eth_sendRawTransaction",
            "hex": hex,
        }
        return self._get_request(schema)

    def eth_getTransactionReceipt(
        self, txhash: str
    ) -> Dict[str, Union[str, float, int]]:
        """
        Returns the receipt of a transaction by transaction hash.
        """
        schema = {
            **self.params,
            "action": "eth_getTransactionReceipt",
            "txhash": txhash,
        }
        return self._get_request(schema)

    def eth_call(
        self, to: str, data: str, tag: str = "latest"
    ) -> Dict[str, Union[str, float, int]]:
        """
        Executes a new message call immediately without creating a transaction on the blockchain.
        """
        schema = {**self.params, "action": "eth_call", "data": data, "tag": tag}
        return self._get_request(schema)

    def eth_getCode(
        self, address: str, tag: str = "latest"
    ) -> Dict[str, Union[str, float, int]]:
        """
        Returns code at a given address.
        """
        schema = {**self.params, "action": "eth_call", "address": address, "tag": tag}
        return self._get_request(schema)

    def eth_getStorageAt(
        self, address: str, position: str, tag: str = "latest"
    ) -> Dict[str, Union[str, float, int]]:
        """
        Returns the value from a storage position at a given address.

        Warning: This endpoint is still experimental and may have potential issues
        """
        warn("This endpoint is still __experimental__ and may have potential issues")
        schema = {
            **self.params,
            "action": "eth_call",
            "address": address,
            "position": position,
            "tag": tag,
        }
        return self._get_request(schema)

    def eth_gasPrice(self, in_wei: bool = True) -> Dict[str, Union[str, float, int]]:
        """
        Returns the current price per gas in wei.
        """
        schema = {
            **self.params,
            "action": "eth_gasPrice",
        }
        response = self._get_request(schema)
        if not in_wei:
            if "result" in response:
                response["result"] = convert_wei2ether(response["result"])
        return response

    def eth_estimateGas(
        self, data: str, to: str, value: str, gas_price: str, gas: str
    ) -> Dict[str, Union[str, float, int]]:
        """
        Makes a call or transaction, which won't be added to the blockchain and returns the used gas.
        """
        schema = {
            **self.params,
            "action": "eth_estimateGas",
            "data": data,
            "to": to,
            "value": value,
            "gasPrice": gas_price,
            "gas": gas,
        }
        return self._get_request(schema)

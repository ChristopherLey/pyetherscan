from typing import Dict
from typing import Union

import requests


class Accounts(object):
    """
    Python endpoint wrapper for Accounts api at etherscan,
    see: https://docs.etherscan.io/api-endpoints/accounts for more details
    """

    def __init__(self, key: str, endpoint: str):
        self.endpoint = endpoint
        self.params = {"apikey": key, "module": "account"}

    def _get_request(self, params: dict) -> Dict[str, Union[str, float, int]]:
        return requests.get(self.endpoint, params=params).json()

    def balance(
        self, address: str, tag: str = "latest"
    ) -> Dict[str, Union[str, float, int]]:
        """
        Returns the Ether balance of a given address.
        """
        schema = {**self.params, "action": "balance", "address": address, "tag": tag}
        return self._get_request(schema)

    def balancemulti(  # noqa
        self, address: list, tag: str = "latest"
    ) -> Dict[str, Union[str, float, int]]:
        """
        Returns the balance of the accounts from a list of addresses.
        """
        schema = {
            **self.params,
            "action": "balancemulti",
            "address": address,
            "tag": tag,
        }
        return self._get_request(schema)

    def txlist(  # noqa
        self,
        address: str,
        start_block: int,
        end_block: int,
        page: int = 1,
        offset: int = 10,
        sort: str = "asc",
    ) -> Dict[str, Union[str, float, int]]:
        """
        Returns the list of transactions performed by an address, with optional pagination.

        Note : This API endpoint returns a maximum of 10000 records only.
        """
        schema = {
            **self.params,
            "action": "txlist",
            "address": address,
            "startblock": start_block,
            "endblock": end_block,
            "page": page,
            "offset": offset,
            "sort": sort,
        }
        return self._get_request(schema)

    def txlistinternal(  # noqa
        self,
        start_block: int,
        end_block: int,
        txhash: str = None,
        address: str = None,
        page: int = 1,
        offset: int = 10,
        sort: str = "asc",
    ) -> Dict[str, Union[str, float, int]]:
        """
        if txhash is not None: Returns the list of internal transactions performed within a transaction.
        elseif address is not None: Returns the list of transactions performed by an address, with optional pagination.
        else: Returns the list of internal transactions performed within a block range, with optional pagination.

        Note : This API endpoint returns a maximum of 10000 records only.
        """
        schema = {
            **self.params,
            "action": "txlistinternal",
        }
        if txhash is None:
            schema = {
                **schema,
                "startblock": str(start_block),
                "endblock": str(end_block),
                "page": str(page),
                "offset": str(offset),
                "sort": sort,
            }
            if address is not None:
                schema["address"] = address
        else:
            schema = {**schema, "txhash": txhash}
        return self._get_request(schema)

    def tokentx(  # noqa
        self,
        contract_address: str,
        address: str,
        start_block: int,
        end_block: int,
        page: int = 1,
        offset: int = 10,
        sort: str = "asc",
    ) -> Dict[str, Union[str, float, int]]:
        """
        Returns the list of ERC-20 tokens transferred by an address, with optional filtering by token contract.

        Usage:
            -   ERC-20 transfers from an address, specify the address parameter
            -   ERC-20 transfers from a contract address, specify the contract address parameter
            -   ERC-20 transfers from an address filtered by a token contract, specify both address and contract
                address parameters.
        """
        schema = {
            **self.params,
            "action": "tokentx",
            "contractaddress": contract_address,
            "address": address,
            "startblock": start_block,
            "endblock": end_block,
            "page": page,
            "offset": offset,
            "sort": sort,
        }
        return self._get_request(schema)

    def tokennfttx(  # noqa
        self,
        contract_address: str,
        address: str,
        start_block: int,
        end_block: int,
        page: int = 1,
        offset: int = 10,
        sort: str = "asc",
    ) -> Dict[str, Union[str, float, int]]:
        """
        Returns the list of ERC-721 (NFT) tokens transferred by an address, with optional filtering by token contract.

        Usage:
        -   ERC-721 transfers from an address, specify the address parameter
        -   ERC-721 transfers from a contract address, specify the contract address parameter
        -   ERC-721 transfers from an address filtered by a token contract, specify both address and contract
            address parameters.
        """
        schema = {
            **self.params,
            "action": "tokennfttx",
            "contractaddress": contract_address,
            "address": address,
            "startblock": start_block,
            "endblock": end_block,
            "page": page,
            "offset": offset,
            "sort": sort,
        }
        return self._get_request(schema)

    def token1155tx(  # noqa
        self,
        contract_address: str,
        address: str,
        start_block: int,
        end_block: int,
        page: int = 1,
        offset: int = 10,
        sort: str = "asc",
    ) -> Dict[str, Union[str, float, int]]:
        """
        Returns the list of ERC-1155 ( Multi Token Standard ) tokens transferred by an address, with optional filtering
        by token contract.

        Usage:
        -   ERC-1155 transfers from an address, specify the address parameter
        -   ERC-1155 transfers from a contract address, specify the contract address parameter
        -   ERC-1155 transfers from an address filtered by a token contract, specify both address and contract
            address parameters.
        """
        schema = {
            **self.params,
            "action": "token1155tx",
            "contractaddress": contract_address,
            "address": address,
            "startblock": start_block,
            "endblock": end_block,
            "page": page,
            "offset": offset,
            "sort": sort,
        }
        return self._get_request(schema)

    def getminedblocks(  # noqa
        self,
        address: str,
        blocktype: str = "blocks",
        page: int = 1,
        offset: int = 10,
    ) -> Dict[str, Union[str, float, int]]:
        """
        Returns the list of blocks mined by an address.

        Note : The timeStamp is represented in Unix timestamp.
        """
        schema = {
            **self.params,
            "action": "getminedblocks",
            "address": address,
            "blocktype": blocktype,
            "page": page,
            "offset": offset,
        }
        return self._get_request(schema)

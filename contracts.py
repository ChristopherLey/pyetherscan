from typing import Dict
from typing import List
from typing import Union
from warnings import warn

import requests


class Contracts(object):
    """
    Python endpoint wrapper for Contracts api at etherscan,
    see: https://docs.etherscan.io/api-endpoints/contracts for more details
    Find verified contracts on etherscan Verified Contracts Source Code page: https://etherscan.io/contractsVerified
    """

    def __init__(self, key: str, endpoint: str):
        self.endpoint = endpoint
        self.params = {"apikey": key, "module": "contract"}

    def _get_request(self, params: dict) -> Dict[str, Union[str, float, int]]:
        return requests.get(self.endpoint, params=params).json()

    def _post_request(
        self, data: dict, params: dict = None
    ) -> Dict[str, Union[str, float, int]]:
        return requests.post(self.endpoint, data=data, params=params).json()

    def getabi(self, address: str) -> Dict[str, Union[str, float, int]]:  # noqa
        """
        Returns the Contract Application Binary Interface ( ABI ) of a verified smart contract.
        """
        schema = {**self.params, "action": "getabi", "address": address}
        return self._get_request(schema)

    def getsourcecode(self, address: str) -> Dict[str, Union[str, float, int]]:  # noqa
        """
        Returns the Solidity source code of a verified smart contract.
        """
        schema = {**self.params, "action": "getsourcecode", "address": address}
        return self._get_request(schema)

    def getcontractcreation(  # noqa
        self, contract_addresses: List[str]
    ) -> Dict[str, Union[str, float, int]]:
        """
        Returns a contract's deployer address and transaction hash it was created, up to 5 at a time.
        """
        schema = {
            **self.params,
            "action": "getcontractcreation",
            "contractaddresses": contract_addresses,
        }
        return self._get_request(schema)

    def verifysourcecode(self, data: dict) -> Dict[str, Union[str, float, int]]:  # noqa
        """
        Verify Source Code
        Submits a contract source code to Etherscan for verification.

        Note : This endpoint is limited to 100 verifications/day, regardless of API PRO tier.

        1. Requires a valid Etherscan API key, it will be rejected otherwise
        2. Supports up to 10 different library pairs
        3. Contracts that use "imports" will need to have the code concatenated into one file as we do not support
        "imports" in separate files.
        4. List of supported solc versions, only solc version v0.4.11 and above is supported e.g.
        v0.4.25+commit.59dbf8f1
        5. Upon successful submission you will receive a GUID (50 characters) as a receipt
        6. You may use this GUID to track the status of your submission
        7. Verified Source Codes will be displayed at the Verified Contracts
        page (https://etherscan.io/contractsVerified).

        Warning: This has not been tested, no warranty is given for correct execution

        ::params::
        data: dict: see https://docs.etherscan.io/api-endpoints/contracts#source-code-submission-gist for data format
        Note: data object sent in the form:
        data = {
            **data,
            apikey: <included api key>,
            module: 'contract',
            action: 'verifysourcecode'
        }
        """
        warn("This has not been tested, no warranty is given for correct execution!")
        data = {**data, **self.params, "action": "verifysourcecode"}
        return self._post_request(data)

    def checkverifystatus(self, guid: str) -> Dict[str, Union[str, float, int]]:  # noqa
        """
        Upon successful submission, a GUID is returned, which can be used to check for submission status.
        """
        schema = {**self.params, "action": "checkverifystatus", "guid": guid}
        return self._get_request(schema)

    def verifyproxycontract(  # noqa
        self, address: str, expected_implementation: str = None
    ) -> Dict[str, Union[str, float, int]]:
        """
        Submits a proxy contract source code to Etherscan for verification.
        1. Requires a valid Etherscan API key, it will be rejected otherwise
        2. Current daily limit of 100 submissions per day per user (subject to change)
        3. Upon successful submission you will receive a GUID (50 characters) as a receipt
        4. You may use this GUID to track the status of your submission
        5. Verified proxy contracts will display the "Read/Write as Proxy" of the implementation contract under the
        contract address's contract tab

        Warning: This has not been tested, no warranty is given for correct execution
        see https://docs.etherscan.io/api-endpoints/contracts#verify-proxy-contract for correct parameters
        """
        warn("This has not been tested, no warranty is given for correct execution!")
        schema = {
            **self.params,
            "action": "verifyproxycontract",
        }
        data = {"address": address, "expectedimplementation": expected_implementation}
        return self._post_request(data=data, params=schema)

    def checkproxyverification(  # noqa
        self, guid: str
    ) -> Dict[str, Union[str, float, int]]:
        """
        Upon successful submission, a GUID is returned, which can be used to check for submission status.
        """
        schema = {**self.params, "action": "checkproxyverification", "guid": guid}
        return self._get_request(schema)

from typing import Dict
from typing import List
from typing import Optional
from typing import Union

import requests


class Logs(object):
    """
    Python endpoint wrapper for Logs api at etherscan,
    see: https://docs.etherscan.io/api-endpoints/logs for more details
    """

    def __init__(self, key: str, endpoint: str):
        self.endpoint = endpoint
        self.params = {"apikey": key, "module": "logs"}

    def _get_request(self, params: dict) -> Dict[str, Union[str, float, int]]:
        return requests.get(self.endpoint, params=params).json()

    def getLogs(
        self,
        address: str,
        from_block: Optional[int] = None,
        to_block: Optional[int] = None,
        page: int = 1,
        offset: int = 1000,
        topics: List[tuple] = None,
    ) -> Dict[str, Union[str, float, int]]:
        """
        Returns the event logs from an address, with optional filtering by block range and/or topics
        """
        schema = {
            **self.params,
            "action": "getLogs",
            "address": address,
            "fromBlock": from_block,
            "toBlock": to_block,
            "page": page,
            "offset": offset,
        }
        if topics is not None:
            if len(topics) == 1:
                schema["topic0"] = topics[0][0]
            for i, topic in enumerate(topics):
                schema[f"topic{i}"] = topic[0]
                if i != len(topics) - 1:
                    schema[f"topic{i}_{i+1}_opr"] = topic[1]
        return self._get_request(schema)


def test_logs():
    import yaml

    config = yaml.load(open("../user_config.yaml", "r"), yaml.Loader)
    my_key = config["etherscan_key"]

    logs = Logs(my_key, "https://api.etherscan.io/api")
    response = logs.getLogs(
        "0xbd3531da5cf5857e7cfaa92426877b022e612cf8",
        topics=[
            (
                "0x27c4f0403323142b599832f26acd21c74a9e5b809f2215726e244a4ac588cd7d",
                "and",
            ),
            ("0x00000000000000000000000023581767a106ae21c074b2276d25e5c3e136a68b",),
        ],
    )
    print(response)

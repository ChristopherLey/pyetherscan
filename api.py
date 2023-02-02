from .accounts import Accounts
from .blocks import Blocks
from .contracts import Contracts
from .gas_tracker import GasTracker
from .logs import Logs
from .proxy import Proxy
from .stats import Stats
from .tokens import Tokens
from .transactions import Transactions


class Connector(object):
    """
    Etherscan api connector, see https://docs.etherscan.io/ for more details
    """

    def __init__(self, key: str, endpoint: str = "https://api.etherscan.io/api"):
        self.endpoint = endpoint
        self.proxy = Proxy(key, endpoint)
        self.accounts = Accounts(key, endpoint)
        self.contacts = Contracts(key, endpoint)
        self.transactions = Transactions(key, endpoint)
        self.blocks = Blocks(key, endpoint)
        self.logs = Logs(key, endpoint)
        self.tokens = Tokens(key, endpoint)
        self.gas_tracker = GasTracker(key, endpoint)
        self.stats = Stats(key, endpoint)

# pyetherscan
A helper module for wrapping [etherscan api](https://docs.etherscan.io/api-endpoints/accounts) functionality.

## Examples:
    
    import yaml
    from pprint import pprint
    from pyetherscan.api import Connector

    config = yaml.load(open('../user_config.yaml', 'r'), yaml.Loader)
    my_key = config['etherscan_key']
    
    etherscan = Connector(my_key)
    
    last_block_number = etherscan.proxy.eth_blockNumber()
    print(last_block_number)

    pprint(etherscan.proxy.eth_getBlockByNumber(last_block_number['result']))


### Best practices
It is required that before pushing that the staged commits __pass__ the `pre-commit`, this involves running

    pre-commit run

which will sanitise the currently staged commits according the repositories rules, this may require a few passes and
perhaps manual intervention (fixes). You should be able to run

    pre-commit run --all

without errors, if not please correct before creating a pull request!
These sanitary practices will aid in code readability and speed up pull requests.

Please also strive to write self documenting code or documentation strings were needed (sparingly)!

__Type hints__ are strongly encouraged!
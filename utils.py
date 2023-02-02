from typing import Union

Ether2Wei = 1e18
Ether2KWei = 1e15
Ether2MWei = 1e12
Ether2GWei = 1e9
Ether2Szabo = 1e6
Ether2Finney = 1e3
Ether2KEther = 1e-3
Ether2MEther = 1e-6
Ether2GEther = 1e-9
Ether2TEther = 1e-12


def convert_wei2ether(wei: Union[float, int, str]) -> Union[float, str]:
    if isinstance(wei, str):
        if wei[:2] == "0x":
            return int(wei, 16) / Ether2Wei
        else:
            return float(wei) / Ether2Wei
    return float(wei) / Ether2Wei


def convert_ether2wei(eth: float) -> float:
    return eth * Ether2Wei

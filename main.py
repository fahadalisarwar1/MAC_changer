#!/bin/python3.8
from core.MacChanger import MACChanger


if __name__ == "__main__":
    mc = MACChanger()
    res_mac = mc.Change_MAC("wlp6s0", "00:11:23:33:44:59")
    print("[+] updated MAC address is ", res_mac)


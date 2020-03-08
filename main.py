#!/bin/python3.8
from core.MacChanger import MACChanger


if __name__ == "__main__":
    mc = MACChanger()
    print("[+] Current MAC is ", mc.getMAC("wlp6s0"))
    res_mac = mc.Change_MAC("wlp6s0", "00:22:23:13:44:59")
    print("[+] updated MAC address is ", res_mac)


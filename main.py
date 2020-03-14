#!/bin/python3
from core.MacChanger import MACChanger
import argparse


if __name__ == "__main__":
    
    parser = argparse.ArgumentParser()
    
    parser.add_argument("-i", "--interface", help="Interface for which you want to change MAC address", required=True)
    parser.add_argument("-m", "--newmac", help="New MAC address", required=True)
    
    args = parser.parse_args()
    iface = args.interface
    new_mac = args.newmac

    
    mc = MACChanger()
    print("[+] Current MAC is ", mc.getMAC(iface))
    res_mac = mc.Change_MAC(iface, new_mac)
    print("[+] updated MAC address is ", res_mac)


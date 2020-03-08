import subprocess
import re


class MACChanger:
    def __init__(self):
        self.MAC = ""

    def getIP(self, iface):
        output = subprocess.run(["ifconfig", iface], shell=False, capture_output=True)

        pattern = r'inet\s[^a-z]*[.]1[^a-z]*[.]1[^a-z]'

        cmd_result = output.stdout.decode('utf-8')
        regex = re.compile(pattern)
        ans = regex.search(cmd_result)

        found_ip = ans.group().split(" ")[1]
        print("[+] Found ip: ", found_ip)

        return found_ip

    def getMAC(self, iface):
        output = subprocess.run(["ifconfig", iface], shell=False, capture_output=True)

        pattern = r'ether\s{1}[\da-z]{2}:[\da-z]{2}:[\da-z]{2}:[\da-z]{2}:[\da-z]{2}:[\da-z]{2}'

        cmd_result = output.stdout.decode('utf-8')
        regex = re.compile(pattern)
        ans = regex.search(cmd_result)

        current_mac = ans.group().split(" ")[1]
        print("[+] Current MAC is : ", current_mac)
        return current_mac

    def Change_MAC(self, iface, newMAC):
        print("[+] Changing MAC for ", iface, " to ", newMAC)
        self.MAC = self.getMAC(iface=iface)
        print("[+] Shutting down interface ", iface)
        output = subprocess.run(["ifconfig", iface, "down"], shell=False, capture_output=True)
        cmd_result = output.stderr.decode('utf-8')
        print("[+] Changing MAC address to ", newMAC)
        output = subprocess.run(["ifconfig", iface, "hw", "ether", newMAC], shell=False, capture_output=True)
        cmd_result = output.stderr.decode('utf-8')

        output = subprocess.run(["ifconfig", iface, "up"], shell=False, capture_output=True)
        cmd_result = output.stderr.decode('utf-8')
        return self.getMAC(iface)

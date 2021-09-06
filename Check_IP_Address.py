#Check for valid IPv4 and IPv6 else return Neither
class Solution:
    def validIPAddress(self, IP: str) -> str:
        res = 0
        ipv4 = IP.split('.')
        if len(ipv4) == 4:
            for x in ipv4:
                if x == '' or (x[0] == '0' and len(x) != 1) or not x.isdigit() or int(x) > 255:
                    res = 1
                    break
            if not res:
                return 'IPv4'
        
        ipv6 = IP.split()
        if len(ipv6) == 8:
            for x in ipv6:
                if x == '' or len(x) > 4 or not all(i in hexdigits for i in x):
                    res = 1
                    break
            if not res:
                return 'IPv6'
                    
        return 'Neither'

print(Check_IP_Address('An.123.122.111'))

"""Check that the entered IP address is valid or not
Condition 1 : It should be in the form of XXX-XXX-XXX-XXX
XXX should be in between 0 and 255"""
def Check_IP_Address(String):
    String = String.split('.')
    for (i) in String:
        if not i.isdigit():
            return False
        if (len(i)!= 4 or int(i) > 255 or int(i) <0):
            return False
    return True

print(Check_IP_Address('An.123.122.111'))
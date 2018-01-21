# You are driving a little too fast, and a police officer stops you. Write code to compute the result,
# encoded as an int value: 0=no ticket, 1=small ticket, 2=big ticket. If speed is 60 or less, the result is 0.
# If speed is between 61 and 80 inclusive, the result is 1. If speed is 81 or more, the result is 2.
# Unless it is your birthday -- on that day, your speed can be 5 higher in all cases.

# caught_speeding(60, False)
# caught_speeding(65, False)
# caught_speeding(65, True)

def caught_speeding(speed, is_birthday):
    speeding = speed - (65 if is_birthday else 60)
    if speeding > 20:
        return 2
    elif speeding >0:
        return 1
    else:
        return 0

print caught_speeding(60,False)
print caught_speeding(65, False)
print caught_speeding(65, True)
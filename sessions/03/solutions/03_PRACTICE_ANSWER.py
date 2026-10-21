# All measurements and counts are synthetic educational examples.
reading = 10
print(reading == 10)
print(reading != 10)
print(reading > 10)
print(reading < 10)
print(reading >= 10)
print(reading <= 10)
print(reading >= 0 and reading <= 20)
print(reading < 0 or reading > 20)
print(not reading == 10)
if reading > 0:
    print("Positive")
else:
    print("Not positive")
if reading < 10:
    print("Below")
elif reading <= 20:
    print("Inside")
else:
    print("Above")
if reading >= 0:
    if reading == 0:
        print("Zero")
    else:
        print("Positive valid")
else:
    print("Invalid")

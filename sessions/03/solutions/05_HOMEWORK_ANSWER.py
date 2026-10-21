# Synthetic educational seedling length, measured in millimetres (mm).
# Assume a finite numeric entry; text conversion errors are not handled yet.
length_mm = float(input("Fictional length (mm): "))
if length_mm < 0:
    print("Invalid: length must be nonnegative.")
elif length_mm == 0:
    print("Teaching range: zero")
elif length_mm < 10:
    print("Teaching range: short")
elif length_mm <= 20:
    print("Teaching range: middle")
else:
    print("Teaching range: long")

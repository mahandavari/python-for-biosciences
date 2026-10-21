# Synthetic educational seedling lengths in millimetres.
# Assume valid numeric input and nonnegative lengths.
first_length_mm = float(input("First length (mm): "))
second_length_mm = float(input("Second length (mm): "))
third_length_mm = float(input("Third length (mm): "))
mean_length_mm = (first_length_mm + second_length_mm + third_length_mm) / 3
print("Mean length (mm):", mean_length_mm)

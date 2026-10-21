# Synthetic educational examples.
sample_name = "Demo A"
sample_count = 3
length_mm = 12.5
is_synthetic = True
print(sample_name, type(sample_name))
print(type(sample_count))
print(type(length_mm))
print(type(is_synthetic))

reading_text = "12.5"
reading = float(reading_text)
count = int("8")
print(reading)
print(count + 2)

print(2 + 3 * 4)
print((2 + 3) * 4)
print(7 / 2)
print(7 // 2)
print(7 % 2)
print(2 ** 3)
first_length_mm = 8.0
second_length_mm = 10.0
third_length_mm = 12.0
mean_length_mm = (first_length_mm + second_length_mm + third_length_mm) / 3
print("Mean length (mm):", mean_length_mm)

a_count = 40
t_count = 20
g_count = 10
c_count = 10
total_count = a_count + t_count + g_count + c_count
gc_percent = (g_count + c_count) / total_count * 100
print("Total bases:", total_count)
print("GC percentage:", gc_percent)

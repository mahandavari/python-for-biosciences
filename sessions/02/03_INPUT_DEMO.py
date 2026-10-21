# Run after learning input() and int() in the lesson.
# Enter nonnegative whole counts; their total must be greater than zero.
# These are invented educational inputs, not experimental measurements.
a_count = int(input("A count: "))
t_count = int(input("T count: "))
g_count = int(input("G count: "))
c_count = int(input("C count: "))

total_count = a_count + t_count + g_count + c_count
gc_percent = (g_count + c_count) / total_count * 100
print("Total bases:", total_count)
print("GC percentage:", gc_percent)

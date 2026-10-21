# Synthetic educational counts, invented for arithmetic practice.
a_count = 30
t_count = 20
g_count = 25
c_count = 25

# Assume nonnegative whole counts and a total greater than zero.
total_count = a_count + t_count + g_count + c_count
gc_count = g_count + c_count
gc_percent = gc_count / total_count * 100

print("Total bases:", total_count)
print("GC percentage:", gc_percent)

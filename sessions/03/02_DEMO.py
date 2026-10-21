# Synthetic educational counts; enter whole numbers, without units.
a_count = int(input("A count: "))
t_count = int(input("T count: "))
g_count = int(input("G count: "))
c_count = int(input("C count: "))

if a_count < 0 or t_count < 0 or g_count < 0 or c_count < 0:
    print("Invalid: counts must be nonnegative.")
else:
    total_count = a_count + t_count + g_count + c_count
    if total_count == 0:
        print("Invalid: total must be positive.")
    else:
        gc_percent = (g_count + c_count) / total_count * 100
        print("Total bases:", total_count)
        print("GC percentage:", gc_percent)
        # These bands are classroom rules, not biological standards.
        if gc_percent < 40:
            print("Teaching band: low")
        elif gc_percent <= 60:
            print("Teaching band: middle")
        else:
            print("Teaching band: high")

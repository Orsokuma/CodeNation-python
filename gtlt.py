num_to_check = 5
for i in range(1, 10):
    if (i == num_to_check):
        print(f"{num_to_check} is equal to {i}")
    else:
        print("{} is {} than {}".format(
            num_to_check,
            "less" if i > num_to_check else "greater",
            i
        ))
# Multiplication tables!

def multiplication_table(table):
    # Count iterations
    cnt = 0;
    for i in range(0, 100, table):
        print(f"{cnt} x {table} = {i}");
        cnt += 1

table = input("Which multiplication table would you like?")
# 3x table
multiplication_table(int(table))
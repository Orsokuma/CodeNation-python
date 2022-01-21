from datetime import date

# Calculate days until next birthday: INPUT BIRTHYEAR-BIRTHMONTH-BIRTHDAY
birthday = date(1991, 8, 7);
def days_til_bornmas(birthday: date, today: date) -> int:
    this_year = (date(today.year, birthday.month, birthday.day) - today).days
    if this_year >= 0:
        return this_year

    next_year = (date(today.year + 1, birthday.month, birthday.day) - today).days
    return next_year

# days = days_til_bornmas(date(1991, 8, 7), date.today())
# print(days)

# Initialize a variable with spaces and a pipe symbol - this will be used to form the "walls" of the board
col = "   |"
# Initialize a variable with hyphens - this will be used to form the rows
row = "----"
# Initialize a blank string variable
out = ""

# A little hacky, but deal with it
# Loop through this segment 3 times (0->1->2)
for i in range(0, 2):
    # Add our "   |" to the `out` string twice, along with a newline character; then do that 3 times
    out += ((col * 2) + "\n") * 3
    # Add our ---- 3 times and a newline
    out += (row * 3) + "\n"
    # If we're in iteration 1 of the loop (the second iteration 0 -> *1* -> 2)
    if (i == 1):
        # Add our last 3 lines of "   |"
        out += ((col * 2) + "\n") * 3
# Finally, show it in the Terminal
print(out)
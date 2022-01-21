class bcolors:
    PURPLE = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    ORANGE = '\033[93m'
    RED = '\033[91m'
    GREY = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

print(bcolors.PURPLE+"Some text\n")
print(bcolors.BLUE+"Some text\n")
print(bcolors.CYAN+"Some text\n")
print(bcolors.GREEN+"Some text\n")
print(bcolors.ORANGE+"Some text\n")
print(bcolors.RED+"Some text\n")
print(bcolors.GREY+"Some text\n")
print(bcolors.BOLD+"Some text\n")
print(bcolors.UNDERLINE+"Some text\n")

for i in range(1, 50):
    print(f"{i} \033[1;33;{str(i)}mTest\033[0m")
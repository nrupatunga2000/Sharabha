#print 1 to 10 by not using loops
def print_numbers(n):
    if n <= 10:
        print(n)
        print_numbers(n + 1)

print_numbers(1)



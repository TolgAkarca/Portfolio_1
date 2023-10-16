def print_pyramid(n):
    for i in range(n):
        print(' ' * (n - i - 1) + '*' * (2 * i + 1) + ' ' * (n - i - 1))

rows = int(input("Enter the number of rows for the pyramid: "))
print_pyramid(rows)



def create_pyramid(n):
    pyramid = []
    for i in range(1, n+1):
        spaces = ' ' * (n - i)
        stars = '*' * i
        pyramid.append(spaces + stars)
    return pyramid

def reverse_pyramid(pyramid):
    pyramid.reverse()
    return pyramid

n = 5
pyramid = create_pyramid(n)
reversed_pyramid = reverse_pyramid(pyramid)

for line in reversed_pyramid:
    print(line)
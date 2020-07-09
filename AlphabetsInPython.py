from string import ascii_lowercase
from string import ascii_uppercase


to_print = ""
for alpha in ascii_lowercase:
    to_print = to_print + ", " + alpha

for alpha in ascii_uppercase:
    to_print = to_print + ", " + alpha

print(to_print)


def add_numbers(x, y, z=None):
    if z == None:
        return x + y
    else:
        return x + y + z


print(add_numbers(1, 2))
print(add_numbers(1, 2, 3))

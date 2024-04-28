"""
Recursion
"""


def do_it(n):
    """Do... it."""
    if n <= 0:
        return 0
    return n % 2 + do_it(n - 1)


print(do_it(5))


def do_something(n):
    """Print the squares of positive numbers from n down to 0."""
    if n <= 0:
        return 0
    else:
        print(n**2)
    return do_something(n - 1)


do_something(4)

blocks = 0
for n in range(0, 7, 1):
    blocks += n
print(blocks)


def do_block_count(n):
    """Prints blocks based on rows"""
    if n <= 0:
        return 0
    return n + do_block_count(n-1)


print(do_block_count(6))

import sys

print("First statement")
print("Second statement")
print("Third statement with multiple words")


def my_func():
    print("sys.copyright")


def my_func2():
    print(sys.copyright)


my_func()
my_func2()

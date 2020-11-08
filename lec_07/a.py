def foo(x):
    print(f'Вызвана функция foo({x})')


def bar(x, y):
    print(x + y)


def print_name():
    print(__name__)

print_name()
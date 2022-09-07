import typing as t

print()


class TestPrint:
    print = lambda: None  # noqa: E731

    def print_something(self):
        print("something")  # type: ignore

    def print_assign(self):
        self.print = None
        print = lambda: None  # noqa: E731
        print()


print()


class TestAnnPrint:
    print: t.Callable[[], None] = lambda: None

    def print_something(self):
        print("something")  # type: ignore

    def print_assign(self):
        self.print = lambda: None
        print: t.Callable[[], None] = lambda: None
        print()


print = lambda: None  # noqa: E731


print()

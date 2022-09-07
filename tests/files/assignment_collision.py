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


print = lambda: None  # noqa: E731


print()

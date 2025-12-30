from functions.run_python_file import run_python_file


def test():
    content = run_python_file("calculator", "main.py")
    print("Output of running 'main.py':")
    print(content)
    print("")

    content = run_python_file("calculator", "main.py", ["3 + 5"])
    print("Output of running 'main.py' with expression '3 + 5':")
    print(content)
    print("")

    content = run_python_file("calculator", "tests.py")
    print("Output of running 'tests.py':")
    print(content)
    print("")

    content = run_python_file("calculator", "../main.py")
    print("Output of running '../main.py':")
    print(content)
    print("")

    content = run_python_file("calculator", "nonexistent.py")
    print("Output of running 'nonexistent.py':")
    print(content)
    print("")

    content = run_python_file("calculator", "lorem.txt")
    print("Output of running 'lorem.txt':")
    print(content)
    print("")


if __name__ == "__main__":
    test()

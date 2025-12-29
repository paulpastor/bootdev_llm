from functions.get_file_content import get_file_content


def test():
    content = get_file_content("calculator", "lorem.txt")
    print("Content of 'lorem.txt':")
    print(content)
    print("")

    content = get_file_content("calculator", "main.py")
    print("Content of 'main.py':")
    print(content)
    print("")

    content = get_file_content("calculator", "pkg/calculator.py")
    print("Content of 'pkg/calculator.py':")
    print(content)
    print("")

    content = get_file_content("calculator", "/bin/cat")
    print("Content of '/bin/cat':")
    print(content)
    print("")

    content = get_file_content("calculator", "pkg/does_not_exist.py")
    print("Content of 'pkg/does_not_exist.py':")
    print(content)
    print("")


if __name__ == "__main__":
    test()

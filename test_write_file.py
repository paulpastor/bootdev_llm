from functions.write_file import write_file


def test():
    content = write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum")
    print(content)
    print("")

    content = write_file(
        "calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet"
    )
    print(content)
    print("")

    content = write_file("calculator", "/tmp/temp.txt", "this should not be allowed")
    print(content)
    print("")


if __name__ == "__main__":
    test()

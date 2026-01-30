def read_file(filename):
    filename = '../data/' + filename
    with open(filename, "r") as file:
        content = file.read()
    return content

if __name__ == "__main__":
    fn = input("Enter a file name: ")
    content = read_file(fn)
    print(f"Contents of {fn}:\n")
    print(content)
def write_file(filename, output):
    filename = '../data/' + filename
    output = output.replace("\\n", "\n") #to be able to print the actual newlines we need this
    with open(filename, "w") as file:
        file.write(output)

if __name__ == "__main__":
    fn = input("Enter a file name: ")
    op = input("What do u wanna add to the file: ")
    write_file(fn, op)

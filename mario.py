def main():
    print_column(3)
    print_row(4)
    print_square(6)


def print_column(height):
    for _ in range(height):
        print("#")

def print_row(width):
    print("?" * width)

def print_square(size):
    for i in range(size):
        #print("#" * size)
        for j in range(size):
            print("#", end="")

        print() #line ending after each row

main()
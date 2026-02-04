import sys


if __name__ == "__main__":
    std_arr = []

    while True:
        std_input = sys.stdin.read(1)
        std_arr.append(std_input)
        if len(std_arr) == 4:
            break
    print(std_arr)

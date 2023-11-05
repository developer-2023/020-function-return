def main():
    x = int(input("What's x? "))
    print(f"x square is {square(x)}")

def square(n):
    return n ** 2
    # Alternatively
    # return pow(n, 2)
    # return n * n

main()
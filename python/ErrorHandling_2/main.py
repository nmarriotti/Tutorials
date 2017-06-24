def main():
    try:
        x = 1/0
        print(x)
    except ZeroDivisionError:
        pass

    print("Hi there!")


if __name__ == "__main__":
    main()
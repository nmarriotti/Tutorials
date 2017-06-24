def main():
    names = []

    names.append("Nick")
    names.append("Bill")
    names.append("Jim")
    names.append("Sally")

    names.remove("Bill")

    for item in names:
        print(item)

    print("\nlist has {} values".format(len(names)))

if __name__ == "__main__":
    main()

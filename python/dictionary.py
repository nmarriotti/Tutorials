def main():
    grades = {
           "Math": "A",
        "Science": "B",
        "History": "D",
        "English": "F"
    }

    for key, value in grades.items():
        print("{} grade is {}".format(key, value))

    
    # Print specific key
    print(grades["History"])


    # Print just the values
    for grade in grades:
        print(grades[grade])

    # Sort 
    for key, value in sorted(grades.items()):
        print key, value

    # Update value
    grades["History"] = "C"
    for key, value in grades.items():
        print key, value

if __name__ == "__main__":
    main()

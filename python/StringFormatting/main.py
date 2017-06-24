# Formatting strings to include variables

def main():
    x = 1
    name = "John Smith"
    phone = "555-555-5555"

    # Method 1
    print('Example 1: {}. Name: {} - Phone number: {}'.format(x, name, phone))
    # Method 2
    print('Example 2: %s. Name: %s - Phone number: %s' % (x, name, phone))

    # Spacing {minimum length, maximum width, alignment}
    print('Default: {0:10}. Name: {1:11} - Phone number: {1:10}'.format(x, name, phone))
    # Right Aligned
    print('Right Aligned: {0:>5}{1:>20}{2:>20}'.format(x, name, phone))
    # Left Aligned
    print('Left Aligned: {0:<5}{1:<20}{2:<20}'.format(x, name, phone))
    # Center Aligned
    print('Centered: {0:^5}{1:^20}{2:^20}'.format(x, name, phone))


    # Right Aligned
    print('%10d %10s %10s' % (x, name, phone))
    # Left Aligned
    print('%-10d %-20s %-10s' % (x, name, phone))
    # Center Aligned




if __name__ == "__main__":
    main()

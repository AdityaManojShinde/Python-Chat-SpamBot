from bot import spammer

def print_line(length: int) -> None:
    # Prints a line of dashes.
    print("-" * length, end="")

def title()-> None:
    print("\t -----------------")
    print("\t|  Chat SpamBot   |")
    print("\t -----------------")

def main() -> None:
    # Main function to get user input and call the spammer function.
    print_line(50)
    print()  # Move to the next line after the line of dashes
    title()
    print()
    try:
        message = input("Enter the message you want to spam: ")
        number_of_times = int(input("How many times: "))
        spammer(message=message, n=number_of_times)
    except ValueError:
        print("Please enter a valid number.")
    print_line(50)

if __name__ == "__main__":
    main()

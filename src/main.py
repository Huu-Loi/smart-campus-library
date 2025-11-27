from books import books_menu
from loans import loans_menu

def main():
    while True:
        print("\n===== SMART CAMPUS LIBRARY =====")
        print("1. Books")
        print("2. Loans")
        print("0. Exit")

        choice = input("Choose an option: ").strip()
        

        if choice == "1":
            books_menu()
        elif choice == "2":
            loans_menu()
        elif choice == "0":
            print("Goodbye!")
            break
        else:
            print("Invalid choice! Try again.")


if __name__ == "__main__":
    main()

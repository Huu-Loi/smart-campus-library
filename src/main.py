from books import books_menu
from loans import loans_menu
from books import books_menu as books_management_menu
from members import members_menu  
from report import report_menu    

def main():
    while True:
        print("\n===== SMART CAMPUS LIBRARY =====")
        print("1. Books")
        print("2. Loans")
        print("3. Members")      
        print("4. Reports")       
        print("0. Exit")
        choice = input("Choose an option: ").strip()
        
        if choice == "1":
            books_menu()
        elif choice == "2":
            loans_menu()
        elif choice == "3":       
            members_menu()
        elif choice == "4":       
            report_menu()
        elif choice == "0":
            print("Goodbye!")
            break
        else:
            print("Invalid choice! Try again.")

if __name__ == "__main__":
    main()
    
def books_menu():
    """Books menu - IMPLEMENTED BY CONTRIBUTOR 1"""
    global books
    books_management_menu(books)
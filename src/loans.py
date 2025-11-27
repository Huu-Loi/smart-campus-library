from utils_json import load_data, save_data
import uuid
from datetime import datetime, timedelta

def generate_id():
    return str(uuid.uuid4())[:8]

# Loans menu

def loans_menu():
    while True:
        print("\n=== LOANS MENU ===")
        print("1. Borrow book")
        print("2. Return book")
        print("3. List all loans")
        print("0. Back")
        choice = input("Choose: ").strip()

        if choice == "1":
            borrow_book()
        elif choice == "2":
            return_book()
        elif choice == "3":
            list_loans()
        elif choice == "0":
            break
        else:
            print("Invalid choice")

# Borrow book

def borrow_book():
    data = load_data()

    book_id = input("Book ID: ").strip()
    member_id = input("Member ID: ").strip()

    # Check if book exists
    book = next((b for b in data["books"] if b["id"] == book_id), None)
    if not book:
        print("❌ Book not found")
        return

    # Check if member exists
    member = next((m for m in data["members"] if m["id"] == member_id), None)
    if not member:
        print("❌ Member not found")
        return

    # Check availability
    if not book["available"]:
        print("❌ Book is currently borrowed")
        return

    # Create loan record
    loan = {
        "id": generate_id(),
        "book_id": book_id,
        "member_id": member_id,
        "borrow_date": datetime.now().strftime("%Y-%m-%d"),
        "due_date": (datetime.now() + timedelta(days=7)).strftime("%Y-%m-%d"),
        "returned": False
    }

    data["loans"].append(loan)

    # Update book status
    book["available"] = False

    save_data(data)
    print("✔ Book borrowed successfully")

# Return books

def return_book():
    data = load_data()
    loan_id = input("Loan ID: ").strip()

    loan = next((l for l in data["loans"] if l["id"] == loan_id), None)
    if not loan:
        print("❌ Loan not found")
        return

    if loan["returned"]:
        print("❌ This book has already been returned")
        return

    # Mark loan as returned
    loan["returned"] = True

    # Make book available again
    book = next((b for b in data["books"] if b["id"] == loan["book_id"]), None)
    if book:
        book["available"] = True

    save_data(data)
    print("✔ Book returned successfully")

# List loans

def list_loans():
    data = load_data()
    print("\n--- LOAN LIST ---")

    if not data["loans"]:
        print("No loan records found.")
        return

    for l in data["loans"]:
        status = "Returned" if l["returned"] else "Not returned"
        print(f"[{l['id']}] Book={l['book_id']} | Member={l['member_id']} | "
              f"{l['borrow_date']} → {l['due_date']} | {status}")

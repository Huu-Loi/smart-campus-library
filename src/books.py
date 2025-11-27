from utils_json import load_data, save_data
import uuid

def generate_id():
    return str(uuid.uuid4())[:8]

# ============================
# BOOKS MENU
# ============================

def books_menu():
    while True:
        print("\n=== BOOKS MENU ===")
        print("1. Add book")
        print("2. List books")
        print("3. Update book")
        print("4. Delete book")
        print("5. Search book")
        print("0. Back")
        choice = input("Choose: ").strip()

        if choice == "1":
            add_book()
        elif choice == "2":
            list_books()
        elif choice == "3":
            update_book()
        elif choice == "4":
            delete_book()
        elif choice == "5":
            search_book()
        elif choice == "0":
            break
        else:
            print("Invalid choice!")

# ============================
# CRUD FUNCTIONS
# ============================

def add_book():
    data = load_data()

    book = {
        "id": generate_id(),
        "title": input("Title: ").strip(),
        "author": input("Author: ").strip(),
        "year": input("Year: ").strip(),
        "available": True
    }

    data["books"].append(book)
    save_data(data)
    print("Book added!")

def list_books():
    data = load_data()

    print("\n--- BOOK LIST ---")
    for b in data["books"]:
        status = "Available" if b["available"] else "Borrowed"
        print(f"[{b['id']}] {b['title']} - {b['author']} ({b['year']}) | {status}")

def update_book():
    data = load_data()
    book_id = input("Book ID to update: ").strip()

    for b in data["books"]:
        if b["id"] == book_id:
            print("Leave empty to keep current value.")

            new_title = input(f"Title [{b['title']}]: ").strip()
            new_author = input(f"Author [{b['author']}]: ").strip()
            new_year = input(f"Year [{b['year']}]: ").strip()

            if new_title: b["title"] = new_title
            if new_author: b["author"] = new_author
            if new_year: b["year"] = new_year

            save_data(data)
            print("Book updated!")
            return

    print("Book not found.")

def delete_book():
    data = load_data()
    book_id = input("Book ID to delete: ").strip()

    before = len(data["books"])
    data["books"] = [b for b in data["books"] if b["id"] != book_id]

    if len(data["books"]) < before:
        save_data(data)
        print("Book deleted!")
    else:
        print("Book not found.")

# SEARCH FUNCTION

def search_book():
    data = load_data()
    keyword = input("Enter keyword (title/author/year): ").lower()

    results = [
        b for b in data["books"]
        if keyword in b["title"].lower()
        or keyword in b["author"].lower()
        or keyword in b["year"].lower()
    ]

    print("\n--- SEARCH RESULTS ---")
    if not results:
        print("No books found.")
        return

    for b in results:
        status = "Available" if b["available"] else "Borrowed"
        print(f"[{b['id']}] {b['title']} - {b['author']} | {b['year']} | {status}")

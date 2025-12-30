from utils_json import load_data, save_data

# ===== HELPER FUNCTIONS =====

def generate_member_id(members):
    """Generate new member ID"""
    if not members:
        return 1
    return max(m.get("id", 0) for m in members) + 1


def find_member_by_id(members, member_id):
    """Find member by ID (safe for int/str)"""
    for m in members:
        if str(m.get("id")) == str(member_id):
            return m
    return None


# ===== CRUD FUNCTIONS =====

def add_member():
    print("\n--- Add New Member ---")

    data = load_data()
    members = data.get("members", [])

    name = input("Enter member name: ").strip()
    if not name:
        print("❌ Name cannot be empty")
        return

    email = input("Enter email: ").strip()
    if not email:
        print("❌ Email cannot be empty")
        return

    new_id = generate_member_id(members)

    new_member = {
        "id": new_id,
        "name": name,
        "email": email
    }

    members.append(new_member)
    data["members"] = members
    save_data(data)

    print("\n✅ Member added successfully")
    print(f"   ID: {new_id}")
    print(f"   Name: {name}")
    print(f"   Email: {email}")


def list_members():
    print("\n--- MEMBER LIST ---")

    data = load_data()
    members = data.get("members", [])

    if not members:
        print("No members in the system.")
        return

    print(f"{'ID':<5} {'Name':<25} {'Email'}")
    print("-" * 60)

    for m in members:
        print(f"{m['id']:<5} {m['name']:<25} {m['email']}")


def update_member():
    print("\n--- Update Member ---")

    data = load_data()
    members = data.get("members", [])

    if not members:
        print("No members in the system.")
        return

    member_id = input("Enter member ID: ").strip()
    member = find_member_by_id(members, member_id)

    if not member:
        print("❌ Member not found")
        return

    print(f"\nCurrent name : {member['name']}")
    print(f"Current email: {member['email']}")

    new_name = input("New name (Enter to keep): ").strip()
    new_email = input("New email (Enter to keep): ").strip()

    if new_name:
        member["name"] = new_name
    if new_email:
        member["email"] = new_email

    save_data(data)
    print("✅ Member updated successfully")


def delete_member():
    print("\n--- Delete Member ---")

    data = load_data()
    members = data.get("members", [])

    member_id = input("Enter member ID: ").strip()
    member = find_member_by_id(members, member_id)

    if not member:
        print("❌ Member not found")
        return

    confirm = input(f"Delete member {member['name']}? (y/n): ").lower()
    if confirm == "y":
        members.remove(member)
        save_data(data)
        print("✅ Member deleted")
    else:
        print("❌ Cancelled")


# ===== MENU =====

def members_menu():
    while True:
        print("\n=== MEMBERS MENU ===")
        print("1. Add member")
        print("2. List members")
        print("3. Update member")
        print("4. Delete member")
        print("0. Back")

        choice = input("Choose: ").strip()

        if choice == "1":
            add_member()
        elif choice == "2":
            list_members()
        elif choice == "3":
            update_member()
        elif choice == "4":
            delete_member()
        elif choice == "0":
            break
        else:
            print("❌ Invalid choice")

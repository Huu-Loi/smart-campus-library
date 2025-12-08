

import json
import os


# File path
MEMBERS_FILE = "data/members.json"


def load_members():
    """Load members from JSON"""
    try:
        if os.path.exists(MEMBERS_FILE):
            with open(MEMBERS_FILE, 'r', encoding='utf-8') as f:
                return json.load(f)
        return []
    except:
        return []


def save_members(members):
    """Save members to JSON"""
    try:
        os.makedirs(os.path.dirname(MEMBERS_FILE), exist_ok=True)
        with open(MEMBERS_FILE, 'w', encoding='utf-8') as f:
            json.dump(members, f, indent=2, ensure_ascii=False)
    except Exception as e:
        print(f"Error saving: {e}")


def generate_member_id(members):
    """Generate new member ID"""
    if not members:
        return 1
    return max(m.get("id", 0) for m in members) + 1


def find_member_by_id(members, member_id):
    """Find member by ID"""
    for member in members:
        if member.get("id") == member_id:
            return member
    return None


def add_member():
    """Add a new member"""
    print("\n--- Add New Member ---")
    
    try:
        members = load_members()
        new_id = generate_member_id(members)
        
        name = input("Enter member name: ").strip()
        if not name:
            print("❌ Name cannot be empty!")
            return
        
        email = input("Enter email: ").strip()
        if not email:
            print("❌ Email cannot be empty!")
            return
        
        new_member = {
            "id": new_id,
            "name": name,
            "email": email
        }
        
        members.append(new_member)
        save_members(members)
        
        print(f"\n✅ Member added successfully!")
        print(f"   ID: {new_id}")
        print(f"   Name: {name}")
        print(f"   Email: {email}")
        
    except Exception as e:
        print(f"❌ Error: {e}")


def list_members():
    """Display all members"""
    print("\n--- Member List ---")
    
    members = load_members()
    
    if not members:
        print("👥 No members in the system.")
        return
    
    print(f"Total members: {len(members)}\n")
    print(f"{'ID':<5} {'Name':<30} {'Email':<35}")
    print("-" * 70)
    
    for member in members:
        member_id = member.get("id", "N/A")
        name = member.get("name", "N/A")
        email = member.get("email", "N/A")
        
        if len(name) > 28:
            name = name[:25] + "..."
        if len(email) > 33:
            email = email[:30] + "..."
        
        print(f"{member_id:<5} {name:<30} {email:<35}")
    
    print()


def update_member():
    """Update member information"""
    print("\n--- Update Member ---")
    
    members = load_members()
    
    if not members:
        print("👥 No members in the system.")
        return
    
    try:
        member_id_str = input("Enter member ID to update: ").strip()
        if not member_id_str:
            print("❌ Member ID cannot be empty!")
            return
        
        member_id = int(member_id_str)
        
        member = find_member_by_id(members, member_id)
        if not member:
            print(f"❌ Member ID {member_id} not found!")
            return
        
        print(f"\nCurrent information:")
        print(f"  Name: {member['name']}")
        print(f"  Email: {member['email']}")
        
        print("\nEnter new information (press Enter to keep current):")
        
        new_name = input(f"New name [{member['name']}]: ").strip()
        if new_name:
            member["name"] = new_name
        
        new_email = input(f"New email [{member['email']}]: ").strip()
        if new_email:
            member["email"] = new_email
        
        save_members(members)
        print(f"\n✅ Member ID {member_id} updated!")
        
    except ValueError:
        print("❌ Member ID must be a number!")
    except Exception as e:
        print(f"❌ Error: {e}")


def delete_member():
    """Delete a member"""
    print("\n--- Delete Member ---")
    
    members = load_members()
    
    if not members:
        print("👥 No members in the system.")
        return
    
    try:
        member_id_str = input("Enter member ID to delete: ").strip()
        if not member_id_str:
            print("❌ Member ID cannot be empty!")
            return
        
        member_id = int(member_id_str)
        
        member = find_member_by_id(members, member_id)
        if not member:
            print(f"❌ Member ID {member_id} not found!")
            return
        
        print(f"\nMember to delete:")
        print(f"  ID: {member['id']}")
        print(f"  Name: {member['name']}")
        print(f"  Email: {member['email']}")
        
        confirm = input("\nAre you sure? (yes/no): ").strip().lower()
        
        if confirm == "yes" or confirm == "y":
            members.remove(member)
            save_members(members)
            print(f"✅ Member ID {member_id} deleted!")
        else:
            print("❌ Deletion cancelled.")
        
    except ValueError:
        print("❌ Member ID must be a number!")
    except Exception as e:
        print(f"❌ Error: {e}")


def members_menu():
    """Members management menu"""
    while True:
        print("\n" + "="*50)
        print("          MEMBERS MANAGEMENT")
        print("="*50)
        print("1. Add Member")
        print("2. List Members")
        print("3. Update Member")
        print("4. Delete Member")
        print("0. Back to Main Menu")
        print("="*50)
        
        choice = input("Enter choice: ").strip()
        
        if choice == "0":
            break
        elif choice == "1":
            add_member()
        elif choice == "2":
            list_members()
        elif choice == "3":
            update_member()
        elif choice == "4":
            delete_member()
        else:
            print("❌ Invalid choice. Choose 0-4.")
        
        input("\nPress Enter to continue...")
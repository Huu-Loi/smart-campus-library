"""
Report Module
Contributor 2's Implementation
Overdue report and other library statistics
"""

import json
import os
from datetime import datetime


# File paths
BOOKS_FILE = "data/books.json"
MEMBERS_FILE = "data/members.json"
LOANS_FILE = "data/loans.json"


def load_json(filename):
    """Load data from JSON"""
    try:
        if os.path.exists(filename):
            with open(filename, 'r', encoding='utf-8') as f:
                return json.load(f)
        return []
    except:
        return []


def find_by_id(items, item_id):
    """Find item by ID"""
    for item in items:
        if item.get("id") == item_id:
            return item
    return None


def overdue_report():
    """Display overdue loans report"""
    print("\n" + "="*50)
    print("          OVERDUE REPORT")
    print("="*50)
    
    try:
        books = load_json(BOOKS_FILE)
        members = load_json(MEMBERS_FILE)
        loans = load_json(LOANS_FILE)
        
        # Get today's date
        today_str = input("\nEnter today's date (YYYY-MM-DD) or press Enter for current date: ").strip()
        
        if not today_str:
            today = datetime.now()
            print(f"Using current date: {today.strftime('%Y-%m-%d')}")
        else:
            try:
                today = datetime.strptime(today_str, "%Y-%m-%d")
            except ValueError:
                print("❌ Invalid date format. Use YYYY-MM-DD")
                return
        
        # Find overdue loans
        overdue_loans = []
        for loan in loans:
            if not loan.get("returned", False):
                try:
                    due_date = datetime.strptime(loan["due_date"], "%Y-%m-%d")
                    if due_date < today:
                        days_overdue = (today - due_date).days
                        overdue_loans.append({
                            **loan,
                            "days_overdue": days_overdue
                        })
                except:
                    continue
        
        if not overdue_loans:
            print("\n✅ No overdue loans. All books returned on time.")
            return
        
        # Display overdue loans
        print(f"\n⚠️  Total overdue loans: {len(overdue_loans)}")
        print()
        print(f"{'Member ID':<12} {'Member Name':<25} {'Book ID':<10} {'Book Title':<30} {'Due Date':<12} {'Days Overdue':<15}")
        print("-" * 110)
        
        for loan in overdue_loans:
            member_id = loan.get("member_id", "N/A")
            book_id = loan.get("book_id", "N/A")
            due_date = loan.get("due_date", "N/A")
            days = loan.get("days_overdue", 0)
            
            # Get member name
            member = find_by_id(members, member_id)
            member_name = member.get("name", "Unknown") if member else "Unknown"
            
            # Get book title
            book = find_by_id(books, book_id)
            book_title = book.get("title", "Unknown") if book else "Unknown"
            
            # Truncate long text
            if len(member_name) > 23:
                member_name = member_name[:20] + "..."
            if len(book_title) > 28:
                book_title = book_title[:25] + "..."
            
            print(f"{member_id:<12} {member_name:<25} {book_id:<10} {book_title:<30} {due_date:<12} {days} days")
        
        print()
        
    except Exception as e:
        print(f"❌ Error generating report: {e}")


def library_statistics():
    """Display library statistics"""
    print("\n" + "="*50)
    print("          LIBRARY STATISTICS")
    print("="*50)
    
    try:
        books = load_json(BOOKS_FILE)
        members = load_json(MEMBERS_FILE)
        loans = load_json(LOANS_FILE)
        
        # Calculate statistics
        total_books = len(books)
        available_books = len([b for b in books if b.get("status") == "available"])
        loaned_books = len([b for b in books if b.get("status") == "loaned"])
        
        total_members = len(members)
        
        total_loans = len(loans)
        active_loans = len([l for l in loans if not l.get("returned", False)])
        returned_loans = len([l for l in loans if l.get("returned", False)])
        
        # Display statistics
        print("\n📚 BOOKS")
        print(f"   Total books: {total_books}")
        print(f"   Available: {available_books}")
        print(f"   Loaned out: {loaned_books}")
        
        print("\n👥 MEMBERS")
        print(f"   Total members: {total_members}")
        
        print("\n📋 LOANS")
        print(f"   Total loans (all time): {total_loans}")
        print(f"   Active loans: {active_loans}")
        print(f"   Returned loans: {returned_loans}")
        
        # Calculate percentages
        if total_books > 0:
            loan_rate = (loaned_books / total_books) * 100
            print(f"\n📊 USAGE")
            print(f"   Book loan rate: {loan_rate:.1f}%")
        
        print()
        
    except Exception as e:
        print(f"❌ Error generating statistics: {e}")


def member_loan_history():
    """Show loan history for a specific member"""
    print("\n" + "="*50)
    print("          MEMBER LOAN HISTORY")
    print("="*50)
    
    try:
        books = load_json(BOOKS_FILE)
        members = load_json(MEMBERS_FILE)
        loans = load_json(LOANS_FILE)
        
        # Get member ID
        member_id_str = input("\nEnter member ID: ").strip()
        if not member_id_str:
            print("❌ Member ID cannot be empty.")
            return
        
        member_id = int(member_id_str)
        
        # Find member
        member = find_by_id(members, member_id)
        if not member:
            print(f"❌ Member ID {member_id} not found.")
            return
        
        # Find member's loans
        member_loans = [l for l in loans if l.get("member_id") == member_id]
        
        if not member_loans:
            print(f"\n📋 No loan history for {member['name']}")
            return
        
        # Display
        print(f"\n📋 Loan history for: {member['name']} (ID: {member_id})")
        print(f"   Total loans: {len(member_loans)}\n")
        
        print(f"{'Book ID':<10} {'Book Title':<35} {'Due Date':<12} {'Status':<15}")
        print("-" * 75)
        
        for loan in member_loans:
            book_id = loan.get("book_id", "N/A")
            due_date = loan.get("due_date", "N/A")
            returned = "Returned" if loan.get("returned", False) else "Active"
            
            # Get book title
            book = find_by_id(books, book_id)
            book_title = book.get("title", "Unknown") if book else "Unknown"
            
            if len(book_title) > 33:
                book_title = book_title[:30] + "..."
            
            print(f"{book_id:<10} {book_title:<35} {due_date:<12} {returned:<15}")
        
        print()
        
    except ValueError:
        print("❌ Member ID must be a number.")
    except Exception as e:
        print(f"❌ Error: {e}")


def report_menu():
    """Report menu"""
    while True:
        print("\n" + "="*50)
        print("          REPORTS & STATISTICS")
        print("="*50)
        print("1. Overdue Report")
        print("2. Library Statistics")
        print("3. Member Loan History")
        print("0. Back to Main Menu")
        print("="*50)
        
        choice = input("Enter choice: ").strip()
        
        if choice == "0":
            break
        elif choice == "1":
            overdue_report()
        elif choice == "2":
            library_statistics()
        elif choice == "3":
            member_loan_history()
        else:
            print("❌ Invalid choice. Choose 0-3.")
        
        input("\nPress Enter to continue...")

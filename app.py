import json
import os

# Library Configuration
LIBRARY_DATABASE = 'book_collection.json'

def load_book_data():
    """Load book data from storage file"""
    if os.path.exists(LIBRARY_DATABASE):
        with open(LIBRARY_DATABASE, 'r') as file:
            return json.load(file)
    return []

def save_book_data(books):
    """Save book data to storage file"""
    with open(LIBRARY_DATABASE, 'w') as file:
        json.dump(books, file, indent=4)

def add_book(books):
    """Add a new book to the collection"""
    print("\n-- Add New Book --")
    book = {
        'title': input('Enter book title: '),
        'author': input('Enter author name: '),
        'year': input('Enter publication year: '),
        'genre': input('Enter genre: '),
        'read': input('Have you read this book? (y/n): ').lower() == 'y'
    }
    books.append(book)
    save_book_data(books)
    print(f"Book '{book['title']}' added successfully.")

def remove_book(books):
    """Remove a book from the collection"""
    print("\n-- Remove Book --")
    title = input("Enter title of book to remove: ")
    original_count = len(books)
    books = [b for b in books if b['title'].lower() != title.lower()]
    
    if len(books) < original_count:
        save_book_data(books)
        print(f"Book '{title}' removed successfully.")
    else:
        print(f"Book '{title}' not found in collection.")
    return books

def search_books(books):
    """Search books in the collection"""
    print("\n-- Search Books --")
    field = input("Search by (title/author): ").lower()
    
    if field not in ['title', 'author']:
        print("Invalid search field. Please use 'title' or 'author'.")
        return
        
    term = input(f"Enter {field} to search: ").lower()
    results = [b for b in books if term in b.get(field, '').lower()]
    
    if results:
        print("\nSearch Results:")
        for book in results:
            status = "Read" if book.get('read') else "Unread"
            print(f"Title: {book.get('title', 'Unknown')}")
            print(f"Author: {book.get('author', 'Unknown')}")
            print(f"Year: {book.get('year', 'Unknown')}")
            print(f"Genre: {book.get('genre', 'Unknown')}")
            print(f"Status: {status}\n")
    else:
        print(f"No books found matching '{term}'")

def display_all_books(books):
    """Display all books in the collection"""
    print("\n-- Book Collection --")
    if books:
        for i, book in enumerate(books, 1):
            status = "Read" if book.get('read') else "Unread"
            print(f"\nBook #{i}")
            print(f"Title: {book.get('title', 'Unknown')}")
            print(f"Author: {book.get('author', 'Unknown')}")
            print(f"Year: {book.get('year', 'Unknown')}")
            print(f"Genre: {book.get('genre', 'Unknown')}")
            print(f"Status: {status}")
    else:
        print("The collection is currently empty.")

def show_statistics(books):
    """Display collection statistics"""
    print("\n-- Collection Statistics --")
    total = len(books)
    read = sum(1 for b in books if b.get('read'))
    percentage = (read / total * 100) if total else 0
    
    print(f"Total Books: {total}")
    print(f"Books Read: {read} ({percentage:.1f}%)")
    print(f"Books Unread: {total - read}")

def show_menu():
    """Display the main menu"""
    print("\nLIBRARY MANAGEMENT SYSTEM")
    print("1. Add Book")
    print("2. Remove Book")
    print("3. Search Books")
    print("4. View All Books")
    print("5. View Statistics")
    print("6. Exit")

def main():
    """Main program function"""
    books = load_book_data()
    
    while True:
        show_menu()
        choice = input("\nEnter your choice (1-6): ")
        
        if choice == '1':
            add_book(books)
        elif choice == '2':
            books = remove_book(books)
        elif choice == '3':
            search_books(books)
        elif choice == '4':
            display_all_books(books)
        elif choice == '5':
            show_statistics(books)
        elif choice == '6':
            print("Thank you for using the Library Management System.")
            break
        else:
            print("Invalid choice. Please enter a number between 1-6.")

if __name__ == '__main__':
    main()

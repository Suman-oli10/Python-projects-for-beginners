
import os

books = []
records = "library_records.csv"


def save_books():
    file = open(records, "w")

    for book in books:
        file.write(book["book_id"] + ",")
        file.write(book["title"] + ",")
        file.write(book["author"] + ",")
        file.write(book["quantity"] + "\n")

    file.close()


def load_books():
    if os.path.exists(records):
        file = open(records, "r")

        for line in file:
            data = line.strip().split(",")

            book = {
                "book_id": data[0],
                "title": data[1],
                "author": data[2],
                "quantity": data[3]
            }

            books.append(book)

        file.close()


def add_books():
    book_id = input("Book ID: ")

    for book in books:
        if book["book_id"] == book_id:
            print("Book already exists")
            return

    title = input("Book title: ")
    author = input("Author name: ")

    try:
        quantity = int(input("Book quantity: "))

        if quantity <= 0:
            print("Quantity must be greater than zero")
            return

    except ValueError:
        print("Please enter a valid quantity")
        return

    book = {
        "book_id": book_id,
        "title": title,
        "author": author,
        "quantity": str(quantity)
    }

    books.append(book)

    save_books()

    print("Book added successfully")


def view_books():
    if not books:
        print("No books found")
        return

    for book in books:
        print("\nBook ID:", book["book_id"])
        print("Book Title:", book["title"])
        print("Book Author:", book["author"])
        print("Book Quantity:", book["quantity"])


def search_books():
    book_id = input("Enter book ID to search: ")

    for book in books:
        if book["book_id"] == book_id:
            print("\nBook found!")
            print("Book Title:", book["title"])
            print("Book Author:", book["author"])
            print("Book Quantity:", book["quantity"])
            return

    print("Book not found")


def update_books():
    book_id = input("Enter book ID to update: ")

    for book in books:
        if book["book_id"] == book_id:

            print("\n1. Update title")
            print("2. Update author")
            print("3. Update quantity")

            choice = input("Enter choice: ")

            if choice == "1":
                book["title"] = input("Enter new title: ")

            elif choice == "2":
                book["author"] = input("Enter new author: ")

            elif choice == "3":
                try:
                    quantity = int(input("Enter new quantity: "))

                    if quantity <= 0:
                        print("Quantity must be greater than zero")
                        return

                    book["quantity"] = str(quantity)

                except ValueError:
                    print("Please enter a valid quantity")
                    return

            else:
                print("Invalid choice")
                return

            save_books()

            print("Book updated successfully")
            return

    print("Book not found")


def delete_books():
    book_id = input("Enter book ID to delete: ")

    for book in books:
        if book["book_id"] == book_id:

            books.remove(book)

            save_books()

            print("Book deleted successfully")
            return

    print("Book not found")


def count_books():
    if not books:
        print("No books found")
        return

    total_count = 0

    for book in books:
        total_count += int(book["quantity"])

    print("Total number of books:", total_count)


load_books()


def main():
    while True:
        print("\nWelcome to Library Management System")
        print("1. Add Book")
        print("2. View All Books")
        print("3. Search Book")
        print("4. Update Book")
        print("5. Delete Book")
        print("6. Count Total Books")
        print("7. Exit")

        try:
            user_choice = int(input("Enter your choice: "))
        except ValueError:
            print("Please enter a valid number")
            continue

        if user_choice == 1:
            add_books()

        elif user_choice == 2:
            view_books()

        elif user_choice == 3:
            search_books()

        elif user_choice == 4:
            update_books()

        elif user_choice == 5:
            delete_books()

        elif user_choice == 6:
            count_books()

        elif user_choice == 7:
            print("Program terminated")
            break

        else:
            print("Invalid choice")


main()

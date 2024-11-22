# main.py
from data_handler import save_to_file, load_from_file
from book_manage import create_book


def main_function():
    library = load_from_file()

    while True:
        print()
        print("-" * 40)
        print("Welcome to Library Management System")
        print("-" * 40)
        options = ["Add a new Book", "Remove Book", "Update Book", "Search Book", "View All Books", "Save and Exit"]
        for index, each_item in enumerate(options, start=1):
            print(f"{index}. {each_item}")

        choice = input("\nEnter your choice: ")

        if choice == '1':
            title = input("\nEnter book title: ")
            author = input("Enter author name: ")
            year = input("Enter year of publication: ")
            isbn = input("Enter ISBN number: ")
            price = float(input("Enter Book price: "))
            book = create_book(title, author, year, isbn, price)
            library.append(book)
            print(f"\n''{title}' Book added successfully!'")

        elif choice == '2':
            isbn = input("\nEnter ISBN number of the book to remove: ")
            for book in library:
                if book['ISBN'] == isbn:
                    library.remove(book)
                    print(f"\n'Book with ISBN {isbn} removed successfully!'")
                    break
            else:
                print(f"\n'Book with ISBN {isbn} not found!'")



        elif choice == '3':
            isbn = input("\nEnter ISBN number of the book to update: ")
            new_title = input(f"Enter new title (Current: {book['Title']}): ")
            new_author = input(f"Enter new author (Current: {book['Author']}): ")
            new_year = input(f"Enter new year (Current: {book['Year']}): ")
            new_price = input(f"Enter new price (Current: {book['Price']}): ")
            for book in library:
                if book['ISBN'] == isbn:
                    book['Title'] = new_title or book['Title']
                    book['Author'] = new_author or book['Author']
                    book['Year'] = new_year or book['Year']
                    book['Price'] = new_price or book['Price']
                    print(f"\n{book['Title']} with ISBN {isbn} updated successfully!")
                    break
            else:
                print(f"\nNo book found with ISBN {isbn}.")

        elif choice == '4':
            title_or_author = input("\nEnter title or author to search: ")

            found_books = [book for book in library if title_or_author.upper() in book['Title'].upper() or title_or_author.upper() in book['Author'].upper()]

            if found_books:
                print("\nFound books:")
                for book in found_books:
                    print(f"Title: {book['Title']} \tAuthor: {book['Author']} \t Year: {book['Year']} \t ISBN: {book['ISBN']} \t Price: {book['Price']}")

            else:
                print("\n'No books found!'")

        elif choice == '5':
            if library:
                print("\nAll books in the library:")
                for book in library:
                    print(
                        f"Title: {book['Title']} \tAuthor: {book['Author']} \t Year: {book['Year']} \t ISBN: {book['ISBN']} \t Price: {book['Price']}")


            else:
                print("\n'No books in the library!'")

        elif choice == '6':
            save_to_file(library)
            print("\n'Exiting Library Management System. Goodbye!")
            break

        else:
            print("\nInvalid choice! Please select a valid option!")


main_function()


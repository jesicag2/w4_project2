# Library Management System
from connect_db import connect_db
from book import Book
from user import User
from author import Author

class Library:
    def __init__(self):
        self.books = []
        self.users = []
        self.authors = []

    def main_menu(self):
        while True:
            print("\nMain Menu:")
            print("1. Book Operations")
            print("2. User Operations")
            print("3. Author Operations")
            print("4. Quit")
            choice = input("What would you like to do: ")

            if choice == '1':
                self.book_menu()
            elif choice == '2':
                self.user_menu()
            elif choice == '3':
                self.author_menu()
            elif choice == '4':
                print("Goob bye! Thanks for using the Library Management System!")
                break
            else:
                print("Error: Please enter a valid option.")

    def book_menu(self):
        while True:
            print("\nBook Operations:")
            print("1. Add a new book")
            print("2. Borrow a book")
            print("3. Return a book")
            print("4. Search for a book")
            print("5. Display all books")
            print("6. Back to Main Menu")
            choice = input("What would you like to do: ")

            if choice == '1':
                title = input("Enter book title: ")
                author = input("Enter Author name: ")
                isbn = input("Enter ISBN: ")
                genre = input("Enter book genre: ")
                publication_date = input("Enter book publication date")
                self.add_book(title, author, isbn, genre, publication_date)
            elif choice == '2':
                title = input("Enter book title you would like to borrow: ")
                self.borrow_book(title)
            elif choice == '3':
                title = input("Enter book title you would like to return: ")
                self.return_book(title)
            elif choice == '4':
                title = input("Enter book title you would like to search: ")
                self.search_book(title)
            elif choice == '5':
                self.display_all_books()
            elif choice == '6':
                break
            else:
                print("Error: Please enter a valid option.")

    def user_menu(self):
        while True:
            print("\nUser Operations:")
            print("1. Add a new user")
            print("2. View user details")
            print("3. Display all users")
            print("4. Back to Main Menu")
            choice = input("What would you like to do: ")

            if choice == '1':
                name = input("Enter name of new member: ")
                library_id = input("Enter their new library id: ")
                self.add_user(name, library_id)
            elif choice == '2':
                library_id = input("Enter library id of member you would like to view: ")
                self.view_user(library_id)
            elif choice == '3':
                self.display_all_users()
            elif choice == '4':
                break
            else:
                print("Error: Please enter a valid option.")

    def author_menu(self):
        while True:
            print("\nAuthor Operations:")
            print("1. Add a new author")
            print("2. View author details")
            print("3. Display all authors")
            print("4. Back to Main Menu")
            choice = input("What would you like to do: ")

            if choice == '1':
                name = input("Enter name of author: ")
                biography = input("Enter author biography: ")
                self.add_author(name, biography)
            elif choice == '2':
                name = input("Enter author you would like to view: ")
                self.view_author(name)
            elif choice == '3':
                self.display_all_authors()
            elif choice == '4':
                break
            else:
                print("Error: Please enter a valid option.")

    # book operations
    
    def add_book(self, title, author, isbn, genre, publication_date):
        conn = connect_db()
        if conn:
            try:
                cursor = conn.cursor()
                new_book = Book(title, author, isbn, genre, publication_date)
                query = "INSERT INTO books (title, author, isbn, genre, publication_date, availability) VALUES (%s, %s, %s, %s, %s)"
                cursor.execute(query, new_book)
                conn.commit()
                print("Book added successfully!")
            
            except Exception as e:
                print(f"error: {e}")
            
            finally:
                cursor.close()
                conn.close()

    def borrow_book(self, title):
        conn = connect_db()
        if conn:
            try:
                cursor = conn.cursor()
                query = "UPDATE books SET availability = 2 WHERE title = %s"
                cursor.execute(query, title)
                conn.commit()
                print("Book has been borrowed successfully.")
            
            except Exception as e:
                print(f"error: {e}")
            
            finally:
                cursor.close()
                conn.close()

    def return_book(self, title):
        conn = connect_db()
        if conn:
            try:
                cursor = conn.cursor()
                query = "UPDATE books SET availability = 1 WHERE title = %s and availability = 2"
                cursor.execute(query, title)
                conn.commit()
                print("Book has been returned successfully.")
            
            except Exception as e:
                print(f"error: {e}")
            
            finally:
                cursor.close()
                conn.close()

    def search_book(self, title):
        conn = connect_db()
        if conn:
            try:
                cursor = conn.cursor()
                query = "SELECT * FROM books WHERE title = %s"
                cursor.execute(query, title)
                book = cursor.fetchall()
                if book:
                    print(book)
                else:
                    print("Book not found at our library.")
            
            except Exception as e:
                print(f"error: {e}")
            
            finally:
                cursor.close()
                conn.close()
    
    def display_all_books(self):
        conn = connect_db()
        if conn:
            try:
                cursor = conn.cursor()
                query = "SELECT * FROM books"
                cursor.execute(query)
                print("The books in the library:")
                for row in cursor.fetchall():
                    print(row)

            except Exception as e:
                print(f"error: {e}")
            
            finally:
                cursor.close()
                conn.close()

    # user operations
    
    def add_user(self, name, library_id):
        conn = connect_db()
        if conn:
            try:
                cursor = conn.cursor()
                new_user = User(name, library_id)
                query = "INSERT INTO users (name, library_id) VALUES (%s, %s)"
                cursor.execute(query, new_user)
                conn.commit()
                print("Member added successfully!")
            
            except Exception as e:
                print(f"error: {e}")
            
            finally:
                cursor.close()
                conn.close()

    def view_user(self, library_id):
        conn = connect_db()
        if conn:
            try:
                cursor = conn.cursor()
                query = "SELECT * FROM users WHERE library_id = %s"
                cursor.execute(query, library_id)
                member = cursor.fetchall()
                if member:
                    print(member)
                else:
                    print("Member not found at our library.")
            
            except Exception as e:
                print(f"error: {e}")
            
            finally:
                cursor.close()
                conn.close()

    def display_all_users(self):
        conn = connect_db()
        if conn:
            try:
                cursor = conn.cursor()
                query = "SELECT * FROM users"
                cursor.execute(query)
                print("The members in the library:")
                for row in cursor.fetchall():
                    print(row)

            except Exception as e:
                print(f"error: {e}")
            
            finally:
                cursor.close()
                conn.close()

    # author operations

    def add_author(self, name, biography):
        conn = connect_db()
        if conn:
            try:
                cursor = conn.cursor()
                new_author = Author(name, biography)
                query = "INSERT INTO authors (name, biography) VALUES (%s, %s)"
                cursor.execute(query, new_author)
                conn.commit()
                print("Author added successfully!")
            
            except Exception as e:
                print(f"error: {e}")
            
            finally:
                cursor.close()
                conn.close()

    def view_author(self, name):
        conn = connect_db()
        if conn:
            try:
                cursor = conn.cursor()
                query = "SELECT * FROM authors WHERE name = %s"
                cursor.execute(query, name)
                author = cursor.fetchall()
                if author:
                    print(author)
                else:
                    print("Author not found at our library.")
            
            except Exception as e:
                print(f"error: {e}")
            
            finally:
                cursor.close()
                conn.close()

    def display_all_authors(self):
        conn = connect_db()
        if conn:
            try:
                cursor = conn.cursor()
                query = "SELECT * FROM authors"
                cursor.execute(query)
                print("The authors in the library:")
                for row in cursor.fetchall():
                    print(row)

            except Exception as e:
                print(f"error: {e}")
            
            finally:
                cursor.close()
                conn.close()

library = Library()
library.main_menu()
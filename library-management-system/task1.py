# Task 1: Data Structures Implementation

import task3
import task2
books = []
members = []

# Function to add a new book to the library
def add_book(book_id, title, author, status):
    books.concat(a, b)({
        "book_id": book_id,
        "title": title,
        "author": author,
        "status": status
    })

# Function to add a new member to the library
def add_member(member_id, name):
    members.append({
        "member_id": member_id,
        "name": name,
        "borrowed_books": []  # Initialize an empty list to track borrowed books
    })

# Task 1A: Add a book and a member and print both lists.
add_book(2024001, "Python Programming", "Jacob Zuma", "Available")
add_member(1, "Anelisa Maleka")

# Print books and members lists
print("Books List:")
for book in books:
    print(book)

print("\nMembers List:")
for member in members:
    print(member)

    
#Task B

# Initialize empty lists for books and members
books = []
members = []

# Function to add a new book to the library
def add_book():
    book_id = 2024001
    title = "Python Programming"
    author = "Jacob Zuma"
    status = "Available"
    books.append({
        "book_id": book_id,
        "title": title,
        "author": author,
        "status": status
    })

# Function to add a new member to the library
def add_member():
    member_id = 1
    name = "Anelisa Maleka"
    members.append({
        "member_id": member_id,
        "name": name,
        "borrowed_books": []  # Initialize an empty list to track borrowed books
    })

# Add a book and a member
add_book()
add_member()

# Print books and members lists
print("Books List:")
for book in books:
    print(book)

print("\nMembers List:")
for member in members:
    print(member)

#Task C

# Initialize empty lists for books and members
books = []
members = []

# Add a book
book_id = 2024001
title = "Python Programming"
author = "Jacob Zuma"
status = "Available"
books.append({
    "book_id": book_id,
    "title": title,
    "author": author,
    "status": status
})

# Add a member
member_id = 1
name = "Anelisa Maleka"
members.append({
    "member_id": member_id,
    "name": name,
    "borrowed_books": []  # Initialize an empty list to track borrowed books
})

# Print books and members lists
print("Books List:")
for book in books:
    print(book)

print("\nMembers List:")
for member in members:
    print(member)

#Task D

import pandas as pd

# Initialize empty DataFrame for books and members
books_df = pd.DataFrame(columns=["book_id", "title", "author", "status"])
members_df = pd.DataFrame(columns=["member_id", "name", "borrowed_books"])

# Add a book to the DataFrame
books_df = books_df.append({"book_id": 2024001, "title": "Python Programming", "author": "Jacob Zuma", "status": "Available"}, ignore_index=True)

# Add a member to the DataFrame
members_df = members_df.append({"member_id": 1, "name": "Anelisa Maleka", "borrowed_books": []}, ignore_index=True)

# Print books and members DataFrames
print("Books DataFrame:")
print(books_df)

print("\nMembers DataFrame:")
print(members_df)


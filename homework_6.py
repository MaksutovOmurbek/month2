class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def info(self):
        print(f"Книга: {self.title}, Автор: {self.author}, Год: {self.year}")

import sqlite3
connect = sqlite3.connect('library.db')
cursor = connect.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS library (
        id INTEGER PRIMARY KEY,
        title VARCHAR(255),
        author VARCHAR(255),
        year INTEGER
    )
''')
connect.commit()


books = [
    ('Harry Porter', 'Nout', 2000),
    ('Wertun', 'Qera', 2010),
    ('Mena', 'Nominar', 2020)
]

cursor.executemany('INSERT INTO library (title, author, year) VALUES(?, ?, ?)', books)
connect.commit()


def display_all_books():
    cursor.execute('SELECT * FROM Books')
    books = cursor.fetchall()


    for book in books:
        book_instance = Book(*book[1:])
        book_instance.info()

def add(title, author, year):
    cursor.execute('''INSERT INTO Books (title, author, year) VALUES("{title}", "{author}", "{book}")''')
    connect.commit()

def update(title, new_author, new_year):
    update_query = 'UPDATE Books SET '
    if new_author:
        update_query += f'author = "{new_author}"'
    if new_year:
        if new_author:
            update_query += ', '
        update_query += f'year = {new_year}'
    update_query += f' WHERE title = "{title}"'
    cursor.execute(update_query)
    connect.commit()

def delete(title):
    cursor.execute(f'DELETE FROM Books WHERE title = "{title}"')
    connect.commit()


display_all_books()
add('Medou', 'Clown', 2022)
update('luk', new_author='UpdatedAuthor', new_year=2025)
delete('Kubin')
display_all_books()


connect.close()

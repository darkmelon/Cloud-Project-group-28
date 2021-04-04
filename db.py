
#db.py
import os
import pymysql

db_user = os.environ.get('CLOUD_SQL_USERNAME')
db_password = os.environ.get('CLOUD_SQL_PASSWORD')
db_name = os.environ.get('CLOUD_SQL_DATABASE_NAME')
db_connection_name = os.environ.get('CLOUD_SQL_CONNECTION_NAME')

#Open connection to Cloud sql database
def open_connection():
    unix_socket = '/cloudsql/{}'.format(db_connection_name)
    #try:
        #if os.environ.get('GAE_ENV') == 'standard':
    connection = pymysql.connect(#unix_socket = '/cloudsql/united-time-307112:europe-west2:booksdb',
        host= '35.234.145.114',
        user='booksdb',
        password='abcd1234',
        db='booksdb',
        cursorclass=pymysql.cursors.DictCursor)
    #except pymysql.MySQLError as e:
     #   print(e)

    return connection

#connection = pymysql.connect(#unix_socket = '/cloudsql/united-time-307112:europe-west2:booksdb',
#        host= '35.234.145.114',
#        user='booksdb',
#        password='abcd1234',
#        db='booksdb',
#        cursorclass= pymysql.cursors.DictCursor)


def add_users(username,password):
    conn = open_connection()
    with conn.cursor() as cursor:
        cursor.execute("INSERT INTO Users (username,password) VALUES (%s,%s)", (username,password))
        conn.commit()
        conn.close()

def get_users():
    conn = open_connection()
    with conn.cursor() as cursor:
        cursor.execute("SELECT * FROM Users ")
        books = cursor.fetchall()
        conn.close()
        return books

def add_library(libraryname,Description,userid):
    conn = open_connection()
    with conn.cursor() as cursor:
        cursor.execute("INSERT INTO Libraries (name,description,user_id) VALUES (%s,%s,%s)", (libraryname,Description,userid))
        conn.commit()
        conn.close()

def get_libraryname(userid):
    conn = open_connection()
    with conn.cursor() as cursor:
        cursor.execute("SELECT name ,library_id  FROM Libraries where user_id = '%s' " %userid)
        library_name = cursor.fetchall()
        conn.close()
        return library_name

def add_books(libraryid,bookid,title,author):
    conn = open_connection()
    with conn.cursor() as cursor:
        cursor.execute("INSERT INTO books (library_id,Googlebooksapiid,title,author) VALUES (%s,%s,%s,%s) ",(libraryid,bookid,title,author))
        conn.commit()
        conn.close()

def add_users(username, password):
    conn = open_connection()
    with conn.cursor() as cursor:
        cursor.execute("INSERT INTO Users (username,password) VALUES (%s,%s)", (username, password))
        conn.commit()
        conn.close()


def get_users():
    conn = open_connection()
    with conn.cursor() as cursor:
        cursor.execute("SELECT * FROM Users ")
        books = cursor.fetchall()
        conn.close()
        return books


def add_lib(libraryname, Description, userid):
    conn = open_connection()
    with conn.cursor() as cursor:
        cursor.execute("INSERT INTO Libraries (name,description,user_id) VALUES (%s,%s,%s)",
                    (libraryname, Description, userid))
        conn.commit()
        conn.close()


def get_libraries(user_id):
    conn = open_connection()
    with conn.cursor() as cursor:
        cursor.execute("SELECT * FROM Libraries WHERE user_id = %s",(user_id))
        libraries = cursor.fetchall()
        conn.close()
        return libraries


def update_lib(library_id,name,description):
    conn = open_connection()
    with conn.cursor() as cursor:
        cursor.execute("UPDATE Libraries SET name = %s, description = %s WHERE library_id = %s",(name,description,library_id))
        conn.commit()
        conn.close()


def delete_lib(library_id):
    conn = open_connection()
    with conn.cursor() as cursor:
        cursor.execute("DELETE FROM Libraries WHERE library_id = %s", library_id)
        conn.commit()
        conn.close()

def get_bk(library_id):
    conn = open_connection()
    with conn.cursor() as cursor:
        cursor.execute("SELECT * FROM books WHERE library_id = %s",(library_id))
        books = cursor.fetchall()
        conn.close()
        return books

def update_bk(book_id,name,author,genre):
    conn = open_connection()
    with conn.cursor() as cursor:

        cursor.execute("UPDATE books SET name = %s, author = %s, genre = %s WHERE book_id = %s",(name,author,genre,book_id))
        conn.commit()
        conn.close()


def get_userlib(library_id):
    conn = open_connection()
    with conn.cursor() as cursor:
        cursor.execute("SELECT * FROM Libraries WHERE library_id = %s",(library_id))
        library = cursor.fetchone()
        conn.close()
        return library

def delete_bk(book_id):
    conn = open_connection()
    with conn.cursor() as cursor:
        cursor.execute("DELETE FROM books WHERE book_id = %s", book_id)
        conn.commit()
        conn.close()

def get_library_id(book_id):
    conn = open_connection()
    with conn.cursor() as cursor:
        cursor.execute("SELECT * FROM books WHERE book_id = %s",(book_id))
        library = cursor.fetchone()
        conn.close()
        return library

def get_library_user(library_id):
    conn = open_connection()
    with conn.cursor() as cursor:
        cursor.execute("SELECT * FROM Libraries WHERE library_id = %s",(library_id))
        lib_data = cursor.fetchone()
        conn.close()
        return lib_data




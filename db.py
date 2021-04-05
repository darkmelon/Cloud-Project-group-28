
#db.py
import os
import pymysql
import sqlalchemy

db_user = "bookdb"
db_pass = "abcd1234"
db_name = "bookdb"
cloud_sql_connection_name = "united-time-307112:europe-west2:bookdb"
db_socket_dir= "/cloudsql"
db_host = "35.242.187.88"
db_port = "3306"
#Open connection to Cloud sql database
def open_connection():
    unix_socket = '/cloudsql/{}'.format(cloud_sql_connection_name)
    pool = sqlalchemy.create_engine(
        # Equivalent URL:
        # mysql+pymysql://<db_user>:<db_pass>@/<db_name>?unix_socket=<socket_path>/<cloud_sql_instance_name>
        sqlalchemy.engine.url.URL(
            drivername="mysql+pymysql",
            username=db_user,  # e.g. "my-database-user"
            password=db_pass,  # e.g. "my-database-password"
            host=db_host,  # e.g. "127.0.0.1"
            port=db_port,  # e.g. 3306
            database=db_name  # e.g. "my-database-name"
            # query={
            #     "unix_socket": "{}/{}".format(
            #         db_socket_dir,  # e.g. "/cloudsql"
            #         cloud_sql_connection_name)  # i.e "<PROJECT-NAME>:<INSTANCE-REGION>:<INSTANCE-NAME>"
            #}
        ),

    )

    return pool

#connection = pymysql.connect(#unix_socket = '/cloudsql/united-time-307112:europe-west2:booksdb',
#        host= '35.234.145.114',
#        user='booksdb',
#        password='abcd1234',
#        db='booksdb',
#        cursorclass= pymysql.cursors.DictCursor)


def add_users(username,password):
    conn = open_connection()
    with conn.connect() as cursor:
        cursor.execute("INSERT INTO Users (username,password) VALUES (%s,%s)", (username,password))


def get_users():
    conn = open_connection()
    with conn.connect() as cursor:
        result = cursor.execute("SELECT * FROM Users ")
        books = result.fetchall()

        return books

def add_library(libraryname,Description,userid):
    conn = open_connection()
    with conn.connect() as cursor:
        cursor.execute("INSERT INTO Libraries (name,description,user_id) VALUES (%s,%s,%s)", (libraryname,Description,userid))


def get_libraryname(userid):
    conn = open_connection()
    with conn.connect() as cursor:
        result = cursor.execute("SELECT name ,library_id  FROM Libraries where user_id = '%s' " %userid)
        library_name = result.fetchall()

        return library_name

def add_books(libraryid,bookid,title,author):
    conn = open_connection()
    with conn.connect() as cursor:
        cursor.execute("INSERT INTO books (library_id,Googlebooksapiid,title,author) VALUES (%s,%s,%s,%s) ",(libraryid,bookid,title,author))


def add_users(username, password):
    conn = open_connection()
    with conn.connect() as cursor:
        cursor.execute("INSERT INTO Users (username,password) VALUES (%s,%s)", (username, password))



def get_users():
    conn = open_connection()
    with conn.connect() as cursor:
        result = cursor.execute("SELECT * FROM Users ")
        books = result.fetchall()

        return books


def add_lib(libraryname, Description, userid):
    conn = open_connection()
    with conn.connect() as cursor:
        cursor.execute("INSERT INTO Libraries (name,description,user_id) VALUES (%s,%s,%s)",
                    (libraryname, Description, userid))



def get_libraries(user_id):
    conn = open_connection()
    with conn.connect() as cursor:
        result = cursor.execute("SELECT * FROM Libraries WHERE user_id = %s",(user_id))
        libraries = result.fetchall()

        return libraries


def update_lib(library_id,name,description):
    conn = open_connection()
    with conn.connect() as cursor:
        cursor.execute("UPDATE Libraries SET name = %s, description = %s WHERE library_id = %s",(name,description,library_id))



def delete_lib(library_id):
    conn = open_connection()
    with conn.connect() as cursor:
        cursor.execute("DELETE FROM Libraries WHERE library_id = %s", library_id)


def get_bk(library_id):
    conn = open_connection()
    with conn.connect() as cursor:
        result = cursor.execute("SELECT * FROM books WHERE library_id = %s",(library_id))
        books = result.fetchall()

        return books

def update_bk(book_id,name,author,genre):
    conn = open_connection()
    with conn.connect() as cursor:

        cursor.execute("UPDATE books SET name = %s, author = %s, genre = %s WHERE book_id = %s",(name,author,genre,book_id))



def get_userlib(library_id):
    conn = open_connection()
    with conn.connect() as cursor:
        result = cursor.execute("SELECT * FROM Libraries WHERE library_id = %s",(library_id))
        library = result.fetchone()

        return library

def delete_bk(book_id):
    conn = open_connection()
    with conn.connect() as cursor:
        cursor.execute("DELETE FROM books WHERE book_id = %s", book_id)


def get_library_id(book_id):
    conn = open_connection()
    with conn.connect() as cursor:
        result = cursor.execute("SELECT * FROM books WHERE book_id = %s",(book_id))
        library = result.fetchone()

        return library

def get_library_user(library_id):
    conn = open_connection()
    with conn.connect() as cursor:
        result = cursor.execute("SELECT * FROM Libraries WHERE library_id = %s",(library_id))
        lib_data = result.fetchone()

        return lib_data




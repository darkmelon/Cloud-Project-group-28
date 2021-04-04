
#db.py
import os
import pymysql
import sqlalchemy

db_user = "booksdb"
db_pass = "abcd1234"
db_name = "booksdb"
cloud_sql_connection_name = "united-time-307112:europe-west2:booksdb"
db_socket_dir= "/cloudsql"
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
            database=db_name,  # e.g. "my-database-name"
            query={
                "unix_socket": "{}/{}".format(
                    db_socket_dir,  # e.g. "/cloudsql"
                    cloud_sql_connection_name)  # i.e "<PROJECT-NAME>:<INSTANCE-REGION>:<INSTANCE-NAME>"
            }
        ),

    )
    # [END cloud_sql_mysql_sqlalchemy_create_socket]

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
        conn.commit()
        conn.close()

def get_users():
    conn = open_connection()
    with conn.connect() as cursor:
        cursor.execute("SELECT * FROM Users ")
        books = cursor.fetchall()
        conn.close()
        return books

def add_library(libraryname,Description,userid):
    conn = open_connection()
    with conn.connect() as cursor:
        cursor.execute("INSERT INTO Libraries (name,description,user_id) VALUES (%s,%s,%s)", (libraryname,Description,userid))
        conn.commit()
        conn.close()

def get_libraryname(userid):
    conn = open_connection()
    with conn.connect() as cursor:
        cursor.execute("SELECT name ,library_id  FROM Libraries where user_id = '%s' " %userid)
        library_name = cursor.fetchall()
        conn.close()
        return library_name

def add_books(libraryid,bookid,title,author):
    conn = open_connection()
    with conn.connect() as cursor:
        cursor.execute("INSERT INTO books (library_id,Googlebooksapiid,title,author) VALUES (%s,%s,%s,%s) ",(libraryid,bookid,title,author))
        conn.commit()
        conn.close()

def add_users(username, password):
    conn = open_connection()
    with conn.connect() as cursor:
        cursor.execute("INSERT INTO Users (username,password) VALUES (%s,%s)", (username, password))
        conn.commit()
        conn.close()


def get_users():
    conn = open_connection()
    with conn.connect() as cursor:
        cursor.execute("SELECT * FROM Users ")
        books = cursor.fetchall()
        conn.close()
        return books


def add_lib(libraryname, Description, userid):
    conn = open_connection()
    with conn.connect() as cursor:
        cursor.execute("INSERT INTO Libraries (name,description,user_id) VALUES (%s,%s,%s)",
                    (libraryname, Description, userid))
        conn.commit()
        conn.close()


def get_libraries(user_id):
    conn = open_connection()
    with conn.connect() as cursor:
        result = cursor.execute("SELECT * FROM Libraries WHERE user_id = %s",(user_id))
        libraries = result.fetchall()
        conn.close()
        return libraries


def update_lib(library_id,name,description):
    conn = open_connection()
    with conn.connect() as cursor:
        cursor.execute("UPDATE Libraries SET name = %s, description = %s WHERE library_id = %s",(name,description,library_id))
        conn.commit()
        conn.close()


def delete_lib(library_id):
    conn = open_connection()
    with conn.connect() as cursor:
        cursor.execute("DELETE FROM Libraries WHERE library_id = %s", library_id)
        conn.commit()
        conn.close()

def get_bk(library_id):
    conn = open_connection()
    with conn.connect() as cursor:
        cursor.execute("SELECT * FROM books WHERE library_id = %s",(library_id))
        books = cursor.fetchall()
        conn.close()
        return books

def update_bk(book_id,name,author,genre):
    conn = open_connection()
    with conn.connect() as cursor:

        cursor.execute("UPDATE books SET name = %s, author = %s, genre = %s WHERE book_id = %s",(name,author,genre,book_id))
        conn.commit()
        conn.close()


def get_userlib(library_id):
    conn = open_connection()
    with conn.connect() as cursor:
        cursor.execute("SELECT * FROM Libraries WHERE library_id = %s",(library_id))
        library = cursor.fetchone()
        conn.close()
        return library

def delete_bk(book_id):
    conn = open_connection()
    with conn.connect() as cursor:
        cursor.execute("DELETE FROM books WHERE book_id = %s", book_id)
        conn.commit()
        conn.close()

def get_library_id(book_id):
    conn = open_connection()
    with conn.connect() as cursor:
        cursor.execute("SELECT * FROM books WHERE book_id = %s",(book_id))
        library = cursor.fetchone()
        conn.close()
        return library

def get_library_user(library_id):
    conn = open_connection()
    with conn.connect() as cursor:
        cursor.execute("SELECT * FROM Libraries WHERE library_id = %s",(library_id))
        lib_data = cursor.fetchone()
        conn.close()
        return lib_data




# Cloud-Project-groupp-28

This file will explain the purpose of each of the files we used in our application:

Main python files:
*****************

db.py -> This is the python file that we used for the connection with our external cloud database(Google Cloud SQL ).Every time we modify,add,open or delete any User,Library or Books data this file will get called from main.py 
main.py -> This is our main application file that will execute the CURD operation using Flask, we have googles books API that also connected here. The routing for the different web sites are also done here

Static folder:All CSS and JS files will be saved here.
*****************

styles.css --> This is the cascade style sheet file and it contains the background styles we used in our application's log page and registration page.This is located within css folder and that css folder is located within static folder.
index.js -> This java script we have used for our library and books page to display the details and their look and feel.This file is in the static folder.


templates Folder: All our html pages are stored in templates folder.
*******************************************************************

login.html:  Login page of our application
register.html:  Registration page of our application
home.html: After successful login user will be directed to this page.User can add library or search book from this page.
Create_library.htm: once user click on add new library button on home.html this page will get open.
library.html:Once user entered the library name and details application will navigate to next page called library page where user can see all the added library information user just entered in last page.This will also allow the user to open, update or delete any library they added.
search.html : If user clicks on Search Books Here button on library page, application will navigate to search.html page.It will ash user to enter the books name that they want to search from google books API.
search_results.html: Once user enter the search book details then application will connect with google books API and display all related books in the search_result.html page.


requirements.txt
******************
This file will be used for specifying all the python packages are required to run the project.












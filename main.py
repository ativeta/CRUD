from books_data import *
from data import authors_list
from list_CRUD import *

authors = authors_list()
books = books_data()

id_counter = 3

while True:
    options_list()
    option = input()
    match option:
        case '1':
            print("Autoriai ir knygos:")
            print_authors(authors, books)
        case '2':
            print("Jūs pasirinkote įtraukti naują autorių į sąrašą")
            id_counter = add_author(id_counter, authors)
        case '3':
            print("Jūs pasirinkote redaguoti autorių")
            author_update(authors)
        case '4':
            print("Jūs pasirinkote pašalinti autorių. Kurį autorių norite pašalinti?")
            delete_author(authors)
        case '5':
            print("Darbas baigtas. Iki kito karto!")
            break
        case _ :
            print("Tokio pasirinkimo nėra. Bandykite dar kartą.")


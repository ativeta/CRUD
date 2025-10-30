def options_list():
    print("Pasirinkite, ką norite daryti toliau:")
    print("1. Peržiūrėti knygų autorius ir jų knygas")
    print("2. Pridėti naują autorių ir knygą")
    print("3. Redaguoti autorių")
    print("4. Redaguoti knygą")
    print("5. Ištrinti autorių arba knygą")
    print("6. Baigti bibliotekos peržiūrą")


def library_options():
    print("1. Peržiūrėti autorių sąrašą")
    print("2. Peržiūrėti knygų sąrašą")
    print("3. Peržiūrėti knygas pagal autorių")



library_options()



def print_authors(authors, books):
    for book in books:
        for author in authors:
            if author['id'] == book['author_id']:
                print(
                    f"{author['id']}. {author['name']} {author['surname']}, Knyga: '{book['book_title']}', Žanras: {book['book_genre']}")
    print("Jeigu norite pamatyti tik autorius, įrašykite raidę A. Jei norite pamatyti tik knygas, įrašykite raidę B")
    while True:
        letter = input().upper()
        match letter:
            case 'A':
                for author in authors:
                    print(f'{author['id']}. Autorius: {author['name']} {author['surname']}')
            case 'B':
                for book in books:
                    print(f'{book["id"]}. {book["book_title"]} {book["book_genre"]}')
            case _ :
                print(f'Tokio pasirinkimo nėra. Grįžtame į pradinį meniu.')
                options_list()

def add_author(id_counter,authors):
    print("Įveskite autoriaus vardą:")
    name = input()
    print("Įveskite autoriaus pavardę:")
    surname = input()
    id_counter += 1
    author = {'id': id_counter, "name": name, "surname": surname}
    authors.append(author)
    print("Autorius sėkmingai įtrauktas!")

def author_update(authors):
    print("Įrašykite autoriaus ID, kurį norite redaguoti")
    edit_id = input()
    found = False
    for i, author in enumerate(authors):
        if str(author['id']) == edit_id:
            print(f"{author['id']}. Autorius: {author['name']} {author['surname']}")
            print("Įveskite naują autoriaus vardą:")
            authors[i]['name'] = input()
            print("Įveskite naują autoriaus pavardę:")
            authors[i]['surname'] = input()
            print("Autoriaus duomenys sėkmingai atnaujinti!")
            found = True
    if not found:
            print("Autorius su tokiu ID neegzistuoja. Pasirinkite kitą ID")

def delete_author(authors):
    print_authors(authors)
    print("Įrašykite autoriaus ID, kurį norite pašalinti")
    del_id = input()
    found = False
    for author in authors:
        if str(author['id']) == del_id:
            authors.remove(author)
            print("Autoriaus duomenys sėkmingai ištrinti!")
            found = True
            break
    if not found:
        print("Autorius su tokiu ID neegzistuoja. Pasirinkite kitą ID")
def options_list():
    print("Pasirinkite, ką norite daryti toliau:")
    print("1. Peržiūrėti knygų autorius")
    print("2. Pridėti naują autorių")
    print("3. Redaguoti autorių")
    print("4. Ištrinti autorių")
    print("5. Baigti autorių peržiūrą")

def print_authors(authors):
    for author in authors:
        print(f'{author['id']}. Autorius: {author['name']} {author['surname']}')

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
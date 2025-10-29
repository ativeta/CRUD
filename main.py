authors = [
    {
        'id':1,
        'name':'Kristina',
        'surname':'Sabaliauskaitė',
    },
    {
        'id':2,
        'name':'Tomas',
        'surname':'Venclova',
    },
    {
        'id':3,
        'name':'Undinė',
        'surname':'Radzevičiūtė',
    }
]

id_counter = 3
while True:
    print("Pasirinkite, ką norite daryti toliau")
    print("1. Peržiūrėti knygų autorius")
    print("2. Pridėti naują autorių")
    print("3. Redaguoti autorių")
    print("4. Ištrinti autorių")
    print("5. Baigti autorių peržiūrą")

    option = input()
    match option:
        case '1':
            print("Jūs pasirinkote peržiūrėti autorių sąrašą")
            for item in authors:
                print(item)
        case '2':
            print("Jūs pasirinkote įtraukti naują autorių į sąrašą")
            print("Įveskite autoriaus vardą")
            name = input()
            print("Įveskite autoriaus pavardę")
            surname = input()
            id_counter +=1
            item = {'id':id_counter, "name":name, "surname":surname}
            authors.append(item)

        case '3':
            print("Jūs pasirinkote redaguoti autorių")
            print("Įrašykite autoriaus ID, kurį norite redaguoti")
            edit_id = input()
            for i, item in enumerate(authors):
                if str(item['id']) == edit_id:
                    print(item)
                    print("Įveskite autoriaus vardą")
                    authors[i]['name'] = input()
                    print("Įveskite autoriaus pavardę")
                    authors[i]['surname'] = input()
        case '4':
            print("Jūs pasirinkote pašalinti autorių")
            print("Įrašykite autoriaus ID, kurį norite pašalinti")
            del_id = input()
            for item in authors:
                if str(item['id']) == del_id:
                    authors.remove(item)
                    break
        case '5':
            print("Jūs pasirinkote baigti autorių sąrašo peržiūrą")
            break
        case _ : #defaultas, kai ivedama belekas
            print("Ar jūs tikrai tai turėjote omenyje")
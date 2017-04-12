import csv

dictionery = {"parameter": ("co to paramter", "zrodlo"), "function": ("co to funkcja", "zrodlo")}

# z biblioteki pythona
def read_from_csv(name_csv):
    with open(name_csv, 'rb') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        for row in spamreader:
            add_from_csv(row[0], row[1], row[2])


def search():
    print("podaj nazwe do wyszukania")
    name = input()
    if dictionery.get(name):
        print(dictionery.get(name))
    else:
        print("nie ma takiego klucza")


def add_from_csv(defintion, explenation, source):
    dictionery.update({defintion: (explenation, source)})


def add():
    print("podaj defincje")
    defintion = input()
    print("podaj wytlumaczenie definicji")
    explenation = input()
    print("podaj zrodlo")
    source = input()
    dictionery.update({defintion: (explenation, source)})


def show_all():
    for definition, explanation in sorted(dictionery.items()):
        print(definition, explanation)


def show_available():
    print("podaj pierwsza litere")
    key_first_letter = input()
    if len(key_first_letter) == 1:
        for definition, explanation in sorted(dictionery.items()):
            if definition[0] == key_first_letter:
                print(explanation)
    else:
        print("podales wiecej niz jedna litere")


def main():
    # read_from_csv("nazwa.csv")
    print("Dictionary for a little programmer:")
    print("1 - serach")
    print("2 - add")
    print("3 - show all")
    print("4 - show all by first letter")
    print("0 - exit")
    print("podaj liczbe do wybou")

    #input_read = int(input()) #nie odporny na dupa
    input_read = input()
    #yes = input_read.isdigit()
    if input_read.isdigit():
        print ("ok")
        input_read = int(input_read)
    else: 
        print("It's not a number from 0 to 4")
    

    
    #while yes:
    if input_read == 1:
        search()
    elif input_read == 2:
        add()
    elif input_read == 3:
        show_all()
    elif input_read == 4:
        show_available()
    elif input_read == 0:
        return
    else:
        print("In menu no such a number, try again") #zeby wracało???
        main()
    #else:
        #print("Type a number from 0 to 4")
    


main()

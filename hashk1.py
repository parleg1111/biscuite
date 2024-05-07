table, tableq = {},{}
totl, totq = 0, 0

def create(b):
    for i in range(b):
        table[i] = None
        tableq[i] = None

def linsert(name, number, b):
    global totl
    hash_val = number % b
    flag = 0

    if table[hash_val] is None:
        table[hash_val] = {'name': name, 'number': number}
    else:
        for i in range(b):
            hash_val = (number + i) % b
            if table[hash_val] is None:
                table[hash_val] = {'name': name, 'number': number}
                totl += 1
                flag += 1
                break

    if flag == 0:
        print("Table Full or Entry not probed.")

def qinsert(name, number, b):
    global totq
    hash_val = number % b
    flag = 0

    if tableq[hash_val] is None:
        tableq[hash_val] = {'name': name, 'number': number}
    else:
        for i in range(0, int((b - 1) / 2)):
            hash_val = (number+ (i * i)) % b
            if tableq[hash_val] is None:
                tableq[hash_val] = {'name': name, 'number': number}
                totq += 1
                flag += 1
                break

    if flag == 0:
        print("Table Full or Entry not probed.")

def Isearch(number, b):
    hash_val = number % b
    flag = 0

    if table[hash_val] is None:
        print("Entry with Number:", number, " is not present.")
    else:
        for i in range(b):
            hash_val = (number + i) % b
            if table[hash_val] is None:
                print("Entry with Number:", number, " is not present.")
                flag += 1
                break
            elif table[hash_val]['number'] == number:
                print("Entry with Number:", number, " is present at location:", hash_val)
                print("Name:", table[hash_val]['name'])
                flag += 1
                break

    if flag == 0:
        print("Entry with Number:", number, " is not present.")

def qsearch(number, b):
    hash_val = number % b
    flag = 0

    if tableq[hash_val] is None:
        print("Entry with Number:", number, " is not present.")
    else:
        for i in range(0, int((b - 1) / 2)):
            hash_val = (number + (i * i)) % b
            if tableq[hash_val] is None:
                print("Entry with Number:", number, " is not present.")
                flag += 1
                break
            elif tableq[hash_val]['number'] == number:
                print("Entry with Number:", number, " is present at location:", hash_val)
                print("Name:", tableq[hash_val]['name'])
                flag += 1
                break

    if flag == 0:
        print("Entry with Number:", number, " is not present.")

def printtable(b):
    print("Linearly Probed Table:")
    for i in range(b):
        print(table[i], end="|")
    print("\nQuadratically Probed Table:")
    for i in range(b):
        print(tableq[i], end="|")
    print("")

b = int(input("Enter the table size: "))
create(b)

while True:
    ch = int(input("Enter 1-LP | 2-QP | 0-EXIT: "))
    
    if ch == 1:
        while True:
            ch2 = int(input("Enter 1-Insert | 2-Search | 0-Back: "))
            
            if ch2 == 1:
                if totl == b:
                    print("The table is already full.")
                else:
                    name = input("Enter the name: ")
                    number = int(input("Enter the number: "))
                    linsert(name, number, b)
                    
            elif ch2 == 2:
                number = int(input("Enter the number to be searched in the table: "))
                Isearch(number, b)
                
            elif ch2 == 0:
                print("GOING BACK")
                break

            printtable(b)

    elif ch == 2:
        while True:
            ch2 = int(input("Enter 1-Insert | 2-Search | 0-Back: "))
            if ch2 == 1:
                if totq == b:
                    print("The table is already full.")
                else:
                    name = input("Enter the name: ")
                    number = int(input("Enter the number: "))
                    qinsert(name, number, b)
                    
            elif ch2 == 2:
                number =int(input("Enter the number to be searched in the table: "))
                qsearch(number, b)
                
            elif ch2 == 0:
                print("GOING BACK")
                break

            printtable(b)

    elif ch == 0:
        print("EXITED")
        printtable(b)
        break

    else:
        print("Invalid input.")
        printtable(b)
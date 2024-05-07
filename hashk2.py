table = {}
totl = 0

def create(b):
    for i in range(b):
        table[i] = None

def linsert(name, number, b):
    global totl
    hash_val = number % b
    flag = 0

    if table[hash_val] is None:
        table[hash_val] = {'name': name, 'number': number}
    else:
        for i in range(b):
            hash_val = 7-(number%7)
            if table[hash_val] is None:
                table[hash_val] = {'name': name, 'number': number}
                totl += 1
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
            hash_val = 7-(number%7)
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

def printtable(b):
    print("doubled hashed Probed Table:")
    for i in range(b):
        print(table[i], end="|")

b = int(input("Enter the table size: "))
create(b)

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
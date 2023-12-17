# This is how we use getattr format 

myList= []

while True:
    command= input('Enter the command').lower()

    if command== 'exit':
        break

    value= input("enter the value")

    try:
        value= int(value)

        if command== 'print':
            print(myList)
        else:
            getattr(myList,command)(value)
    except ValueError:
        print('please print a valid integer') 
    print(myList)

import addressbook_pb2

_TIMEOUT_SECONDS = 10

def insert(stub):
    insertentry = addressbook_pb2.Person()
    insertentry.id = int(raw_input("Enter ID: "))
    insertentry.name = raw_input("Enter Name: ")
    number = raw_input("Enter a phone number: ")
    telephone = insertentry.phone.add()
    telephone.number = number
    contact = raw_input("mobile/home/work : ")
    if contact == "mobile":
        telephone.type = addressbook_pb2.Person.MOBILE
    elif contact == "home":
        telephone.type = addressbook_pb2.Person.HOME
    elif contact == "work":
        telephone.type = addressbook_pb2.Person.WORK
    else:
        print "No Type Mentioned."

    email = raw_input("Enter email address:")
    if email != "":
        insertentry.email = email

    response = stub.InsertEntry(insertentry, _TIMEOUT_SECONDS)


def display(stub):
    disp = addressbook_pb2.DisplayAll(display1='')
    response = stub.AllEntries(disp, _TIMEOUT_SECONDS)
    print "Printing All Entries"
    for i in response.person:
        print "ID: ", i.id
        print "Name: ", i.name
        if i.email is not None:
            print "Email: ", i.email
        print "\n"

def run():
    with addressbook_pb2.early_adopter_create_Greeter_stub('localhost', 50051) as stub:

        while 1:
            print("Enter your choice:\n")
            print("1. Insert\n2. Display\n3. Exit\n")
            choice = raw_input()
            if choice == '1':
                insert(stub)
            elif choice == '2':
                display(stub)
            else:
                exit(0)

if __name__ == '__main__':
    run()

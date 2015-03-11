
import time

import addressbook_pb2

_ONE_DAY_IN_SECONDS = 60 * 60 * 24


class Greeter(addressbook_pb2.EarlyAdopterGreeterServicer):

    addressbook = addressbook_pb2.AddressBook()

    def InsertEntry(self, request, context):
        Greeter.addressbook.person.extend([request])
        return addressbook_pb2.AddressReply(message='%s Entry Added' % request.name)

    def AllEntries(self, request, context):
        return addressbook_pb2.AddressBook(person=Greeter.addressbook.person)


def serve():
        server = addressbook_pb2.early_adopter_create_Greeter_server(
        Greeter(), 50051, None, None)
        server.start()
        try:
            while True:
                time.sleep(_ONE_DAY_IN_SECONDS)
        except KeyboardInterrupt:
             server.stop()

if __name__ == '__main__':
    serve()

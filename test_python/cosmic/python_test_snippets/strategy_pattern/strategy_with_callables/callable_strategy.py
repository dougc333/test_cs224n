from support.callable_app import (
    CustomerSupport,
    FIFOProcessing,
    FILOProcessing,
    RandomProcessing,
)
from support.callable_ticket import SupportTicket


def main():
    app = CustomerSupport()
    app.add_ticket(SupportTicket("John Smith", "My computer makes strange sounds"))
    app.add_ticket(SupportTicket("Linus Sebastian", "I cant upload videos please help"))
    app.add_ticket(SupportTicket("Arjan Codes", "VSCOde broken"))

    print("FILO")
    app.process_tickets(FILOProcessing())
    print("FIFO")
    # no () for fn.
    app.process_tickets(FIFOProcessing)
    print("Random")
    app.process_tickets(RandomProcessing())


if __name__ == "__main__":
    main()


from support.protocol_app import FIFOProcessing,RandomProcessing,FILOProcessing, CustomerSupport
from support.protocol_ticket import SupportTicket

def main():
    app = CustomerSupport()
    app.add_ticket(SupportTicket("John Smith", "My computer makes strange sounds"))
    app.add_ticket(SupportTicket("Linus Sebastian", "I cant upload videos please help"))
    app.add_ticket(SupportTicket("Arjan Codes", "VSCOde broken"))
    
    print("FILO")
    app.process_tickets(FILOProcessing())
    print("FIFO")
    app.process_tickets(FIFOProcessing())
    print("Random")
    app.process_tickets(RandomProcessing())

if __name__=='__main__':
    main()
    
    


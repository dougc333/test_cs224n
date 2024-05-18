
from support.app import CustomerSupport
from support.ticket import SupportTicket

def main():
    app = CustomerSupport()
    app.add_ticket(SupportTicket("John Smith", "My computer makes strange sounds"))
    app.add_ticket(SupportTicket("Linus Sebastian", "I cant upload videos please help"))
    app.add_ticket(SupportTicket("Arjan Codes", "VSCOde broken"))
    
    app.process_tickets("fifo")

if __name__=='__main__':
    main()


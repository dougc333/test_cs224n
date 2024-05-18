
from support.strategy_app import FifoOrderingStrategy, RandomOrderingStrategy
from support.strategy_app import FILOOrderingStrategy
from support.strategy_app import CustomerSupport
from support.strategy_ticket import SupportTicket

def main():
    app = CustomerSupport()
    #little weird there is no id in the original ctor,like ticketID. 
    app.add_ticket(SupportTicket("John Smith", "My computer makes strange sounds"))
    app.add_ticket(SupportTicket("Linus Sebastian", "I cant upload videos please help"))
    app.add_ticket(SupportTicket("Arjan Codes", "VSCOde broken"))
    print("FILOOrderingStrategy")
    app.process_tickets(FILOOrderingStrategy())
    print("------------------")
    print("----Random--------------")
    app.process_tickets(RandomOrderingStrategy())
    print("------------------")
    print("------FILO------------")
    app.process_tickets(FifoOrderingStrategy())    

if __name__=='__main__':
    main()


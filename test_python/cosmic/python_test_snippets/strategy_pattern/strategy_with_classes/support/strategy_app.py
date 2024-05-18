#
from abc import ABC, abstractmethod
from support.strategy_ticket import SupportTicket
import random

class TicketOrderingStrategy(ABC):
    @abstractmethod
    def create_ordering(self,tickets:list[SupportTicket]) -> list[SupportTicket]:
        """returns unordered list of tickets"""
        
class FifoOrderingStrategy(TicketOrderingStrategy):
    def create_ordering(self, tickets: list[SupportTicket]) -> list[SupportTicket]:
        return tickets.copy()

class FILOOrderingStrategy(TicketOrderingStrategy):
    def create_ordering(self, tickets: list[SupportTicket]) -> list[SupportTicket]:
        return list(reversed(tickets))

class RandomOrderingStrategy(TicketOrderingStrategy):
    def create_ordering(self, tickets: list[SupportTicket]) -> list[SupportTicket]:
        return random.sample(tickets,len(tickets))

class CustomerSupport:
    def __init__(self):
        self.tickets: list[SupportTicket] = []
        
    def add_ticket(self,ticket: SupportTicket):
        self.tickets.append(ticket)
    
    def process_tickets(self, processing_strategy:TicketOrderingStrategy):
        ticket_list = processing_strategy.create_ordering(self.tickets)
        
        #is this better than the for loop? The 1 line generator exexuting the iterator? 
        list(ticket.process() for ticket in ticket_list)
        #for ticket in ticket_list:
        #    ticket.process()
        #removed the emptying of the list so I can see the ordering change
        
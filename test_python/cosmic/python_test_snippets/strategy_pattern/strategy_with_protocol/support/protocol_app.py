import random
from abc import abstractmethod
from typing import Protocol

from support.protocol_ticket import SupportTicket


class TicketProcessing(Protocol):
    @abstractmethod
    def process_ticket(self, tickets: list[SupportTicket]) -> list[SupportTicket]:
        print("PT ABSTRACT")
        raise NotImplementedError


# saves code, duck typing system figures out FIFOProcessing part of TicketProcessing
class FIFOProcessing:
    def process_ticket(self, tickets: list[SupportTicket]) -> list[SupportTicket]:
        print("PT FIFO")
        return tickets.copy()


class FILOProcessing:
    def process_ticket(self, tickets: list[SupportTicket]) -> list[SupportTicket]:
        return reversed(tickets)


class RandomProcessing:
    def process_ticket(self, tickets: list[SupportTicket]) -> list[SupportTicket]:
        return random.sample(tickets, len(tickets))


class CustomerSupport:
    def __init__(self):
        self.tickets: list[SupportTicket] = []

    def add_ticket(self, ticket: SupportTicket):
        self.tickets.append(ticket)

    def process_tickets(self, processing_strategy: TicketProcessing):

        ticket_ordering_list = processing_strategy.process_ticket(self.tickets)

        for ticket in ticket_ordering_list:
            ticket.process()

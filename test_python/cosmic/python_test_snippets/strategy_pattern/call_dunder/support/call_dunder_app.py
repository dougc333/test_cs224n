import random
from typing import Protocol

from support.call_dunder_ticket import SupportTicket


# does this only work for 1 fn in this class? yes
# if there are multiple functions can you nest them each with call? No you have
# to use more arguments and parse the list of arguments to add additional functionality
class TicketProcessing(Protocol):
    def __call__(self, tickets: list[SupportTicket]) -> list[SupportTicket]:
        print("PT ABSTRACT You should never see this")
        raise NotImplementedError


# saves code, duck typing system figures out FIFOProcessing part of TicketProcessing
class FIFOProcessing:
    def __call__(self, tickets: list[SupportTicket]) -> list[SupportTicket]:
        print("PT FIFO")
        return tickets.copy()


class FILOProcessing:
    def __call__(self, tickets: list[SupportTicket]) -> list[SupportTicket]:
        return list(reversed(tickets))


class RandomProcessing:
    def __call__(self, tickets: list[SupportTicket]) -> list[SupportTicket]:
        return random.sample(tickets, len(tickets))


class CustomerSupport:
    def __init__(self):
        self.tickets: list[SupportTicket] = []

    def add_ticket(self, ticket: SupportTicket):
        self.tickets.append(ticket)

    def process_tickets(self, processing_strategy: TicketProcessing):

        ticket_ordering_list = processing_strategy(self.tickets)

        for ticket in ticket_ordering_list:
            ticket.process()

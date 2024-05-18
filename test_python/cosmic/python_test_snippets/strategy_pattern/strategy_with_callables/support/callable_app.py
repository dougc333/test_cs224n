import random
from typing import Callable

from support.callable_ticket import SupportTicket

# this is confusing. What are teh rules for Callable to match the classes
# to Callable? Callable defines a type and uses __call__ to matchcd
TicketOrderingStrategy = Callable[[list[SupportTicket]], list[SupportTicket]]

# TicketOrderingStrategy = Callable(list[SupportTicket], list[SupportTicket])


""" class FIFOProcessing:
    def __call__(self, tickets: list[SupportTicket]) -> list[SupportTicket]:
        print("PT FIFO")
        return tickets.copy() """

# functions are callable also it doesnt matter if class or fn
def FIFOProcessing(tickets: list[SupportTicket]):
    return tickets.copy()


# document creator fn vs class? is this necessary? See this a lot
# in old code. nexted functions with parameters vs class variables
# this is a closure. closure functions vs classes. add partials here
# and you are supposed to use closure dunder methods.


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

    def process_tickets(self, processing_strategy: TicketOrderingStrategy):

        ticket_ordering_list = processing_strategy(self.tickets)

        for ticket in ticket_ordering_list:
            ticket.process()

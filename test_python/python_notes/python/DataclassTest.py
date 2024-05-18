from dataclasses import dataclass, field




@dataclass(frozen=True, eq=False)
class LineItem:
    id: str = field(default_factory=str)
    product_name: str = field(default_factory=str)
    quantity: int = field(default_factory=int)


@dataclass(frozen=True, eq=False)
class Order:
    id: str = field(default_factory=str)
    customer_id: str = field(default_factory=str)
    line_item: LineItem


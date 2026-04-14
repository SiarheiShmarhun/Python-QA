"""Module for managing order statuses using Enum."""

import logging
from enum import Enum

logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')


class OrderStatus(Enum):
    PENDING = "Order awaiting processing"
    IN_PROGRESS = "Order ready"
    READY = "Order ready"
    COMPLETED = "Order completed"
    CANCELED = "Order canceled"


class Order:
    def __init__(self, order_id: int, status: OrderStatus = OrderStatus.PENDING):
        self.order_id = order_id
        self.status = status

    def update_status(self, new_status: OrderStatus) -> None:
        self.status = new_status
        logging.info("Order status #%s updated to: %s", self.order_id, self.status.value)

    def display_status(self) -> None:
        logging.info("Order #%s now: %s", self.order_id, self.status.value)


if __name__ == "__main__":
    my_order = Order(order_id=101)
    my_order.display_status()
    my_order.update_status(OrderStatus.READY)
    my_order.display_status()

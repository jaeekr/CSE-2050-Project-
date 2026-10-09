from node import Node
from linked_list import LinkedList
from stack import Stack
from order_queue import OrderQueue
from order import Order
from product import Product
from customer import Customer
from cart import ShoppingCart
from store import Store
import unittest


class TestStore(unittest.TestCase):
    def setUp(self):
        self.store = Store()
        self.customer = Customer("C1", "Bob")
        self.product = Product("P1", "Laptop", 1000)

        self.store.add_customer(self.customer)
        self.store.add_product(self.product)

    def test_checkout(self):
        self.assertIsNone(self.store.checkout("INVALID_ID"))

        self.assertIsNone(self.store.checkout("c1"))
        self.assertEqual(len(self.store.get_orders()),0)

        self.customer.get_cart().add_product(self.product)
        order = self.store.checkout("C1")
        self.assertIsNotNone(order)
        self.assertEqual(order.get_id(), "O1")
        self.assertEqual(order.get_customer(), self.customer)
        self.assertEqual(order.get_status(), "PENDING")
        self.assertEqual(order.calculate_total(), 1000)
        self.assertTrue(self.customer.get_cart().is_empty())
        self.assertEqual(len(self.store.get_orders()),1)

    def test_process_next_order(self):
        self.customer.get_cart().add_product(self.product)
        order = self.store.checkout("C1")

        processed = self.store.process_next_order()
        self.assertIs(processed, order)
        self.assertEqual(processed.get_status(), "PROCESSING")
        self.assertIsNone(self.store.process_next_order())

    def test_order_history(self):
        product2 = Product("P2", "Mouse", 25)
        customer2 = Customer("C2", "Sam")
        self.store.add_product(product2)
        self.store.add_customer(customer2)

        self.customer.get_cart().add_product(self.product)
        customer2.get_cart().add_product(product2)

        order1 = self.store.checkout("C1")
        order2 = self.store.checkout("C2")
        self.store.process_next_order()
        self.store.process_next_order()

        history = self.store.get_order_history()
        self.assertEqual(history, [order2, order1])
        self.assertEqual(self.store.processed_order.size(), 2)
        self.assertEqual(self.store.get_order_history(), [order2, order1])


class TestNode(unittest.TestCase):
    def test_init(self):
        second = Node('cat')
        first = Node('dog', second)
        self.assertEqual(first.data, 'dog')
        self.assertIs(first.next, second)
        self.assertIsNone(second.next)


class TestLinkedList(unittest.TestCase):
    def test_empty_list(self):
        ll = LinkedList()
        self.assertTrue(ll.is_empty())
        self.assertEqual(ll.size(), 0)
        self.assertIsNone(ll.get_first())
        self.assertIsNone(ll.remove_first())

    def test_add_first(self):
        ll = LinkedList()
        ll.add_first('b')
        ll.add_first('a')
        self.assertEqual(ll.get_first(), 'a')
        self.assertEqual(ll.size(), 2)
        self.assertFalse(ll.is_empty())

    def test_add_last(self):
        ll = LinkedList()
        ll.add_last('a')
        ll.add_last('b')
        ll.add_last('c')
        self.assertEqual(ll.get_first(), 'a')
        self.assertEqual(ll.size(), 3)

    def test_remove_first(self):
        ll = LinkedList()
        ll.add_last('a')
        ll.add_last('b')
        self.assertEqual(ll.remove_first(), 'a')
        self.assertEqual(ll.size(), 1)
        self.assertEqual(ll.remove_first(), 'b')
        self.assertTrue(ll.is_empty())
        ll.add_last('c')
        self.assertEqual(ll.get_first(), 'c')


class TestOrder(unittest.TestCase):
    def test_init(self):
        product1 = Product(10, 'Cup', 5)
        product2 = Product(11, 'Chair', 10)
        product3 = Product(12, 'Bottle', 7)
        product4 = Product(13, 'Sofa', 100)

        list1 = [product1, product2]
        list2 = [product3, product4]

        customer1 = Customer(83243, 'Emilio')
        customer2 = Customer(84870, 'Tony')

        order1 = Order(1, customer1, list1)
        order2 = Order(2, customer2, list2)

        self.assertEqual(order1.order_id, 1)
        self.assertEqual(order1.customer, customer1)
        self.assertEqual(order1.purchased_items, list1)

        self.assertEqual(order2.order_id, 2)
        self.assertEqual(order2.customer, customer2)
        self.assertEqual(order2.purchased_items, list2)

    def test_calculate_total(self):
        product1 = Product(10, 'Cup', 5)
        product2 = Product(11, 'Chair', 10)
        product3 = Product(12, 'Bottle', 7)
        product4 = Product(13, 'Sofa', 100)

        list1 = [product1, product2]
        list2 = [product3, product4]

        customer1 = Customer(83243, 'Emilio')
        customer2 = Customer(84870, 'Tony')

        order1 = Order(1, customer1, list1)
        order2 = Order(2, customer2, list2)

        self.assertEqual(order1.calculate_total(), 15)
        self.assertEqual(order2.calculate_total(), 107)

    def test_get_status(self):
        product1 = Product(10, 'Cup', 5)
        product2 = Product(11, 'Chair', 10)
        product3 = Product(12, 'Bottle', 7)
        product4 = Product(13, 'Sofa', 100)

        list1 = [product1, product2]
        list2 = [product3, product4]

        customer1 = Customer(83243, 'Emilio')
        customer2 = Customer(84870, 'Tony')

        order1 = Order(1, customer1, list1)
        order2 = Order(2, customer2, list2)

        self.assertEqual(order1.get_status(), 'PENDING')

        order1.set_status('PROCESSING')
        order2.set_status('COMPLETED')

        self.assertEqual(order1.get_status(), 'PROCESSING')
        self.assertEqual(order2.get_status(), 'COMPLETED')

        self.assertRaises(ValueError, order1.set_status, 'HELLO')


class TestOrderQueue(unittest.TestCase):
    def test_init(self):
        queue = OrderQueue()
        self.assertTrue(queue.is_empty())
        self.assertEqual(queue.size(), 0)

    def test_enqueue_dequeue(self):
        queue = OrderQueue()

        self.assertTrue(queue.is_empty())

        queue.enqueue('item1')
        queue.enqueue('item2')
        queue.enqueue('item3')

        self.assertFalse(queue.is_empty())
        self.assertEqual(queue.size(), 3)

        self.assertEqual(queue.dequeue(), 'item1')
        self.assertEqual(queue.size(), 2)

        self.assertEqual(queue.dequeue(), 'item2')
        self.assertEqual(queue.size(), 1)

        self.assertEqual(queue.dequeue(), 'item3')
        self.assertTrue(queue.is_empty())

        self.assertEqual(queue.dequeue(), None)

    def test_peek(self):
        queue = OrderQueue()

        self.assertEqual(queue.peek(), None)

        queue.enqueue('item1')
        queue.enqueue('item2')
        queue.enqueue('item3')

        self.assertEqual(queue.size(), 3)
        self.assertEqual(queue.peek(), 'item1')

        queue.dequeue()
        self.assertEqual(queue.peek(), 'item2')

        queue.dequeue()
        self.assertEqual(queue.peek(), 'item3')

        queue.dequeue()
        self.assertEqual(queue.peek(), None)


class TestStack(unittest.TestCase):
    def test_init(self):
        my_stack = Stack()
        self.assertEqual(my_stack.size(), 0)
        self.assertIsNone(my_stack.peek())
        self.assertTrue(my_stack.is_empty())

    def test_stack_functions(self):
        my_stack = Stack()

        my_stack.push('apple')
        self.assertEqual(my_stack.size(), 1)
        self.assertEqual(my_stack.peek(), 'apple')
        self.assertFalse(my_stack.is_empty())

        my_stack.pop()
        self.assertEqual(my_stack.size(), 0)
        self.assertTrue(my_stack.is_empty())

        my_stack.push('banana')
        my_stack.push(5)
        my_stack.push('even')

        self.assertEqual(my_stack.size(), 3)
        self.assertEqual(my_stack.peek(), 'even')
        self.assertFalse(my_stack.is_empty())

        my_stack.pop()
        self.assertEqual(my_stack.size(), 2)
        self.assertEqual(my_stack.peek(), 5)
        self.assertFalse(my_stack.is_empty())

    def test_pop_empty_stack(self):
        my_stack = Stack()
        self.assertIsNone(my_stack.pop())
        self.assertEqual(my_stack.size(), 0)


if __name__ == "__main__":
       unittest.main()

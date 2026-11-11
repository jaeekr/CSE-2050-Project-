import unittest 
from node import Node
from linked_list import LinkedList
from stack import Stack
from order_queue import OrderQueue
from order import Order
from product import Product
from customer import Customer
from cart import ShoppingCart
from store import Store
from algorithms import (recursive_total_price, fewest_coins, bubble_sort, selection_sort, insertion_sort, binary_search)
from entry import Entry
from hash_mapping import HashMapping

class TestHash_Mapping(unittest.TestCase):

    def test_len(self):
        m = HashMapping()
        self.assertEqual(m._len,0)

    def test_put(self):
        m = HashMapping()
        m.put("P100", "Keyboard")
        x= m._find_entry("P100")
        self.assertEqual(x, "P100")

    def test_get(self):
        pass

    def test_rehash(self):
        pass

    def test_collisions(self):
        pass

    def test_update(self):
        m = HashMapping(size=3)
        m.put("P100", "Keyboard")
        m.put("P100", "Wireless Keyboard")
        self.assertEqual(m.get("P100"), "Wireless Keyboard")
        self.assertEqual(len(m), 1)

    def test_missing_key_raises(self):
        m = HashMapping(size=3)
        m.get("P999")
        self.assertRaises(KeyError)
        
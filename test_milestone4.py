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
        self.assertEqual(len(m),0)
        m.put("P100", "Keyboard")
        self.assertEqual(len(m), 1)

    def test_put(self):
        m = HashMapping()
        m.put("P100", "Keyboard")
        self.assertEqual(m.get("P100"), "Keyboard")
        self.assertIn("P100", m)

    def test_get(self):
        m = HashMapping(size=3)
        m.put("P100", "Keyboard")
        m.put("P200", "Headphones")
        m.put("P300", "Mouse")
        self.assertEqual(m.get("P100"), "Keyboard")
        self.assertEqual(m.get("P200"), "Headphones")
        self.assertEqual(m.get("P300"), "Mouse")
        self.assertNotIn("P999", m)

    def test_rehash(self):
        m = HashMapping()
        for i in range(50):
            m.put(f"P{i}", i)
        self.assertEqual(len(m), 50)
        for i in range(50):
            self.assertEqual(m.get(f"P{i}"), i)
        self.assertNotIn("P999", m)

    def test_collisions(self):
        m = HashMapping(size=2)
        for key, value in [("A", 1), ("B", 2), ("C", 3), ("D", 4), ("E", 5)]:
            m.put(key, value)
        self.assertEqual(len(m), 5)
        self.assertEqual(m.get("A"), 1)
        self.assertEqual(m.get("B"), 2)
        self.assertEqual(m.get("C"), 3)
        self.assertEqual(m.get("D"), 4)
        self.assertEqual(m.get("E"), 5)

    def test_update(self):
        m = HashMapping(size=3)
        m.put("P100", "Keyboard")
        m.put("P100", "Wireless Keyboard")
        self.assertEqual(m.get("P100"), "Wireless Keyboard")
        self.assertEqual(len(m), 1)

    def test_missing_key_raises(self):
        m = HashMapping(size=3)
        self.assertRaises(KeyError, m.get, "P999")







if __name__ == "__main__":
    unittest.main()
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
from algorithms import (recursive_total_price, fewest_coins, bubble_sort, selection_sort, insertion_sort, binary_search, merge_sort, quick_sort, quick_select)
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

class Milestone4_algorithms(unittest.TestCase):
    def check_sort(self, sort_func):
        a = Product('A1', 'Camera', 20)
        b = Product('B1', 'Phone', 30)
        c = Product('C1', 'Tablet', 10)
        expected = [a, b, c]

        for data in ([b, c, a], [a, b, c], [c, b, a]):
            l1 = list(data)      
            sort_func(l1)
            self.assertEqual(l1, expected)

        empty_list = []
        self.assertEqual(sort_func(empty_list), [])

        list_of_one = [a]
        self.assertEqual(sort_func(list_of_one), [a])

    def test_merge_sort(self):
        self.check_sort(merge_sort)

    def test_quick_sort(self):
        self.check_sort(quick_sort)

    def test_quick_select(self):
        a = Product('A1', 'Camera', 20)
        b = Product('B1', 'Phone', 30)
        c = Product('C1', 'Tablet', 10)
        products = [a, b, c]

        # Test finding the smallest element
        self.assertEqual(quick_select(products, 0), c)
        # Test finding the largest element
        self.assertEqual(quick_select(products, 2), b)
        # Test finding the middle element
        self.assertEqual(quick_select(products, 1), a)

        empty_list = []
        self.assertIsNone(quick_select(empty_list, 0))
        list_of_one = [a]
        self.assertEqual(quick_select(list_of_one, 0), a)

class TestStoreIntegration(unittest.TestCase):

    def set_up(self):
        store = Store()
        p1 = Product("A0", "Mouse", 29.99)
        p2 = Product("A1", "Keyboard", 59.99)
        p3 = Product("A3", "Headphones", 39.99)

        self.store.add_product(p1)
        self.store.add_product(p2)
        self.store.add_product(p3)

    def test_sort(self):
        self.store.products.reverse()  #unsorts
        self.store.merge_sort_products()
        ids = [p.get_id() for p in self.store.products] # gets ids for each product
        self.assertEqual(ids, ["A0", "A1", "A3"]) #checks ids against actrual ones

        self.store.products.reverse()  # unsorts
        self.store.quick_sort_products()
        ids = [p.get_id() for p in self.store.products]
        self.assertEqual(ids, ["A0", "A1", "A3"])
        
    def test_quick_select(self):
        self.assertEqual(self.store.quick_select_product(1).get_id(), "A0")
        self.assertEqual(self.store.quick_select_product(3).get_id(), "A3")
        self.assertIsNone(self.store.quick_select_product(0))
        self.assertIsNone(self.store.quick_select_product(4))

    def test_find_product(self):
        self.assertEqual(self.store.find_product("A1").get_name(), "Keyboard")
        self.assertIsNone(self.store.find_product("A9"))
        self.store.merge_sort_products()
        self.assertEqual(self.store.find_product("A3").get_name(), "Headphones")
    

if __name__ == "__main__":
    unittest.main()





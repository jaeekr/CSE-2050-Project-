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
import unittest

class TestRecursionTotalPrice:
    def test_empty_list(self):
        self.assertEqual(recursive_total_price([]), 0.0)

    def test_multiple_products(self):
        products = [
            Product("P100", "Keyboard", 59.99),
            Product("P200", "Headphones", 39.99),
            Product("P300", "Mouse", 29.99),
        ]
        self.assertAlmostEqual(recursive_total_price(products), 129.97)

class TestFewestCoins(unittest.TestCase):
    """Tests for fewest_coins."""

    def test_amount_zero(self):
        self.assertEqual(fewest_coins([1, 5, 10], 0), 0)

    def test_exact_coin(self):
        self.assertEqual(fewest_coins([1, 5, 10], 10), 1)

    def test_combination_of_coins(self):
        self.assertEqual(fewest_coins([1, 5, 10], 12), 3)

    def test_larger_amount(self):
        self.assertEqual(fewest_coins([1, 5, 10, 25], 63), 6)


class TestStoreCatalogAndChange(unittest.TestCase):
    """Integration tests for the Store methods that call algorithms.py."""

    def setUp(self):
        self.store = Store()
        self.store.add_product(Product("P300", "Mouse", 29.99))
        self.store.add_product(Product("P100", "Keyboard", 59.99))
        self.store.add_product(Product("P200", "Headphones", 39.99))

    def test_calculate_change(self):
        self.assertEqual(self.store.calculate_change([1, 5, 10], 12), 3)
        self.assertEqual(self.store.calculate_change([1, 5, 10], 0), 0)

    def test_recursive_catalog_total(self):
        self.assertAlmostEqual(self.store.recursive_catalog_total(), 129.97)

    def test_recursive_catalog_total_empty_store(self):
        self.assertEqual(Store().recursive_catalog_total(), 0.0)


if __name__ == "__main__":
    unittest.main()

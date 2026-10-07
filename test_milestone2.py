import unittest

class TestShoppingCart(unittest.TestCase):
    def __init__(self):
        pass

class TestStore(unittest.TestCase):
    def __init__(self):
        pass


class TestNode(unittest.TestCase):
    def __init__(self):
        pass


class TestLinkedList(unittest.TestCase):
    def __init__(self):
        pass


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

        order1.set_status('PROCCESING')
        order2.set_status('COMPLETED')

        self.assertEqual(order1.get_status(), 'PROCCESING')
        self.assertEqual(order2.get_status(), 'COMPLETED')
        self.assertRaises(ValueError, order1.set_status, 'HELLO')


class TestStack(unittest.TestCase):
    def __init__(self):
        pass



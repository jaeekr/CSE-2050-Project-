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
    #all functions are acounted for as the other three are tested in each assert function after each other function occurs
    def test_init(self):
        my_stack = Stack()
        self.assertEqual(my_stack.size(), 0)
        self.assertIsNone(my_stack.peek())
        self.assertTrue(my_stack.is_empty())
    def test_stack_functions(self):
        #PUSH
        #one item tested first
        my_stack = Stack()
        my_stack.push('apple')
        self.assertEqual(my_stack.size(), 1)
        self.assertEqual(my_stack.peek(), 'apple')
        self.assertFalse(my_stack.is_empty())

        #POP TILL END
        my_stack.pop()
        self.assertEqual(my_stack.size(), 0)
        self.assertTrue(my_stack.is_empty())

        #push multiple items now
        my_stack.push('banana')
        my_stack.push(5)
        my_stack.push('even')
        self.assertEqual(my_stack.size(), 3)
        self.assertEqual(my_stack.peek(), 'even') #testing ordering
        self.assertFalse(my_stack.is_empty())

        #POP
        my_stack.pop()
        self.assertEqual(my_stack.size(), 2)
        self.assertEqual(my_stack.peek(), 5) #testing ordering
        self.assertFalse(my_stack.is_empty())

    def test_pop_empty_stack(self):
        my_stack = Stack()
        self.assertIsNone(my_stack.pop())
        self.assertEqual(my_stack.size(), 0)
        

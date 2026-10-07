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

        # test initialization of order objects with customer objects fully created as well as product objects fully created

        order1 = Order(1, customer1, list1)
        order2 = Order(2, customer2, list2)

        self.assertEqual(order1.order_id, 1)
        self.assertEqual(order1.customer, customer1)
        self.assertEqual(order1.purchased_items, list1)
        #  test initialization of both created order objects instance variables 
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

        # same order1 and order2 objects intialized but in this test being used to test the calculate_total method of price given in product initialization

        self.assertEqual(order1.calculate_total(), 15)
        self.assertEqual(order2.calculate_total(), 107)


    def test_get_status(self):
        # test initialization of order objects for get_status method
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
        # same initalization of order1 and order2 objects

        self.assertEqual(order1.get_status(), 'PENDING')
        # test setting and getting status of order objects
        order1.set_status('PROCCESING')
        order2.set_status('COMPLETED')
        # test that the status has been updated correctly
        self.assertEqual(order1.get_status(), 'PROCCESING')
        self.assertEqual(order2.get_status(), 'COMPLETED')
        # test that setting an invalid status raises a ValueError
        self.assertRaises(ValueError, order1.set_status, 'HELLO')

class TestOrderQueue(unittest.TestCase):
    def test_init(self):
        # test initialization of the order queue
        queue = OrderQueue()
        self.assertTrue(queue.is_empty())
        # test that the queue is initially empty and has size 0
        self.assertEqual(queue.size(), 0)
        # test that the queue is initially empty and has size 0

    def test_enqueue_dequeue(self):

        queue = OrderQueue()
        # initializes order queue object 

        self.assertTrue(queue.is_empty())
        queue.enqueue('item1')
        queue.enqueue('item2')
        queue.enqueue('item3')
        self.assertFalse(queue.is_empty())
        self.assertEqual(queue.size(), 3)
        # test that the queue size is correct after enqueuing items

        self.assertEqual(queue.dequeue(), 'item1')
        self.assertEqual(queue.size(), 2)
        self.assertEqual(queue.dequeue(), 'item2')
        self.assertEqual(queue.size(), 1)
        self.assertEqual(queue.dequeue(), 'item3')
        # test that the queue is empty after dequeuing all items
        self.assertTrue(queue.is_empty())
        # test that dequeuing from an empty queue returns None

        self.assertEqual(queue.dequeue(), None)
        # test that the queue size is correct after dequeuing all items

    def test_peek(self):

        queue = OrderQueue()
        self.assertEqual(queue.peek(), None)
        queue.enqueue('item1')
        queue.enqueue('item2')
        queue.enqueue('item3')
        self.assertEqual(queue.size(), 3)
        self.assertEqual(queue.peek(), 'item1')
        # test that peeking at the queue returns the correct item before dequeuing any
        queue.dequeue()
        self.assertEqual(queue.peek(), 'item2')
        # test that peeking at the queue returns the correct item after dequeuing one
        queue.dequeue()
        self.assertEqual(queue.peek(), 'item3')

        queue.dequeue()
        self.assertEqual(queue.peek(), None)
        # test that peeking at an empty queue returns None


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
        

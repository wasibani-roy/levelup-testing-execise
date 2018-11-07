import unittest
from check_order import check_order_status,\
    check_order_not_available,check_order_list
class TestOrders(unittest.TestCase):
    def test_order_status(self):
        self.assertTrue(check_order_status(order_id=2), True)
    def test_order_status_invalid_id(self):
        self.assertFalse(check_order_status(order_id=6), False)
    def test_order_status_id_not_exist_in_both(self):
        self.assertTrue(check_order_not_available(6), True)
    def test_order_list_is_empty(self):
        self.assertFalse(check_order_list(), False)

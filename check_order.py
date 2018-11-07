delivered = [1,2,34,100]
pending = []

def check_order_status(order_id):
    if order_id in delivered:
        return True
    else:
        return False

def check_order_not_available(order_id):
    if order_id not in delivered and order_id not in pending:
        return True
    else:
        return False

def check_order_list():
    if len(delivered) == 0:
        return True
    else:
        return False
def calculate_bill(item_cost, quantity, tax=0.05, discount=0):
    """
    Calculate total bill including tax and discount for items in a shopping cart
    Args:
        item_cost (float): Cost per item
        quantity (int): Number of items
        tax (float, optional): Tax rate as a decimal. Defaults to 0.05 (5%)
        discount (float, optional): Discount amount. Defaults to 0
    Returns:
        float: Total bill amount after tax and discount
    """
    total = (item_cost * quantity) + (item_cost * quantity * tax) - discount
    return total

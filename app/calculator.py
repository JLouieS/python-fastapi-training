def calculate_total(price: float, quantity: int, discount: float = 0) -> float:
    """
    Calculate the total price after applying discount.

    :param price: The price of a single item.
    :param quantity: The number of items.
    :param discount: The discount percentage to apply (default is 0).
    :return: The total price after discount.
    """
    if quantity < 0:
        raise ValueError("Quantity cannot be negative.")
    if price < 0:
        raise ValueError("Price cannot be negative.")
    if not (0 <= discount <= 100):
        raise ValueError("Discount must be between 0 and 100.")

    total = price * quantity
    total_after_discount = total * (1 - discount / 100)
    
    return total_after_discount

def get_grade(score: int) -> str:
    """
    Determine the letter grade based on the score.

    :param score: The score as an integer.
    :return: The letter grade as a string.
    """
    if not (0 <= score <= 100):
        raise ValueError("Score must be between 0 and 100.")

    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    elif score >= 60:
        return 'D'
    else:
        return 'F'

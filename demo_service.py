import math

def calculate_monthly_payment(principal: float, annual_rate: float, years: int) -> float:
    """
    Calculates the monthly mortgage payment.
    """
    monthly_rate = annual_rate / 100 / 12
    number_of_payments = years * 12
    
    if monthly_rate == 0:
        return principal / number_of_payments
        
    payment = principal * (monthly_rate * (1 + monthly_rate) ** number_of_payments) / \
              ((1 + monthly_rate) ** number_of_payments - 1)
    return round(payment, 2)

def validate_user_email(email: str) -> bool:
    """
    Checks if an email string is formatted correctly.
    Note: This is a basic demonstration helper.
    """
    if "@" in email and "." in email.split("@")[-1]:
        return True
    return False

def get_distance_between_points(x1, y1, x2, y2):
    # This function has no docstring, let's see if the AI can describe it!
    distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return distance
import math


# calculates a simple return value
def simple_return(price_old, price_new):

    # prevents divide by zero error
    if price_old <= 0:
        raise ValueError("price_old and price_new cannot be less than or equal to zero")

    return (price_new - price_old) / price_old

# calculates a log return value
def log_return(price_old, price_new):

    # prevents divide by zero error
    if (price_old <= 0) or (price_new <= 0):
        raise ValueError("price_old and price_new cannot be less than or equal to zero")

    return math.log(price_new / price_old)
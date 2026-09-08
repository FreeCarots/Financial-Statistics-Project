
# Calculates a simple return percentage
def simple_return(price_old, price_new):

    # Prevents Divide by Zero Error
    if price_old == 0:
        raise ValueError("price_old cannot be zero")

    return (price_new - price_old) / price_old


import returns

old_price = 100
new_price = 110

simple_return = returns.simple_return(old_price, new_price)

print(simple_return)


log_return = returns.log_return(old_price, new_price)

print(log_return)

old_error_price = -1
new_error_price = 0

error_return = returns.log_return           (old_error_price, new_error_price)

print(error_return)
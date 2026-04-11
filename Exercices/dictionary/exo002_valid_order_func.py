
# ## Order validity
# Write a function is_ordre_valid(order, stock) to check if all the products from an order are available.
# - The order is a list of tuple (product_id, quantity)
# - Stock is a dictionnary {product_id : quantity}
# - The fonction must return True of False

def is_ordre_valid(order, stock):
    s = True
    for i in order:
        product_id, quantity = i
        c = stock.get(product_id)
        if c < quantity:
            s = False
            break
    return s


order = [] 
stock = {}

print("check order : ", is_ordre_valid([(1,5),(5,200)], {1:500, 5:100}))

# **Note**: dictionary keys must match - int, str
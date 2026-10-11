products = [
       { 
         "name": "big_Yoggy soda",
         "price": 1000,
         "quantity": 67,
         "reorder_level": 14,
        },
        { 
          "name": "balls juice",
          "price": 250,
          "quantity": 50,
          "reorder_level": 22,
        },
        { 
          "name": "black soda",
          "price": 120,
          "quantity": 26,
          "reorder_level": 27,
        }
]
def check_stock(product):
        if product["quantity"] <=  product["reorder_level"]:
            print(f"low on stocks for {product['name']}")

        else:
            print(f"enough stocks for {product['name']}")

check_stock(products[0])

def sales(product,amount):
    if
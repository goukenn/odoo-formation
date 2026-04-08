def display_product(a_product):
    name = a_product['name']

    match a_product:
        case {"type": "électronique", "price": prix} if prix > 500:
            return f"{name} est un équipement électronique coûteux"
        case {"type": "électronique", "price": _}:
            return f"{name} est un électronique abordable"
        case {"type": "livre", "price": prix} if prix < 20:
            return f"{name} est un livre abordable"
        case {"type": "livre", "price": _}:
            return f"{name} est un livre coûteux"
        case _:
            return "Type de produit inconnu"


product = {"type": "électronique", "name": "Smartphone", "price": 800}
# Smartphone est un équipement électronique coûteux
print(display_product(product)) 
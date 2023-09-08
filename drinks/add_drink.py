from drinks.models import Drink

def add_drink(drink_name, drink_description):
    return Drink.objects.create(name=drink_name, description=drink_description)
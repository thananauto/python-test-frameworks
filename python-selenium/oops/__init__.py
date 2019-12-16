from oops.Encapsulation import Encapsulation
from oops.User import Office, Admin


def make_sound(animalType):
    animalType.programming();

# example for inheritance
if __name__ == '__main__':
    office = Office('kumar')
    office.print_user()
    make_sound(office);
    admin = Admin('Avengers')
    make_sound(admin)

# Examples for encapsulation and method overloading
if __name__ == '__main1__':

    enpacp = Encapsulation();

    enpacp.set_brand('Audi')
    enpacp.set_speed('')
    #enpacp.set_name('Peter')
    #enpacp.print_product()
    enpacp.print_name()
    #enpacp.__print_name_none() --> This method have throws error, since the method is private0
    enpacp.method_overloading("Frank")
    enpacp.method_overloading()
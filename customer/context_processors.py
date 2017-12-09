from .customer import Customer


def customer(request):
        return {'customer': Customer(request)}

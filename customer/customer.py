class Customer(object):
    def __init__(self, request):
        self.customer_id = 1

    def get_id(self):
        return self.customer_id
"""
        self.session = request.session
        customer = self.session.get(setting.CUSTOMER_SESSION_ID)
        if not customer:
            customer = self.session[self.CUSTOMER_SESSION_ID] = {}
        self.customer = customer
        customer_id = str(1)
        if customer_id not in self.customer:
            self.customer[customer_id] = {}
        self.session[setting.CUSTOMER_SESSION_ID] = self.customer

    def login(self, c_ID = 1):
        customer_id = str(c_ID)
        if customer_id not in self.customer:
            self.customer[customer_id] = {}
        self.save()

    def save(self):
        self.session[setting.CUSTOMER_SESSION_ID] = self.customer
        self.session.modified = True
"""

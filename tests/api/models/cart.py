class Cart:
    def __init__(self, json):
        self.json = json
        self.quantity_of_products = self.json['updatetopcartsectionhtml']
        self.additional_sucsess_status = self.json['success']

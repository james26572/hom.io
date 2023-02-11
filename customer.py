class Customer:
    name = ""
    college = ""
    accommodation_type = ""
    required_facilities = []
    maxPrice = float("-inf")
    def __init__(self,name,college,accommodation_type,required_facilities,max_price):
        self.name = name
        self.college = college
        self.accommodation_type = accommodation_type
        self.required_facilities = required_facilities
        self.maxPrice = max_price

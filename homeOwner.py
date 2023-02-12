class HomeOwner:
    name = None
    distanceFromTrinity = None
    distanceFromDCU = None
    distanceFromUCD = None
    nearby_facilities = set()
    min_price = None
    home_type = None
    email = None
    def __init__(self,name,trinDist,DCUDist,UCDDist,*facilities,minPrice,hometype,email):
        self.name = name
        self.distanceFromTrinity = trinDist
        self.distanceFromDCU = DCUDist
        self.distanceFromUCD = UCDDist
        self.nearby_facilities = set(list(facilities)[0])
        self.min_price = minPrice
        self.home_type = hometype
        self.email = email
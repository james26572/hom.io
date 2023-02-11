class HomeOwner:
    name = None
    distanceFromTrinity = None
    distanceFromDCU = None
    distanceFromUCD = None
    nearby_facilities = set()
    min_price = None
    home_type = None
    def __init__(self,name,trinDist,DCUDist,UCDDist,*facilities,minPrice,hometype):
        self.name = name
        self.distanceFromTrinity = trinDist
        self.distanceFromDCU = DCUDist
        self.distanceFromUCD = UCDDist
        self.nearby_facilities = set(list(facilities)[0])
        self.min_price = minPrice
        self.home_type = hometype
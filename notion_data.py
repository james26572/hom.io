from notion_client import Client
from customer import Customer
from homeOwner import HomeOwner


from basic_notion.query import Query
from basic_notion.page import NotionPage, NotionPageList
from basic_notion.field import SelectField, TitleField, MultiSelectField,NumberField

# First define models

class MyRow(NotionPage):
    name = TitleField(property_name='Name')
    college = SelectField(property_name='College')
    accomtype = SelectField(property_name='Accommodation Type')
    requiredFacilities = MultiSelectField(property_name="Desired Nearby Facilities")
    maxPrice = NumberField(property_name="Max Price")
    distanceFromTrinity = NumberField(property_name="Distance from Trinity")
    distanceFromDCU = NumberField(property_name="Distance from DCU")
    distanceFromUCD = NumberField(property_name="Distance from UCD")
    nearbyFacilities = MultiSelectField(property_name="Nearby Facilities")
    minPrice = NumberField(property_name="Min Price")
    acomType = MultiSelectField(property_name="Accommodation Type")
    # ... your other fields go here
    # See your database's schema and the available field classes
    # in basic_notion.field to define this correctly.

class MyData(NotionPageList[MyRow]):
    ITEM_CLS = MyRow

# You need to create an integration and get an API token from Notion:

DATABASE_IDCust = 'a576c60298d1445688b4ced4f6232c6c'
DATABASE_IDHome = 'c977a9d35b5c44ff8f147acdef5620bc'


# Now you can fetch the data

def get_data(token,database_id: str) -> MyData:
    client = Client(auth=token)
    data = client.databases.query(
        **Query(database_id=database_id).serialize()
    )
    return MyData(data=data)

'''
my_data = get_data(database_id=DATABASE_ID)
#print(my_data.items())
listOfCustomers = []
for row in my_data.items():
    
    name = row.name.get_text() if row.name.get_text() != "" else "N/A"
    
    #print(name)
    
    college = row.college.data['select']['name'] if row.college.data['select'] is not None else "N/A"
    #print(college)
    accommodation_type = row.accomtype.data['select']['name'] if row.accomtype.data['select'] is not None else "N/A"
    #print(accommodation_type)
    required_facilities = row.requiredFacilities.get_text()
    
    price_range = row.priceRange.data['select']['name'] if row.priceRange.data['select'] is not None else "N/A"
    currentCustomer = Customer(name,college,accommodation_type,required_facilities,required_facilities)
    listOfCustomers.append(currentCustomer)

# Do whatever else you may need to do
'''

def getCustomerInfo():
    NOTION_TOKEN = 'secret_SaD0zcwx1BUXZEMSncbWuMZt2vEJKA4Uw7iKvaCkYd1'
    my_data = get_data(token=NOTION_TOKEN,database_id=DATABASE_IDCust)
    listOfCustomers = []
    for row in my_data.items():
        name = row.name.get_text() if row.name.get_text() != "" else "N/A"
        college = row.college.data['select']['name'] if row.college.data['select'] is not None else "N/A"
        accommodation_type = row.accomtype.data['select']['name'] if row.accomtype.data['select'] is not None else "N/A"
        required_facilities = row.requiredFacilities.get_text()
        max_price = row.maxPrice.data['number'] if row.maxPrice.data['number'] is not None else float("-inf")
        
        currentCustomer = Customer(name,college,accommodation_type,required_facilities,max_price)
        listOfCustomers.append(currentCustomer)
    return listOfCustomers

def getHomeOwnerInfo():
    NOTION_TOKEN = "secret_x20riM1RHE0gWNsZWBGONxH9DwPfySmAh5ccjAXajkk"
    my_data = get_data(token = NOTION_TOKEN,database_id=DATABASE_IDHome)
    listOfHomeOwners = []
    for row in my_data.items():
        name = row.name.get_text() if row.name.get_text() != "" else "N/A"
        distFromTrinity = row.distanceFromTrinity.data['number'] if row.distanceFromTrinity.data['number'] is not None else float("inf")
        accomType = row.acomType.get_text()
        
        distanceFromDCU = row.distanceFromDCU.data['number'] if row.distanceFromDCU.data['number'] is not None else float("inf")
        distanceFromUCD = row.distanceFromUCD.data['number'] if row.distanceFromUCD.data['number'] is not None else float("inf")
        nearbyFacilities = row.nearbyFacilities.get_text()
        minPrice = row.minPrice.data['number'] if row.minPrice.data['number'] is not None else float("-inf")
        homeOwner = HomeOwner(name,distFromTrinity,distanceFromDCU,distanceFromUCD,nearbyFacilities,minPrice=minPrice,hometype=accomType)
        listOfHomeOwners.append(homeOwner)
    return listOfHomeOwners


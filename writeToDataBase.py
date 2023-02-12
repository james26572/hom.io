
DATABASE_ID = 'd2648772b9a2417ea4ef8c9a779c034a'
NOTION_KEY = 'secret_8uuXiCn5hDAmanyqGdq9xJzsL7fZUfBc9F33ZX8NMTm'

from notion_client import Client
notion = Client(auth=NOTION_KEY)
new_page = {
    "Student": {
        "title": [
            {
                "text": {
                    "content": "PLACEHOLDER"
                }
            }
        ]
    },
    "Homeowner Contact": {
        "rich_text": [
            {
                "text": {
                    "content": "PLACEHOLDER"
                }
            }
        ]
    }
}
#print(new_page['Student']['title'][0]['text']['content'])
#print(new_page["Homeowner Contact"]["rich_text"][0]["text"]["content"])


#notion.pages.create(parent={"database_id": DATABASE_ID}, properties=new_page)


def addAllocationToDataBase(new_page,studentName,homeOwnerEmail):
    if isinstance(homeOwnerEmail,list):
        homeOwnerEmail = " ".join(homeOwnerEmail)
    new_page['Student']['title'][0]['text']['content'] = studentName
    new_page["Homeowner Contact"]["rich_text"][0]["text"]["content"] = homeOwnerEmail
    notion.pages.create(parent={"database_id": DATABASE_ID}, properties=new_page)

'''
name = "james"
email = "hjakd"
addAllocationToDataBase(new_page=new_page,studentName=name,homeOwnerEmail=email)
'''
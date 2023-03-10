
from notion_data import getCustomerInfo, getHomeOwnerInfo
from writeToDataBase import addAllocationToDataBase,new_page



studentsInfo = getCustomerInfo()
homeOwnersInfo = getHomeOwnerInfo()


#homeOwnersInfo = sorted(homeOwnersInfo,key = lambda x: x.distanceFromTrinity)


def optimize(studentsInfo,homeOwnersInfo):
    pairings = {}
    for student in studentsInfo:
        pairings[student] = []
        college = student.college
        
        if college == "Trinity":
            homeOwnersInfo = sorted(homeOwnersInfo,key = lambda x:x.distanceFromTrinity)
        else:
             if college == "DCU":
                homeOwnersInfo = sorted(homeOwnersInfo,key = lambda x:x.distanceFromDCU)
             else :
                homeOwnersInfo = sorted(homeOwnersInfo,key = lambda x:x.distanceFromUCD)
        for home in homeOwnersInfo:
            if(home.min_price>student.maxPrice):
                continue
            if(home.home_type != student.accommodation_type):
                continue
            for facility in student.required_facilities:
                if facility not in home.nearby_facilities:
                    continue
            pairings[student].append(home.email)
        addAllocationToDataBase(new_page=new_page,studentName=student.name,homeOwnerEmail=pairings[student])
            
    return pairings


optimize(studentsInfo=studentsInfo,homeOwnersInfo=homeOwnersInfo)

'''
pairings = optimize(studentsInfo,homeOwnersInfo)
for idx,student in enumerate(studentsInfo):
    print("Optimal allocations for student ",student.name)
    if(len(pairings[student])==0):
        print("No optimal allocations")
    for housename in pairings[student]:
        print("House owner name ",housename)
    
'''


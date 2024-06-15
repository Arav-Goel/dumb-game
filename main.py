print("WELCOME TO FLAMES RELATIONSHIP TESTER!!!!!!!")
xname1 = input("1st name: ")
name1 = xname1.lower()
xname2 = input("2nd name: ")
name2 = xname2.lower()

file = open("store.txt", "w")  
# print(name1)
# print(name2)
list1 = []
list2 = []

for x in name1:
    list1.append(x)

for y in name2:
    list2.append(y)

for a in list1:
    if (a in list2):
        count1 = list1.count(a)
        for i in range(0, count1):
            list1.remove(a)
        count2 = list2.count(a)
        for u in range(0, count2):
            list2.remove(a)
    else:
        pass

# print(list1)
# print(list2)
fincount1 = int(len(list1))
fincount2 = int(len(list2))
finsum = fincount1 + fincount2

def divide(sts):
    check = True
    while (check==True):
        if (sts>6):
            sts = sts - 6
            pass
        else:
            check == False
            return sts

pq = divide(finsum)
# print(pq)
flame = {1:"Friends", 2:"Lovers", 3:"Affectionate", 4:"Marriage", 5:"Enemies", 6:"Sibling"}
m = flame.get(pq)
print(m)
# print(type(list1))
# print(type(list2))
file.write(xname1)
file.write(xname2)

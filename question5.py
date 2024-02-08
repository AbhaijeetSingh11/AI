d={1:"One",2:"Two",3:"Three",4:"Four",5:"Five"}
print(d)
d.update({6:"Six"})
print(d)
d.pop(2)
print(d)
# chec=d.get(1)
# if(chec != "None"):
#     print('not present')  
# else:
#     print("present")
print(d.__len__())
print(sum(d))
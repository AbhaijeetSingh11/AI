import random
list=[]
even=[]
odd=[]
primenumber=[]
for i in range(0,100):
    list.append(random.randint(100,900))
print('printing numbers in list:',list)
def find(list):
    for j in range(0,100):
        if((list[j]%2)==0):
            even.append(list[j])
        else:
            odd.append(list[j])
# calling function
find(list)


print('There are ',even.__len__(),' even numbers in list\n')
print('printing even numbers:',even)

print('\nThere are ',odd.__len__(),' odd numbers in list\n')
print('printing odd numbers:',odd)

# def prime(list):
#     for t in range(0,100):
#         for k in range(2,int((list[t]/2)+1)):
#             if(list[t]%k==0):
#                 primenumber.append(list[t])
#                 break
# prime(list)

# print('\nThere are ',primenumber.__len__(),' prime numbers in list\n')
# print('printing prime numbers:',primenumber)
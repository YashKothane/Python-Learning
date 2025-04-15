#  This is the program to write the code for stocks buy and sell
# So basically its the difference between the highest and smallest value

user_input=input("Enter the array").split()
user_lst=list(map(int,user_input))
print(user_lst)

temp=user_lst[0]
# [7 10 1 3 6 9 2]
# [ 11 10 3 12 ]
for i in range(0,len(user_lst)):
    if(user_lst[i]>temp):
        temp=user_lst[i]

print(f"the max element is{temp}")
# var=user_lst[0]
# for j in range(0, len(user_lst)):
#     if(user_lst[j]<var):
#         var=user_lst

# print(f"the smallest element is {var}")

#  So this approach was not correct because we first need to buy the stock and then sell the stock
#  SO lets consider the array as [ 7 10 1 3 6 9 2]
#  So here we need to buy at 7 and sell at 10 of buy at 10
#  and sell at 1 or 
# 
# but at 1 and sell at 3
profit=[]
max=0
for x in range(len(user_lst)):
    for y in range(x+1,len(user_lst)):
        
        demo=user_lst[y]-user_lst[x]
        if(max<demo):
            max=demo
    #     temp2.append(demo)
    
    # print[temp2]
    # zero=temp2[0]
    # for z in range(len(temp2)):
    #     if(zero<temp2[z]):
    #         zero=temp2[z]
    # profit.append(zero)
print(max)
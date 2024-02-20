# Countdown 
def count_down(number):
    tab = []
    for y in range(number, -1, -1):
        tab.append(y)
    return tab

print(count_down(5))  
# Print and Return
def Print_and_Return(a,b):
    print(a)
    return b
Print_and_Return(1,2)

# First Plus Length
def First_Plus_Length(list_number):
    
    sum=list_number[0]+len(list_number)
    return sum

result=First_Plus_Length([1,2,3,4,5])
print(result)

# Values Greater than Second 
new_list=[]
def Values_Greater_than_Second(list_number):
    if len(list_number) < 2 :
        return false
    else:
        for x in range(len(list_number)):
            if list_number[x] > list_number[1]:
                new_list.append(list_number[x])
        return new_list
result=Values_Greater_than_Second([5,2,3,2,1,4])
print(result)

# This Length, That Value
def This_Length_That_Value(a,b):
    new_list=[]
    for i in range(a):
        new_list.append(b)
    return new_list


result= This_Length_That_Value(6,2)
print(result)


arr=[3,3,4,2,4,4,2,4,4]
count={}
for num in arr:
    count[num]=count.get(num,0)+1
majority_element=None
for key,value in count.items():
    if value>len(arr)//2:
        majority_element=key
        break
print("Majority element:",majority_element)

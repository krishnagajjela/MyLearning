def twosum_hashmap(arr,sum):
    dict={}
    for i in range(len(arr)):
        if(sum - arr[i] in dict):
            return [sum-arr[i],arr[i]]
        elif(arr[i] not in dict):
            dict[arr[i]]=i


arr=[5,7,4,3,9,8,19,21]
sum=27
s=twosum_hashmap(arr,sum)
print(s)

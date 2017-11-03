#%%
import numpy as np

#%%
def BinarySearch(list,item):
    '''
    二分查找法
    '''
    low,high = 0,len(list)-1
    while(low <= high):
        mid = int((low+high)/2)
        if(item == list[mid]):
            return mid
        if(item > list[mid]):
            low = mid+1
        else:
            high = mid-1
    return None

list = [1,3,5,7,9]
print(BinarySearch(list,9))
print("最多需要多少步：",np.log2(len(list)))
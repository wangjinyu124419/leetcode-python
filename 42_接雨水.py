nums_list=[0,1,0,2,1,0,1,3,2,1,2,1]

#暴力循环法
def trap(nums_list):
    total=0
    for i in range(1,len(nums_list)-1):
        max1=max(nums_list[:i])
        max2=max(nums_list[i+1:])
        l_max=min(max1,max2)
        if l_max>nums_list[i]:
            total+=l_max-nums_list[i]
    return total

if __name__ == '__main__':
    res=trap(nums_list)
    print(res)

height=[0,1,0,2,1,0,1,3,2,1,2,1]

#暴力循环法
def trap(height):
    total=0
    for i in range(1,len(height)-1):
        max1=max(height[:i])
        max2=max(height[i+1:])
        l_max=min(max1,max2)
        if l_max>height[i]:
            total+=l_max-height[i]
    return total


#动态规划
def trap_dynamic(height):
    if not height:
        return 0
    left=[None]*len(height)
    right=[None]*len(height)
    left[0]=height[0]
    right[-1]=height[-1]
    for i in range(1,len(height)):
        left[i]=max(left[i-1],height[i])
    for i in range(len(height)-2,-1,-1):
        right[i]=max(right[i+1],height[i])
    total=0
    for i in range(1,len(height)-1):
        total+=min(left[i],right[i])-height[i]

    print(left)
    print(right)
    print(height)
    return total


#双指针
"""

left_max：左边的最大值，它是从左往右遍历找到的
right_max：右边的最大值，它是从右往左遍历找到的
left：从左往右处理的当前下标
right：从右往左处理的当前下标
定理一：在某个位置i处，它能存的水，取决于它左右两边的最大值中较小的一个。

定理二：当我们从左往右处理到left下标时，左边的最大值left_max对它而言是可信的，但right_max对它而言是不可信的。（见下图，由于中间状况未知，对于left下标而言，right_max未必就是它右边最大的值）

定理三：当我们从右往左处理到right下标时，右边的最大值right_max对它而言是可信的，但left_max对它而言是不可信的。
"""
def trap_point(height):
    left=0
    right=len(height)-1
    left_max=0
    right_max=0
    total=0
    while left<right:
        if height[left]<height[right]:
            if left_max>height[left]:
                total+=left_max-height[left]
            else:
                left_max=height[left]
            left+=1
        else:
            if right_max>height[right]:
                total+=right_max-height[right]
            else:
                right_max=height[right]
            right-=1
    return total
height=[0,1,0,2,1,0,1,3,2,1,2,1]


if __name__ == '__main__':
    # res=trap(height)
    # res=trap_dynamic(height)
    res=trap_point(height)
    print(res)

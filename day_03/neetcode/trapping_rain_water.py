def trapping_rain_water(height):
    if not height:
        return 0
    l, r=0, len(height)-1
    res=0
    leftmax, rightmax = height[l], height[r]
    while l<r:
        if leftmax<rightmax:
            l +=1
            leftmax=max(leftmax, height[l])
            res+=leftmax-height[l]
        else:
            r-=1
            rightmax=max(rightmax, height[r])
            res+=rightmax-height[r]
    return res


assert trapping_rain_water([0,2,0,3,1,0,1,3,2,1])==9
print("all test cases passed")
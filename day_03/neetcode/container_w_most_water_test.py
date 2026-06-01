def container_w_most_water(height):
    res=0
    l, r=0, len(height)-1

    while l<r:
        area = (r-l)*min(height[l], height[r])
        res= max(area, res)
        if height[l]<height[r]:
            l+=1
        else:
            r-=1
    return res

assert container_w_most_water([1,7,2,5,4,7,3,6]) ==36
print("all cases passed")

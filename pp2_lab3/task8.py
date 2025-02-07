def spy_game(nums):
    for i in range(len(nums)-2):
        if nums[i]==0:
            for j in range(i+1,len(nums)-1):
                if nums[j]==0:
                    for h in range(j+1,len(nums)):
                        if nums[h]==7:
                            return True
    return False
print(spy_game([0,0,7]))
print(spy_game([1,2,4,0,0,7,5])) 
print(spy_game([1,0,2,4,0,5,7]) )
print(spy_game([1,7,2,0,4,5,0]) )
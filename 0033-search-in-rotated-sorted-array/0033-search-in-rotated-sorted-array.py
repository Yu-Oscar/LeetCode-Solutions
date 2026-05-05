class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left < right:
            mid = (left + right) // 2

            print(left, right, mid, nums[left:right+1])
            if nums[mid] == target:
                return mid
            elif nums[mid] < nums[right]:
                print('# right sorted')               
                if nums[right] == target:
                    return right
                elif nums[mid] < target < nums[right]:
                    print('# between mid and right')  
                    left = mid + 1  
                else:                
                    print('# at left')                   
                    right = mid - 1
            else:                                       
                print('# left sorted')
                if nums[left] == target:
                    return left
                elif nums[left] < target < nums[mid]:  
                    print('# between left and mid')
                    right = mid - 1  
                else:                                  
                    print('# at right')
                    left = mid + 1

        if nums[left] == target:
            return left
        else:
            return -1
            
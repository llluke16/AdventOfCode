totalSafe = 0

def checkSafe(nums):
    trend = None
    for i in range(len(nums) - 1):
        if nums[i] == nums[i + 1] or abs(nums[i + 1] - nums[i]) >= 4:
            return False
        
        diff = nums[i + 1] - nums[i]

        if diff > 0:  # Increase
            if trend is None:
                trend = 'increase'
            elif trend == 'decrease':
                return False
        elif diff < 0:  # Decrease
            if trend is None:
                trend = 'decrease'
            elif trend == 'increase':
                return False
    return True

with open('2/data.txt') as f:
    for line in f:
        nums = [int(num) for num in line.split()]
        
        # Check if the row is safe without removing any element
        if checkSafe(nums):
            totalSafe += 1
            continue
        
        # Check if removing one element makes it safe
        row_safe = False
        for i in range(len(nums)):
            fixedRow = nums[:i] + nums[i+1:]  # Create a new row by removing the i-th element
            if checkSafe(fixedRow):
                row_safe = True
                break
        
        if row_safe:
            totalSafe += 1

print(totalSafe)
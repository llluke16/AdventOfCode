
totalSafe = 0

with open('2/data.txt') as f:
    for line in f:
        nums = [int(num) for num in line.split()]
        
        row_safe = True
        trend = None
        
        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1] or abs(nums[i + 1] - nums[i]) >= 4:
                row_safe = False
                break
            
            diff = nums[i + 1] - nums[i]

            if diff > 0:  # Increase
                if trend is None:
                    trend = 'increase'
                elif trend == 'decrease':
                    row_safe = False
                    break
            elif diff < 0:  # Decrease
                if trend is None:
                    trend = 'decrease'
                elif trend == 'increase':
                    row_safe = False
                    break
        
        if row_safe:
            totalSafe += 1

print(totalSafe)
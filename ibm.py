def getNumPairs(arr, l, r):
    n = len(arr)
    count = 0
    
    # Sorting the array for efficient pair finding
    arr.sort()
    
    # Initializing left and right pointers
    left = 0
    right = n - 1
    
    # Loop until left pointer crosses the right pointer
    while left < right:
        # If the sum of elements at left and right indices is within the range [l, r]
        if arr[left] + arr[right] >= l and arr[left] + arr[right] <= r:
            # Count the number of pairs
            count += right - left
            # Move the left pointer to the right
            left += 1
        else:
            # If the sum is less than the lower bound, move left pointer to the right
            if arr[left] + arr[right] < l:
                left += 1
            # If the sum is greater than the upper bound, move right pointer to the left
            else:
                right -= 1
    
    return count

# Example usage
arr = [2, 3, 4, 5]
l = 5
r = 7
print(getNumPairs(arr, l, r))  # Output: 4



def kthOccurrence(X, arr, query_values):
    result = []
    for q in query_values:
        count = 0
        found = False
        for i, num in enumerate(arr):
            if num == X:
                count += 1
                if count == q:
                    result.append(i + 1)
                    found = True
                    break
        if not found:
            result.append(-1)
    return result

# Example usage:
arr = [1, 2, 20, 8, 8, 1, 2, 5, 8, 0]
X = 8
query_values = [100353, 4, 2]

print(kthOccurrence(X, arr, query_values))

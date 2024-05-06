import math

def smallest_subarray_with_given_sum(S, arr):
    windowSum = 0 # starting sum
    minLength = math.inf
    windowStart = 0

    # Creates the sum of the array elements by index
    for windowEnd in range(0, len(arr)):
        windowSum += arr[windowEnd] 
        # print(windowSum)

    while windowSum >= S:
        minLength = min(minLength, windowEnd - windowStart + 1)
        windowSum -= arr[windowStart]
        windowStart += 1
    if minLength == math.inf:
        return 0
    return minLength
        
   

def main():
    print("Smallest subarray length: " + str(smallest_subarray_with_given_sum(7, [2, 1, 5, 2, 3, 2])))
    print("Smallest subarray length: " + str(smallest_subarray_with_given_sum(7, [2, 1, 5, 2, 8])))
    print("Smallest subarray length: " + str(smallest_subarray_with_given_sum(8, [3, 4, 1, 1, 6])))
    

main()
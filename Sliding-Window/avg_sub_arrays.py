def find_svg_subarrays (K, arr):
    result = [] # stores the final result
    windowSum = 0.0 # starting sum
    windowStart = 0 # starting arr index

    for windowEnd in range(len(arr)):
        windowSum += arr[windowEnd] # adds the next elements and puts in the WindowSum
        
        # slide the window, we don't need to slide if we've not hit the required window size of 'k'
        if windowEnd >= K - 1:
            result.append(windowSum / K) # This does the averaging of the K length window
            windowSum -= arr[windowStart] # subtracts from the front of the array
            windowStart += 1 # Now windowStart begins at the next element from 0, then 1, then 2 etc.
            
    return result
    

def main():
    result = find_svg_subarrays(5, [1, 3, 2, 6, -1, 4, 1, 8, 2])
    print("averages of subarrays of size K: " + str(result))

main()


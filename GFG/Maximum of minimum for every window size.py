#User function Template for python3

class Solution:
    
    #Function to find maximum of minimums of every window size.
 def maxOfMin(self,arr,n):
    # code here
    left_array = [-1] * n
    right_array = [n] * n
    
    # Create stacks to store indices of elements in the array.
    stack = []
    
    # Calculate the previous smaller element for each element in the array.
    for i in range(n):
        while stack and arr[stack[-1]] >= arr[i]:
            stack.pop()
        if stack:
            left_array[i] = stack[-1]
        stack.append(i)
    
    # Clear the stack for the next round.
    stack = []
    
    # Calculate the next smaller element for each element in the array.
    for i in range(n-1, -1, -1):
        while stack and arr[stack[-1]] >= arr[i]:
            stack.pop()
        if stack:
            right_array[i] = stack[-1]
        stack.append(i)
    
    # Initialize the result array with zeros.
    result = [0] * (n + 1)
    
    # Calculate the maximum of the minimums for each window size.
    for i in range(n):
        window_size = right_array[i] - left_array[i] - 1
        result[window_size] = max(result[window_size], arr[i])
    
    # Fill in the gaps in the result array with larger values.
    for i in range(n-1, 0, -1):
        result[i] = max(result[i], result[i+1])
    
    # Return the final result array.
    return result[1:]

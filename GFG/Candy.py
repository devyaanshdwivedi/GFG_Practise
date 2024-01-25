#User function Template for python3

class Solution:
    #def minCandy(self, N, ratings):
        # Code here
        
    def minCandy(self, N, ratings):
      n = len(ratings)
      # Initialize candies array with 1 for each child
      candies = [1] * n
    
      # Left-to-Right pass: assign candies based on increasing ratings
      for i in range(1, n):
        if ratings[i] > ratings[i-1]:
          candies[i] = candies[i-1] + 1
    
      # Right-to-Left pass: adjust candies based on decreasing ratings
      for i in range(n-2, -1, -1):
        if ratings[i] > ratings[i+1]:
          candies[i] = max(candies[i], candies[i+1] + 1)
    
      # Return the sum of candies for all children
      return sum(candies)
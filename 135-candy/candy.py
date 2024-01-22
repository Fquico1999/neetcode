"""
Difficulty: Hard
There are n children standing in a line.
Each child is assigned a rating value given in the integer array ratings.
You are giving candies to these children subjected to the following requirements:
- Each child must have at least one candy.
- Children with a higher rating get more candies than their neighbors.
Return the minimum number of candies you need to have to distribute the candies to the children.
"""

class Solution(): #pylint: disable=too-few-public-methods
    """
    Solution class
    """
    def candy(self, ratings)->int:
        """
        Two pass implementation. The forward pass, O(n) ensures that increasing ratings
        are handeled properly, whereas the backward pass, O(n), corrects for earlier
        ratings and the forward pass not having full context.
        """

        # At least there will be len(ratings) candies
        num_candies = len(ratings)
        candies = [1]*num_candies

        l = 0
        while l < len(ratings)-1:
            if ratings[l+1] < ratings[l] and candies[l] <= candies[l+1]:
                candies[l]+=1
            elif ratings[l+1] > ratings[l]:
                candies[l+1] = candies[l]+1
            l+=1

        # Reverse pass
        l = len(ratings)-1
        while l > 0:
            if ratings[l-1] < ratings[l] and candies[l] <= candies[l-1]:
                candies[l]+=1
            elif ratings[l-1] > ratings[l] and candies[l-1] <= candies[l]:
                candies[l-1] = candies[l]+1
            l-=1

        return sum(candies)

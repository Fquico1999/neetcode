"""
Difficulty: Medium

There are n gas stations along a circular route, where the amount of gas
at the ith station is gas[i]. You have a car with an unlimited gas tank
and it costs cost[i] of gas to travel from the ith station to its next
(i + 1)th station. You begin the journey with an empty tank at one of
the gas stations. Given two integer arrays gas and cost, return the
starting gas station's index if you can travel around the circuit once
in the clockwise direction, otherwise return -1.
If there exists a solution, it is guaranteed to be unique
"""

class Solution: # pylint: disable=too-few-public-methods
    """
    Solution Class
    """
    def can_complete_circuit_brute(self, gas, cost)-> int:
        """
        Brute force approach. Iterate through gas list and check if we can reach the end.
        O(n^2) time complexity because we check for each index.
        """

        def can_complete_given_index(idx)->bool:
            """
            Helper function to check if circuit can be completed with a given starting idx.
            O(n) time complexity.
            """
            i = 0
            tank = 0
            while i < len(gas):
                tank += gas[(idx+i)%len(gas)] - cost[(idx+i)%len(gas)]
                if tank < 0:
                    return False
                i+=1
            return True

        for i in range(len(gas)):
            if can_complete_given_index(i):
                return i

        return -1

    def can_complete_circuit_window(self, gas, cost)->int:
        """
        Pointer/window method. Essentially increase window size until we go bust.
        Set the left pointer to the right one and try again.
        """

        # Compute difference array
        diff = [gas[i] - cost[i] for i in range(len(gas))]

        l = 0
        r = 0
        c = 0
        while l < len(diff):
            if r == (l-1)%len(diff):
                if c+diff[r] >= 0:
                    return l

                l+=1
                r=l
                c=0
            else:
                if diff[l] < 0:
                    l+=1
                    r+=1
                else:
                    c += diff[r]
                    if c >= 0:
                        r+=1
                    else:
                        # We can skip some if r hasnt reached the end of the diff
                        # otherwise, increase l by 1.
                        l = max(r, l+1)
                        r = l
                        c = 0
                # Adjust r to ensure it wraps around.
                r = r % len(diff)
        return -1

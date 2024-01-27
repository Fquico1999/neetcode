"""
Difficulty: Hard

Given an array of strings words and a width maxWidth, 
format the text such that each line has exactly maxWidth 
characters and is fully (left and right) justified.

You should pack your words in a greedy approach;
that is, pack as many words as you can in each line.
Pad extra spaces ' ' when necessary so that each line has exactly maxWidth characters.

Extra spaces between words should be distributed as evenly as possible.
If the number of spaces on a line does not divide evenly between words,
the empty slots on the left will be assigned more spaces than the slots on the right.

For the last line of text, it should be left-justified,
and no extra space is inserted between words.

Note:

A word is defined as a character sequence consisting of non-space characters only.
Each word's length is guaranteed to be greater than 0 and not exceed maxWidth.
The input array words contains at least one word.
"""

class Solution(): #pylint: disable=too-few-public-methods
    """
    Solution class
    """

    def full_justify(self, words, max_width):
        """
        Implementation that does two passes over the words list. First pass is meant to
        seperate words into an array of strings trying to be greedy. O(n) time.
        The second pass is to compute how many additional spaces are needed, 
        and then add those between the words. O(n) as well ( loop over the array)
        and then each item in the array for a total of n.
        O(2n) - O(3n) space complexity to create string array, length array, and
        spaces array.
        """

        # Start by choosing putting words into strings,
        # And splitting off when close to max_width
        str_arr = [""]
        str_lens = [[]]
        for word in words:
            if len(str_arr[-1]) + len(word) > max_width:
                # Remove last trailing space
                str_arr[-1]=str_arr[-1][:-1]
                str_arr.append(word+" ")
                str_lens.append([len(word)])
            else:
                str_arr[-1]+=word+" "
                str_lens[-1].append(len(word))

        # Ensure the last string doesn't have an extra whitespace
        str_arr[-1] = str_arr[-1][:max_width]
        # Next, iterate over the array, and adjust until max_width is reached
        for i, string in enumerate(str_arr):
            # Fully left justify the last entry or single word
            if i == len(str_arr)-1 or len(str_lens[i]) == 1:
                while len(str_arr[i]) < max_width:
                    str_arr[i]+=" "
            elif len(string) < max_width:
                # Find how many spaces we can evenly add between all words
                delta =  (max_width - len(string)) // (len(str_lens[i])-1)
                remainder = (max_width - len(string)) % (len(str_lens[i])-1)
                # Create array to store number of spaces to add to each interval
                spaces = [delta]*(len(str_lens[i])-1)
                # Loop over spaces and add remainder from left to right.
                idx = 0
                while remainder > 0:
                    if idx == len(spaces):
                        idx = 0
                    spaces[idx]+=1
                    idx+=1
                    remainder-=1
                # Iterate over the number of intervals and add spaces
                idx = 0
                for j in range(len(str_lens[i])-1):
                    str_arr[i] = str_arr[i][:idx+str_lens[i][j]]+ \
                        " "*spaces[j] + str_arr[i][idx+str_lens[i][j]:]
                    idx+=str_lens[i][j]+spaces[j]+1

        return str_arr

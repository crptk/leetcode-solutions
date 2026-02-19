class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        output = [0] * len(temperatures)
        for i in range(len(temperatures)):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                index = stack.pop()
                output[index] = i - index
            stack.append(i)
        return output

'''
Calculating the distance would mean calculating the index,
we know that we have to keep track of index, and we know that 
we have to have O(n) time complexity, which means that hashmap,
two pointers, etc, is out of the question

We have to think outside the box, and say "Well if we are iterating,
and we have to find one that is greater than the previous, then 
the moment we run into one that is greater than the previous, then there's
more than enough possibility that the one previous to it is greater,
so we can keep "popping" the indexes until we reach the conclusion. This is kind
of the intuition of the stack
'''
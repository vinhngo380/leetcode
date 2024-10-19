class Solution:
    def occurrencesOfElement(self, nums: List[int], queries: List[int], x: int) -> List[int]:
        occur = dict()
        c = 1
        for i in range(len(nums)):
            if nums[i] == x:
                occur[c] = i
                c += 1
                
        res = []
        for q in queries:
            if occur.get(q,None) != None:
                res.append(occur[q])
            else:
                res.append(-1)
        return res

  '''
  TLDR: Use hashmap! Store each occurrence as a key (using a counter variable) with the index as its value. Then use another loop to iter through queries.

  TC O(n)
  SC O(n)
  '''

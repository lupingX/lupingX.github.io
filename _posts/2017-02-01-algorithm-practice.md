---
title: Algorithm practice?
---

<p class="lead"> <a href="http://jekyllrb.com">Some program for interest</a> Here is a collection of my personal code</p>

From [the project's readme](https://github.com/jekyll/jekyll/blob/master/README.markdown):

> Have fun and keep hungry

## **Two Sum**
>Given an array of integers, return indices of the two numbers such that they add up to a specific target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
*Example*:
```python
Given nums = [2, 7, 11, 15], target = 9,
Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
```
Below is a O(n^2) solution which is also my first thought.
```python
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if target==nums[i]+nums[j]:
                    return [i,j]
```
Then how can we solve this problem with less time?-- if we can store something then
check it later(ex:dic)
Below is another solution using O(N) complexity:
```python
        if len(nums) <= 1:
            return False
        dict = {}
        for i in range(len(nums)):
            if nums[i] in dict:
                return [dict[nums[i]], i]
            else:
                dict[target - nums[i]] = i
```




---
title: Algorithm practice?
---

<p class="lead">Here is a collection of my personal code when practice algorithm at Leetcode</p>

From [the project's readme](https://github.com/jekyll/jekyll/blob/master/README.markdown):

> Have fun and keep going

**Two Sum**
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

**3Sum**
>Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0? Find all *unique triplets* in the array which gives the sum of zero.
Note: The solution set must not contain duplicate triplets.
```python
For example, given array S = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
```
So the solution should be like:
```python
1. sorted the list, then use small median large to point the list.
2. loop the small until >1 or end, then loop the large and left until they meet (use condition-if mid+large+small>0 then large left move, or mid right move-to check )
3. Then the complexity should be O(N^2).
--Optimization: maybe use binary search in the second loop, then the complexity should be O(NlogN)
```
But here I have 2 submission error:
<br>1. is not consider when find right answer- should jump out the loop
<br>2. is not consider when duplicate at first loop
```python
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums = sorted(nums)
        result = []
        for small in range(len(nums) - 2):
            if not (small > 0 and nums[small] == nums[small - 1]):
                if nums[small] <= 0:
                    mid = small + 1
                    large = len(nums) - 1
                    while mid < large:
                        temp = nums[small] + nums[mid] + nums[large]
                        if temp == 0:
                            if nums[mid]>nums[mid-1] or mid-1==small:
                                result += [[nums[small], nums[mid], nums[large]]]
                                mid+=1
                                large-=1
                            else:
                                mid+=1
                        elif temp > 0:
                            large -= 1
                        else:
                            mid += 1
        return result
```

**3SumClosest**
>Given an array S of n integers, find three integers in S such that the sum is closest to a given number, target. Return the sum of the three integers. You may assume that each input would have exactly one solution.

```python
    For example, given array S = {-1 2 1 -4}, and target = 1.
    The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
```

```python
1. use while loop to do the first loop.
2. follow the above algorithm and just modify some small part. And the complexity should be O(N^2)
3. And at this particular question, we can't optimize it using binary search cause we need to travel through to get the closest.
```

code:
```python
    def threeSumClosest(self, nums, target):

        nums = sorted(nums)
        result = nums[0] + nums[1] + nums[2]#iniliazation
        small=0
        while small<len(nums)-2:

                    mid = small + 1
                    large = len(nums) - 1
                    while mid < large:
                        temp = nums[small] + nums[mid] + nums[large]
                        if abs(target-temp) <= abs(target-result):
                            result=temp
                            if target>temp:
                                mid += 1
                            elif target<temp:
                                large-=1
                            else:
                                small=len(nums)
                                break
                        elif result < temp:
                            large -= 1
                        else:
                            mid += 1
                    small+=1
        return result

```

**Add Two Numbers**
>You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.
```python
You may assume the two numbers do not contain any leading zero, except the number 0 itself.
Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
```
algorithm thought:
```python
1. we need a new link to store the sum and also a number to store the add-on.
2. need to consider when the 2 links are not same length.
```
code:
```python
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        p1 = l1
        p2 = l2
        addon = 0
        l3 = ListNode((p1.val + p2.val+addon) % 10)
        p=l3
        addon=(p1.val + p2.val)//10
        while p1.next or p2.next:
            if p1.next:
                val1=p1.next.val
                p1=p1.next
            else:
                val1=0
            if p2.next:
                val2=p2.next.val
                p2=p2.next
            else:
                val2=0
            p3 = ListNode((val1+val2+addon) % 10)
            addon = (val1+val2+addon) // 10
            p.next=p3
            p=p.next
        if addon:
            p.next=ListNode(addon)
        return l3
```
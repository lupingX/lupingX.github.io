---
title: Algorithm practice?
---

<p class="lead">Here is a collection of my personal code when practice algorithm at Leetcode</p>

List:
<br>[**Two Sum[E]**](#Two Sum)
<br>[**3Sum[M]**](#3Sum)
<br>[**3SumClosest[M]**](#3SumClosest)
<br>[**Longest Substring Without Repeating Characters[M]**](#Longest Substring Without Repeating Characters)
<br>[**Median of Two Sorted Arrays[H]**](#Median of Two Sorted Arrays)
> Have fun and keep going

<a name="Two Sum"></a>
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

<a name="3Sum"></a>
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

<a name="3SumClosest"></a>
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

<a name="Add Two Numbers"></a>
**Add Two Numbers**
>You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.
```python
You may assume the two numbers do not contain any leading zero, except the number 0 itself.
Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
```
pseudocode::
* iniliaze p1 and p2 to l1 and l2
* inilize addon to be zero
* loop until p1 and p2 to the end:
    * d1=p1.val if p1 else 0, same with p2
    * keep the sum of p1 p2 and addon
    * create a new node to keep (p1.val+p2.val+addon)%10
    * and reflush addon = (p1.val+p2.val+addon)//10
* create a brand new node if addon not zero
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

<a name="Longest Substring Without Repeating Characters"></a>
**Longest Substring Without Repeating Characters**
>Given a string, find the length of the longest substring without repeating characters.
```python
Given "abcabcbb", the answer is "abc", which the length is 3.
Given "bbbbb", the answer is "b", with the length of 1.
Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
```

pseudocode::
* initilize result=1 temp=1 and input string s
* loop s from currentIndex=0 until end:
    * temp+=1 if s[currentIndex] not in s(currentIndex-temp,currentIndex) else temp=0
    * result =temp if reuslt>temp
submission error:
<br>1. didn't consider the condition input='' so make change to reuslt and temp
<br>2. and this idea is not right when reset, so i need to change it at the else part: (1) find the duplicate part at index. (2) change the temp to temp=currentIndex-index
>finish and complexity is O(N) acceptable

code:
```python
        result=0
        temp=0
        for currentIndex in range(len(s)):
            if s[currentIndex] not in s[currentIndex-temp:currentIndex]:
                temp+=1
            else:
                index=s.find(s[currentIndex],currentIndex-temp,currentIndex)
                temp=currentIndex-index
            if temp>result:
                result=temp
        return result
```


<a name="Median of Two Sorted Arrays"></a>
**Median of Two Sorted Arrays**
>There are two sorted arrays nums1 and nums2 of size m and n respectively.
Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).
```python
nums1 = [1, 3]
nums2 = [2]
The median is 2.0
nums1 = [1, 2]
nums2 = [3, 4]
The median is (2 + 3)/2 = 2.5
```

thought::
* the idea should be combine 2 sorted array to one sorted array
* MIT course- merge sort, the complexity should be NlogN, whihc is more than requirement
* The difference is that we don't need a sorted array- but the k-th number.
* [divide and conquer](https://hk029.gitbooks.io/leetbook/content/%E5%88%86%E6%B2%BB/004.%20Median%20of%20Two%20Sorted%20Arrays[H]/004.%20Median%20of%20Two%20Sorted%20Arrays[H].html)

pseudocode:: input(nums1, nums2) both list
* find the shortest L1 then do binary search: C1=len(L1)/2 C2=K-C1 initilize
    - until L1.left<L2.right and L2.left<L1.right
    - if L1.left>L2.left move right

```python
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        if len(nums1)<=len(nums2):
            l1=nums1
            l2=nums2
        else:
            l1=nums1
            l2=nums2#make sure l1 shortest
        C1=len(L1)-1

```
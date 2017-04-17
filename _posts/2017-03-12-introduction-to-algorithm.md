---
title: Introduction-to-Algorithm?
---

<p class="lead"> <a href="https://lupingx.github.io/algorithm-MIT/">Algorithm</a> is so important that I use this link to record what I have learned from MIT open course and
the implementation code for specific algorithm.</p>

If you have any question or issue, contact me.

> This is only a immature practice, I just want to this this method to push me recording my study.

Please visit the detail [visiting the project on GitHub](https://lupingx.github.io/algorithm-MIT/).

**Lecture 1: Analysis of Algorithm**
><br>Insertion sort
<br>Asymptotic analysis
<br>Merge sort
<br>Recurrences

Insert sort:insort in the right place and move others to the right

pseudocode for insertion sort:
```python
for index1 in range(1,len(input)):
	index2=index1-1
	let key=input(index1)
	while input(index2)>input(index1) and index2>=0:
			input(index2+1)=input(index2)
			index2-=1
	input(index2+1)=key
```
>Complexity is O(N^2)

Merge sort: divide the input into 2 array, Recursively sort A[1...N/2] A[N/2...N] then Merge:
pseudocode for how to merge:(input is A and B, both sorted)
```python
	def Merge(A,B):
		Result=[]
		index_A=0
		index_B=0
		while index_A<len(A) or index_B<len(B):
			if index_B<len(B) and index_A<len(A):
				Result.append(A(index_A++) if A(index_A)>B(index_B) else B(index_B))
				elif index_B<len(B)
				index++
				else ...
```

This example is for using recurrences analysis:
T(N)=2*T(N/2)+CN
marster theory: so the complexity should be O(NlogN)
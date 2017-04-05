---
title: Algorithms-in-Python?
---

<p class="lead"> From this book, I want to practice algorithm by using Python. I will record all the necessary tips about python and keep the code</p>
[Algorithm in python](https://lupingX.github.io/materials/algorithms-in-python.pdf).

>This book is very useful and I strongly recommand this to practice your code.

## Chapter one: **Python Primer**
>[1] bool int float tuple str are **immutable** which means they can't be changed at the id place.
<br>[2] The difference of tuple and list(mutable vs immutable)
<br>[3] Raise error=> try: except: finally: syntax
<br>[4] How do iterator and generators(**yield**) work
<br>[5]**Set**->like hash table:{'red','green',1}; **dict** class->(key value):{'ga':'Irish','xx':'xxx'}
<br>[6]**is**->same identity; a is b:true if a and b are alias for the same object.=== **is not**. **//** integer division. **in** containment check. **del d[key]**: remove key and
its  associated value from dictionary.
<br>[7]if beta is list: (beta+=[4,5]:extends the original list with 2 more elements; beta=beta+[6,7]: reassign beta to a new list [xxx,6,7]  )
<br>Some **build-in** function:
isinstance(obj,cls):determine if obj is an instance of the class(or subclass)
<br>[8]**File**: fp=open('xxx.dat','w')#'w','r','a'

<br>this chapter is basically as a refence or handbook for me. If anything confused me, then turn back and have a look at this chapter.

## Chapter two: **Object-oriented Programming**
>[1]**unit test**: if \_\_name__=='\_\_main\_\_':
<br>[2]Operator overloading: a+b is converted to a method call on object a of the form, a.\_\_add\_\_(b) Alternatively b.\_\_radd(a)
can let the new class use the existing class.
<br>[3]iter(a) can be geneated automatically by def len and getitem
<br>[4]\_\_init\_\_: constructor
<br>[5]**Inheritance**: how?-> class xxx(xparents): use? super().\_\_init\_\_(xxxxx)
<br>[6]shallow copy and deep copy: if a=b(type:list):means create a new allias, no new list created; a=list(b): shallow copy=>new ref list created
but not the content. By using the copy module, we can do a deep copy, then a totally new content created: a= copy.deepcopy(b) 
[practice code](https://lupingX.github.io/materials/algorithm-in-python/chat2_test.py). 

This chapter is mainly about OOP, and how to do it in python. Understand it and do practice is the core.

## Chapter three: **Algorithm Analysis**
>ignoring this chapter-mainly about how to compare two algorithm. Big-O notation(see Introduction to Algorithm blog)

## Chapter four: **Recursion**
>learned and this book is about example:
[practice code](https://lupingX.github.io/materials/algorithm-in-python/char4_disk_usage.py).

## Chapter five: **Array-Based Sequences**
>[1]**list**,**tuple**,**str**->sequence and each uses a low-level concept known as an *array* to represent the sequcen.
[2]*array*: **Referential Array**->list:save the ref not the actual contents. And because Int of float or string..are immutable, so a[3]=3 only change the ref, not the exact num.
And tuple also save the ref, but can't change the ref. u can do append at tuple class..
**Compact array**->str: save the exact number by using Unicode international character set.->which is really great for saving a lot of RAM.
[3]64-bit computer means: every memory address using 64bits(8Byte), and Unicode set use 2 byte for saving.
[4]**Dynamic Array**:->append: create a greater capacity than the actual used. If then you have used all the capacity then create a new and larger list. copy the original list
to the new list then append sth and the old list is no longer needed.
[5]**insertation sort**: insert into the kth place then shift everything to the right.
[practice code](https://lupingX.github.io/materials/algorithm-in-python/char5_array.py).
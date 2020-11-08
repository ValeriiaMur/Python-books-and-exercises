# Part 1: Why is it So Important to Sort Data?

## We're Always Searching
Users do not have patience for slow apps. And rightfully so! While a a big reason why the applications we use now-a-days are so fast is due to the improvements made in hardware over the last few decades, the software developer still has an important role to play in keeping everything moving quickly.

As we write our applications, we should always be mindful of what operations are being done frequently, since optimizing these will have the biggest impact on the efficiency of our overall application. And regardless of *what* type of app you are creating, it is likely that one of the operations you will be relying on is ***searching***. We search for songs to add to a playlist, videos to watch, people we need to talk to and so much more. Because of this, it is essential that we optimize our searches.

## Linear vs. Binary Search
There are two common searching algorithms that developers are often introduced to when they are writing some of their first apps: **linear search** and **binary search**. Let's walk through the differences between them.

### Linear (Sequential) Search

Sometimes referred to as sequential search, this algorithm is fairly straightforward. Given a set of data, traverse the dataset one item at a time until either you find the item you are looking for OR check every item in the set and verify the item you are looking for is not there.

### Binary Search

The process of performing a binary search has a couple of extra steps. First, there is a *precondition* that the set of data you are searching is ***already sorted*** (alphabetically, numerically, etc). Then, the steps to search are:

1. Compare the item in the middle of the data set to the item we are searching for.
    - If it is the same, stop. We found it and are done!
    - Else, if the item we are searching for is LESS than the item in the middle:
        - Eliminate the RHS of list. Repeat step 1 with only the LHS of list.
    - Else, the item we are searching for is GREATER than the item in the middle:
        - Eliminate the LHS of list. Repeat step 1 with only the RHS of the list.


A visualization comparing these two algorithms is shown below.
![binary v sequential](https://www.mathwarehouse.com/programming/images/binary-vs-linear-search/binary-and-linear-search-animations.gif "Binary v Sequential Search")

### Your Task 
- Complete all of the functions in the `searching.py` file.

### Runtimes

These two searching strategies have very different runtimes.

**Linear Search:** O(n)  
**Binary Search:** O(log(n))

Looking at the above runtimes, it is clear that we should be using binary search over linear search. 
***However, we cannot perform binary search if our data isn't ALREADY SORTED!***

While the justification for *WHY* we want to sort our data is pretty clear, a harder question to answer is *HOW* do we want to sort our data. Over the next few days, we will explore several different sorting algorithms, examining the pros and cons of each.

[Just for fun...(VIDEO) 15 Sorting Algorithms in 6 Minutes  ![alt text](https://i.ytimg.com/vi/kPRA0W1kECg/maxresdefault.jpg)](https://www.youtube.com/watch?v=kPRA0W1kECg)
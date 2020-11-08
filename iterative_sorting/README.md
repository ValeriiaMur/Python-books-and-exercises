# Iterative Sorting Algorithms

## Bubble Sort

In **Bubble Sort**, we make a series of swaps between adjacent elements, gradually moving larger elements towards the end of the array (or _bubbling_ larger elements up).

### Algorithm

1. Loop through your array
    - Compare each element to its neighbor
    - If elements in wrong position (relative to each other, swap them)
2. If no swaps performed, stop. Else, go back to the element at index 0 and repeat step 1.

### Real-World Applications

***Bubble Sort*** is not ideal for many real-world applications. If a small element that _should_ be at the beginning of our array is originally located near the end, it will take a long time to move it into its correct position.

However, it should be noted that if you perform **Bubble Sort** on an array that's already sorted, it will only require a single pass through the array, making its best-case performance linear. It's also very simple to implement.

## Selection Sort

***Selection Sort*** is an algorithm that many of you have probably used before when sorting things in your everyday lives. Imagine that you have several books you want to arrange on a shelf from shortest to tallest. You start off by looking for the shortest book, and when you find it, put it on the far left side of the shelf. Then, you look for the second shortest book and insert it directly to the right of the first book. You repeat this process, selecting the next shortest book and moving it next to the most recently placed book, until you have moved all books into the correct place. This is ***Selection Sort***.  

An example of this algorithm being applied to an array with 10 numerical elements can be seen in the video below.

[(VIDEO) Select-sort with Gypsy folk dance](https://www.youtube.com/watch?v=Ns4TPTC8whw)

[![(VIDEO) Select-sort with Gypsy folk dance](https://i.ytimg.com/vi/Ns4TPTC8whw/hqdefault.jpg)](https://www.youtube.com/watch?v=Ns4TPTC8whw)

### Algorithm

1. Start with current index = 0

2. For all indices EXCEPT the last index:

    a. Loop through elements on right-hand-side 
    of current index and find the smallest element

    b. Swap the element at current index with the
    smallest element found in above loop

### Real-World Applications

While ***Selection Sort*** is one of the easier sorting algorithms to understand and implement, it has one major drawback - its efficiency.

Recall that the runtime complexity of an algorithm, often expressed using *Big O notation*, tells us how the amount of operations our algorithm requires will grow as the size of our input grows. ***Selection Sort*** has  a runtime of O(n²), making it impractical to use with many large, real-world data sets.

# Search algorithms

## Task 1

Add a `delete` method for removing key-value pairs in the `HashTable` implemented in the lecture notes.

## Task 2

Implement binary search for a sorted array of floating-point numbers. The function for binary search should return a tuple where the first element is the number of iterations needed to find the element. The second element should be the "upper bound" — the smallest element that is greater than or equal to the given value.

## Task 3

Compare the efficiency of the substring search algorithms: Boyer-Moore, Knuth-Morris-Pratt, and Rabin-Karp based on two text files ([article 1](./assets/article_1.txt), [article 2](./assets/article_2.txt)). Using `timeit`, measure the execution time of each algorithm for two types of substrings: one that actually exists in the text, and another — invented (substring selection at your discretion). Based on the obtained data, determine the fastest algorithm for each text separately and overall.

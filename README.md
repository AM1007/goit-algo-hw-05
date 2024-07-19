# Search algorithms

## Task 1

Add a `delete` method for removing key-value pairs in the `HashTable` implemented in the lecture notes.

## Task 2

Implement binary search for a sorted array of floating-point numbers. The function for binary search should return a tuple where the first element is the number of iterations needed to find the element. The second element should be the "upper bound" — the smallest element that is greater than or equal to the given value.

## Task 3

Compare the efficiency of the substring search algorithms: Boyer-Moore, Knuth-Morris-Pratt, and Rabin-Karp based on two text files ([article 1](./task_3/article_1.txt), [article 2](./task_3/article_2.txt)). Using `timeit`, measure the execution time of each algorithm for two types of substrings: one that actually exists in the text, and another — invented (substring selection at your discretion). Based on the obtained data, determine the fastest algorithm for each text separately and overall.

### Result

| Substring  | Algorithm   | Article 1 (sec) | Article 2 (sec) |
| ---------- | ----------- | --------------- | --------------- |
| Література | Boyer-Moore | 0.053505        | 0.057251        |
| Література | KMP         | 0.105887        | 0.155059        |
| Література | Rabin-Karp  | 0.282676        | 0.398028        |
| алгоритм   | Boyer-Moore | 0.000961        | 0.013094        |
| алгоритм   | KMP         | 0.002042        | 0.029687        |
| алгоритм   | Rabin-Karp  | 0.005457        | 0.086537        |

### Сonclusion

Based on the execution time results in the table, the best algorithm for skin text evaluation as a whole is the Boyer-Moore algorithm. It consistently has the lowest execution time across different patterns and articles.

Here are the execution times for the Boyer-Moore algorithm on the two articles:

For the pattern "algorithms", the execution time on Article 1 is 0.036287 seconds and on Article 2 is 0.062654 seconds.
For the pattern "non-existent substring to test for", the execution time on Article 1 is 0.018204 seconds and on Article 2 is 0.023793 seconds.
Compared to the other algorithms (KMP and Rabin-Karp), the Boyer-Moore algorithm has the lowest execution times in both cases.

Therefore, the Boyer-Moore algorithm is recommended as the best algorithm for skin text evaluation.

# SLE-2: Profiling Report

**Course:** 02AML204 – Introduction to Artificial Intelligence  
**PRN:** 25UAM01
**Name:** Samruddhi Javale
**Division:** A

---

## 1. Algorithms / Versions Profiled

- **Algorithm A:** Linear Search
- **Algorithm B:** Binary Search
- **Problem Used:** Searching an element in a sorted list

Both algorithms were tested on the same list so that the comparison is fair.

The list contains 100,000 elements.

---

## 2. Profiling Method

- **Tool Used:** py-spy and Python `time` module
- **Measurement:** Execution time in seconds
- **Number of Runs:** 3 runs for each case

The execution time was measured for the Best Case, Average Case, and Worst Case.

### Cases Used

**Linear Search**
- Best Case: Element is at the beginning.
- Average Case: Element is near the middle.
- Worst Case: Element is at the end.

**Binary Search**
- Best Case: Element is at the middle.
- Average Case: Element is found after a few searches.
- Worst Case: Element is not present / requires maximum comparisons.

---

## 3. Results

### Execution Time Comparison

| Case | Linear Search (seconds) | Binary Search (seconds) |
|------|--------------------------|--------------------------|
| Best Case | ______ | ______ |
| Average Case | ______ | ______ |
| Worst Case | ______ | ______ |

### Number of Comparisons

| Case | Linear Search | Binary Search |
|------|---------------|---------------|
| Best Case | ______ | ______ |
| Average Case | ______ | ______ |
| Worst Case | ______ | ______ |

### Short Observation

Linear Search checks the elements one by one, so its execution time increases when the required element is farther from the beginning.

Binary Search repeatedly divides the sorted list into smaller parts. Therefore, it requires fewer comparisons for a large list.

---

## 4. Justification & Analysis

The profiling results show the difference between Linear Search and Binary Search.

Linear Search checks elements sequentially from the beginning until the required element is found.

In the best case, Linear Search finds the element in the first comparison.

In the worst case, Linear Search may check all the elements.

Binary Search works only on a sorted list and divides the search area into two parts in every iteration.

Therefore, Binary Search needs fewer comparisons when the input size becomes large.

The actual execution times obtained from the experiment are used in the comparison table above.

As the problem size increases, the difference between the two searching methods becomes more noticeable.

---

## 5. AI Contribution Note

- **AI Tool Used:** ChatGPT
- **What AI Helped With:** AI helped me understand the profiling task, prepare the Linear Search and Binary Search programs, and understand how to use py-spy.
- **What I Did Myself:** I created the files, executed the programs, ran the profiling experiment, recorded the actual execution times, and analyzed the results.

---

## 6. Conclusion

This profiling exercise helped me understand how the performance of two search algorithms can be measured using actual execution time.

I learned that Linear Search checks elements sequentially, while Binary Search reduces the search space by dividing it into smaller parts.

I also learned how profiling tools can be used to compare algorithms using real performance data.

The experiment helped me connect the theoretical behavior of algorithms with their actual execution performance.
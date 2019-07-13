### Binary Search
Code template: [[template.py](template.py)].

#### Complexity
T(N) = T(N/2) + O(1) = logN * O(1) + T(1) = O(logN)

分析：用O(1)的时间把问题规模缩小一半。

类比：用O(N)的时间把问题缩小一半。

T(N) = T(N/2) + O(N) = ... = O(N + N/2 + N/4 + ...) + T(1) ~= O(2N) = O(N)

#### Variation 变形
* Insertion index: use template, return `r` [[template.py](template.py)].
* Find first occurrence of change [[first_occurence.py](first_occurence.py)].
* Find last occurrence of change [[last_occurence.py](last_occurence.py)].

#### Primer 基础题
* Plain vanilla binary search while loop [[704](704_binary_search.py)].
* Plain vanilla binary search recursion [[457](457_classical_binary_search.py)].
* Plain vanilla binary search for insert position [[35](35_search_insert_position.py)].

#### Application 经典题
* XXOO: Find point of change (first occurrence of a new series) [[278](278_first_bad_version.py)].
* XXOO: Find minimum in a rotated array (first bad version logic) [[minimim_in_rotated_array.py](minimim_in_rotated_array.py)].
* Half-half: Search in rotated sorted array [[33](33_search_in_rotated_sorted_array.py)].
* Half-half: Find peak index in a mountain array. Apply logic, not template [[852](852_peak_index_in_a_mountain_array.py)].
* 二分答案: Square root [[69](69_sqrtx.py)].
* 二分答案：Wood cut [[link](https://www.lintcode.com/problem/wood-cut/description)][[wood_cut.py](wood_cut.py)].
* 二分答案：Copy book [[link](https://www.lintcode.com/problem/copy-books/description)][[copy_book.py](copy_book.py)].

#### Hard 难题
* Maximum Average Subarray II [[Link](https://leetcode.com/problems/maximum-average-subarray-ii/)][[Code](644_maximum_average_subarray_ii.py)]
  - Keep a cumulative sum array `s` of length `n + 1`, first element is 0.
  - `s[i]` is sum of elements `nums[0] + ... nums[i-1]`, first i elements
  - `s[j]` is sum of elements `nums[0] + ... nums[j-1]`, first j elements
  - Let `i > j`
  - To get sum of elements `j ~ i` (inclusive j), use `s[i] - s[j - 1]`
  - Average of elements `j ~ i` (inclusive) is `(s[i] - s[j - 1]) / (i - j + 1)`
  - Reduce sum array `s[i] = nums[0] - m + ... + nums[i - 1] - m`
* Median of Two Sorted Arrays [[Link](https://leetcode.com/problems/median-of-two-sorted-arrays/)][[Code](4_median_of_two_sorted_arrays.py)][[Tutorial](https://www.youtube.com/watch?time_continue=1&v=LPFhl65R7ww)]
  - Find index `i` for array `x`, `j` for array y, such that `x[i] <= y[j + 1], y[j] <= x[i + 1]`
  - For even number of elements `m + n`, `i + j = (m + n) / 2`, median is `avg(max(x[i], y[j]), min(x[i+1], y[j] + 1))`
  - For odd number of elemnts, `i + j = (m + n + 1) / 2`, median is `max(x[i], y[j])`
  - Combine the even & odd condition using integer division `i + j = (m + n + 1) // 2`
  - Time `O(log(min(x, y)))`
  - make `x` the shorter array
  - Use infinity to handle empty partition
  - In my code, `i, j` points to first elements in right partitions

```   
        i
x1 x2 | x3 x4 x5 x6
y1 y2 y3 y4 | y5 y6 y7 y8
              j
```

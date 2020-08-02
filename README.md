# 1494.-Parallel-Courses-II
LeetCode: 1494. Parallel Courses II


Given the integer n representing the number of courses at some university labeled from 1 to n, and the array dependencies where dependencies[i] = [xi, yi]  represents a prerequisite relationship, that is, the course xi must be taken before the course yi.  Also, you are given the integer k.

In one semester you can take at most k courses as long as you have taken all the prerequisites for the courses you are taking.

Return the minimum number of semesters to take all courses. It is guaranteed that you can take all courses in some way.

Example 1:

Input: n = 4, dependencies = [[2,1],[3,1],[1,4]], k = 2
Output: 3 
Explanation: The figure above represents the given graph. In this case we can take courses 2 and 3 in the first semester, then take course 1 in the second semester and finally take course 4 in the third semester.


Example 2:

Input: n = 5, dependencies = [[2,1],[3,1],[4,1],[1,5]], k = 2
Output: 4 
Explanation: The figure above represents the given graph. In this case one optimal way to take all courses is: take courses 2 and 3 in the first semester and take course 4 in the second semester, then take course 1 in the third semester and finally take course 5 in the fourth semester.


Input: n = 11, dependencies = [], k = 2
Output: 6


Solution:
I use reccursion to solve this problem.

1. Finding root nodes. Which are nothing but subjects which does not have any dependency.

2. if length of root node is less than or equal k, append subject(s) to the list.
   else get combination of subjects of length (k),
   than, for each subject combination get subjects whose dependencies are resolved.
3. For new subject list, repeat the step 2.
4. if new subject list is empty and all subjects are visited, then the length of the queue to the semister list.
5. if legth of the semister list exceeds above nCr then exit.

Finally, return minumum value from semister list.

Let me know if you have any questions.

Note: Code is not optimized, there is lot of room for improvement.

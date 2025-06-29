Part A: Questions about the video
Do not forget to add all group members' names (and email addresses) to the top of the
file if you are working in a group.
1. What sorting algorithm was the speaker trying to improve?

Insertion sort resulting in Heap Insertion sort

2. At what partition size does VS perform a simpler sort algorithm instead of
continuing to partition?

Threshold is 32 on VS

3. At what partition size does GNU perform a simpler sort algorithm instead of
continuing to partition?

Threshhold is 16 on GNU

4. Regular insertion sort does a linear search backwards from end of array for 
correct spot to insert. According to the speaker, why does switching to a binary
search not improve performance?

Reduces the amount of comparisons by 13% but increases runtime by 13% due to increased threshold

5. Describe what is meant by branch prediction. (this may require further research)

Branch prediction is used by the cpu to guess the most likely outcome of a branch for example an if statement if it guesses correct it can continue running the code without any delay, however if it guesses wrong it the pipeline must be discarded and then the correct branch must be run which increases the total amount of cpu cycles required.

6. What is meant by the term informational entropy? (this may require further
research)

Informational entropy is the unpredictability of an outcome. A random number generator from 1–100 will have high entropy, while a generator from 1–2 will have lower entropy, because it has fewer possible outcomes and is more predictable.

7. Speaker suggests the following algorithm:
o make_heap()
o unguarded_insertion_sort()
He suggests that by doing make_heap() first, you can do something called
unguarded_insertion_sort(). Please explain what unguarded_insertion_sort() is and
why it is faster than regular insertion sort. How does performing make_heap()
allow you to do this?

make_heap() rearranges the array into a topology thats favourable for unguarded insertion sort by moving smaller elements to the beginning and larger ones towards the end which ends up removing the bounds checking because the smallest elements act as guards at the beginning of the array

8. The speaker talks about incorporating your conditionals into your arithmetic.
What does this mean? Provide an example from the video and explain how the
conditional is avoided.

The speaker wants you to do conditionals in your arithmetic to avoid decisions/branching which can increase cpu cycles such as the example in the video avoiding an if statement with
const auto jr = rightKid - (a[rightKid - 1] <= a[rightKid]) as well as sort2(first[0], first[size == 2]) where he states "you don't want if's you just want booleans within your calculations".

9. The speaker talks about a bug in gnu's implementation. Describe the
circumstances of this bug.

The speaker mentions an inefficency when building heaps in standard implementation like GNU when there is a lone child when creating the heap the speaker avoids this by ignoring the last element of the heap and then reinserts it using push_heap()
Or later in the video when he mentions rotated data which makes quicksort quadratic in GNU as well as 10th element being broken on GNU

10. The speaker shows several graphs about what happens as the threshold increases
using his new algorithm. The metric of comparison is increased, and the metric of
moves is increased, but time drops... What metric does the author think is
missing? Describe the missing metric he speaks about in the video. What is the
metric measuring?

The missing metric he talks about is D(n) the average distance between two subsequent array accesses which gives you an idea of cache

11. What does the speaker mean by fast code is left-leaning?

The speaker means that code that is straight forward without conditionals like if, for, switch which typically stick closer to the left of the page will be faster than having conditionals that introduce more lines of code pushing you further from the left

12. What does the speaker mean by not mixing hot and cold code?

Keep code that is run frequently together and code that is run infrequently together using breaks and returns

Part B: Reflection
This part must be individually done.
1. What did you/your team find most challenging to understand in the video?

I struggle the most with understanding the different metrics such as the blended cost in the "Weird territory" of the video

2. What is the most surprising thing you learned that you did not know before?

I learned that heap insertion is faster than plain insertion in most cases

3. Has the video given you ideas on how you can write better/faster code? If yes,
explain what you plan to change when writing code in the future. If not, explain
why not.

Yes, the video explains and demonstrates that by including your conditionals in arithmetic when possible you can speed up your code as you avoid branching and conditional statements which slow down code.

Sources

https://en.algorithmica.org/hpc/pipelining/branching/
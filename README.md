# Problem 1299: Replace Elements with Greatest Element on Right Side

7/14/2025

## Thought Process
My initial reaction to the problem was to use a double for loop and traverse through the array multiple times to get the max value of the right side. I also knew that if the length of the array list equal to 1, then to just return a list with -1.  

##  Initial Solution
I initially created an ans list to put the max values in; however, I decided that I could just replace the initial list with max values. I would go through both loops, and after the inner loop runs, I would put the max value in the list. After both loops run, I return the list.

Initial solution - Time Limit Exceeded 

Complexity - O(n^2)

## Final Solution
I decided to go backwards, starting from len(arr) - 1, and incrementing by -1. This way I only have to iterate through the list once. I set the max_value to equal -1 and then checked if the current array index value was greater. If it was, then I would set max_value to equal the current list value. This way, I would not have to iterate through the list multiple times.

Final Solution - 23 ms

Complexity - O(n)

## Takeaways
I learned the proper way to iterate backwards through a list in python, after knowing how to do it in Java. I also learned how to manipulate iteration and how to save space by using already existing data structures
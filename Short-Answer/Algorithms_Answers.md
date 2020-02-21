#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) O(1) because no matter what the input size of n, the number of operations remains constant. 


b) O(log n) because even though the range is declared as n number of elements, the loop only iterates j times in 2^j until that total surpasses n.


c) O(n) because the function bunnyEars is recursively being called n times before reaching its base case.

## Exercise II

1) Find the middle floor of the n-floor building and drop an egg
    a) If the egg breaks, eliminate all floors below
    b) If the egg doesn't break, eliminate all floors above
2) Repeat on sub-sections of floors based on egg-drop results
3) Stop when you've reached the lowest floor that the egg doesn't break from
4) Runtime complexity: O(log n)



% Base case: The sum of integers from 1 to 0 is 0.
sum_to_n(0, 0).

% Recursive case: The sum of integers from 1 to N is N + sum of integers from 1 to (N-1).
sum_to_n(N, Sum) :-
    N > 0,               % Ensure N is greater than 0 to continue recursion.
    N1 is N - 1,         % Calculate the previous number.
    sum_to_n(N1, Sum1),  % Recursively calculate the sum of numbers from 1 to N-1.
    Sum is N + Sum1.     % Add N to the result of the recursive call.

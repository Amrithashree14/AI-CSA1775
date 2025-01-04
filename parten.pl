% Pattern matching for lists
match_list([H|T], H, T).             % Matches the head and tail of a list
match_first_two([X, Y|_], X, Y).     % Matches the first two elements of a list

% Pattern matching for nested lists
match_nested([H|_], H).              % Matches the first element of a nested list
match_inner([[X|]|], X).           % Matches the first element of the first inner list

% Pattern matching for strings (treated as lists of characters)
match_string("hello", "h", Rest) :-  % Matches 'h' and the rest of the string
    "hello" = [H|T],
    atom_chars(H, ["h"]),
    Rest = T.

% Pattern matching for structures
match_structure(person(Name, Age), Name, Age). % Matches fields in a structure

% Example queries:
% ?- match_list([a, b, c], Head, Tail).
% ?- match_first_two([1, 2, 3], First, Second).
% ?- match_nested([[x, y], z], Inner).
% ?- match_inner([[a, b], [c, d]], InnerElement).
% ?- match_string("hello", H, Rest).
% ?- match_structure(person(john, 25), Name, Age).

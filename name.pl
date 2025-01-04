% Define a database of people with their name and date of birth.
person('Alice', '2000-05-14').
person('Bob', '1998-09-22').
person('Charlie', '1995-12-30').
person('Diana', '2001-03-10').

% Query a person's date of birth by their name.
find_dob(Name, DOB) :-
    person(Name, DOB).

% Query a person's name by their date of birth.
find_name(DOB, Name) :-
    person(Name, DOB).

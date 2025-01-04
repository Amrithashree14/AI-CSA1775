% Define a database of students, teachers, and subject codes.
student_teacher_subject('John', 'Mr. Smith', 'CS101').
student_teacher_subject('Alice', 'Ms. Johnson', 'CS102').
student_teacher_subject('Bob', 'Dr. Brown', 'CS103').
student_teacher_subject('Eve', 'Dr. White', 'CS104').

% Query the teacher and subject code for a specific student.
find_teacher_and_subject(Student, Teacher, SubjectCode) :-
    student_teacher_subject(Student, Teacher, SubjectCode).

% Query the students who are taught by a specific teacher.
find_students_by_teacher(Teacher, Student) :-
    student_teacher_subject(Student, Teacher, _).

% Query the students enrolled in a specific subject code.
find_students_by_subject(SubjectCode, Student) :-
    student_teacher_subject(Student, _, SubjectCode).

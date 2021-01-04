## Environment:
- Python version: 3.7
- Django version: 3.0.6

## Read-Only Files:
- app/tests.py
- manage.py

## Requirements:


In this challenge, your task is to implement two models to represent Students and Courses.


1. Each course must have the following fields:

- `id`: a unique autoincrement integer ID of the course
- `name`: a string denoting the name of the course


2. Each student must have the following fields:

- `id`: a unique autoincrement integer ID of the student
- `name`: a string denoting the name of the student


3. A course must be able to be created in the following way:

   ```course = Course(name='Math')```


4. A student must be able to be created in the following way:

   ```student = Student(name='Alex')```

5. The Course model implements the `get_students()` method, which returns a `Queryset` of all Students enrolled in the Course, sorted by their usernames in ascending order.

6. The Student model implements the `get_courses()` method, which returns a `Queryset` of all Courses the Student is enrolled in, sorted by their ids in ascending order.

7. The Student model implements the `enroll(course)` method, which enrolls the Student in the Course given as a parameter. If the student is already enrolled in the given course, nothing happens.

8. The Student model implements the `disenroll(course)` method, which disenrolls the Student from the Course given as a parameter. If the student is not enrolled in the given course, nothing happens.


## Example Usage:

```python
>>> alex = Student(name='Alex')
>>> alex.save()
>>> jordan = Student(name='Jordan')
>>> jordan.save()

>>> math = Course(name='math')
>>> math.save()
>>> biology = Course(name='Biology')
>>> biology.save()

>>> alex.enroll(math)
>>> jordan.enroll(biology)
>>> alex.enroll(biology)

>>> biology.get_students()
<QuerySet [<Student: Student object (1)>, <Student: Student object (2)>]>

>>> math.get_students()
<QuerySet [<Student: Student object (1)>]>

>>> alex.get_courses()
<QuerySet [<Course: Course object (1)>, <Course: Course object (2)>]>

>>> jordan.get_courses()
<QuerySet [<Course: Course object (2)>]>

>>> alex.disenroll(biology)
>>> biology.get_students()
<QuerySet [<Student: Student object (2)>]>

>>> alex.get_courses()
<QuerySet [<Course: Course object (1)>]>
```

## Commands

+ run:
```source env1/bin/activate; pip3 install -r requirements.txt; python3 manage.py makemigrations && python3 manage.py migrate --run-syncdb && python3 manage.py runserver 0.0.0.0:8000```

+  install:
```bash python_install.sh;source env1/bin/activate; pip3 install -r requirements.txt;```

+ test:
```rm -rf unit.xml;source env1/bin/activate; python3 manage.py test```

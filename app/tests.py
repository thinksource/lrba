from django.test import TestCase

from django.db.models import QuerySet

from app.models import Course
from app.models import Student


class CourseCreationTestCase(TestCase):
    def test_create_course(self):
        course = Course(name='Math')
        course.save()
        self.assertEqual(course.name, 'Math')


class StudentCreationTestCase(TestCase):
    def test_create_student(self):
        student = Student(name='Alex')
        student.save()
        self.assertEqual(student.name, 'Alex')


class EnrollmentTestCase(TestCase):

    def test_enroll_student_in_course(self):
        student = Student(name='Alex')
        student.save()
        course = Course(name='Math')
        course.save()

        self.assertIsInstance(course.get_students(), QuerySet)
        self.assertNotIn(student, course.get_students())

        self.assertIsInstance(student.get_courses(), QuerySet)
        self.assertNotIn(course, student.get_courses())

        student.enroll(course)

        self.assertIn(student, course.get_students())
        self.assertIn(course, student.get_courses())

    def test_enroll_already_enrolled_student_in_course(self):
        student = Student(name='Alex')
        student.save()
        course = Course(name='Math')
        course.save()

        student.enroll(course)

        self.assertIn(student, course.get_students())
        self.assertIn(course, student.get_courses())

        student.enroll(course)

        self.assertIn(student, course.get_students())
        self.assertIn(course, student.get_courses())

    def test_disenroll_student_from_course(self):
        student = Student(name='Alex')
        student.save()
        course = Course(name='Math')
        course.save()

        student.enroll(course)

        self.assertIn(student, course.get_students())
        self.assertIn(course, student.get_courses())

        student.disenroll(course)

        self.assertNotIn(student, course.get_students())
        self.assertNotIn(course, student.get_courses())

    def test_disenroll_not_enrolled_student_from_course(self):
        student = Student(name='Alex')
        student.save()
        course = Course(name='Math')
        course.save()

        self.assertNotIn(student, course.get_students())
        self.assertNotIn(course, student.get_courses())

        student.disenroll(course)

        self.assertNotIn(student, course.get_students())
        self.assertNotIn(course, student.get_courses())

    def test_with_many_courses_and_many_students(self):
        alex = Student(name="Alex")
        alex.save()
        jordan = Student(name="Jordan")
        jordan.save()

        math = Course(name="Math")
        math.save()
        biology = Course(name="Biology")
        biology.save()

        alex.enroll(math)
        jordan.enroll(biology)
        alex.enroll(biology)

        self.assertListEqual(list(alex.get_courses()), [math, biology])
        self.assertListEqual(list(jordan.get_courses()), [biology])

        self.assertListEqual(list(biology.get_students()), [alex, jordan])

        self.assertListEqual(list(math.get_students()), [alex])

        alex.disenroll(biology)

        self.assertListEqual(list(alex.get_courses()), [math])
        self.assertListEqual(list(biology.get_students()), [jordan])

        jordan.disenroll(math)
        self.assertListEqual(list(jordan.get_courses()), [biology])
        self.assertListEqual(list(math.get_students()), [alex])

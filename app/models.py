from django.db import models




class Course(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return str('%s, %s'%(self.id, self.name))

    def get_course(self):
        return Course.objects.all()

    def get_students(self):
        return Student.objects.filter(selectedCourse=self).order_by('name')
        

class Student(models.Model):
    name = models.CharField(max_length=100)
    selectedCourse = models.ManyToManyField(Course, through='StudentSelectedCourse')

    def get_student(self):
        return Student.objects.all()

    def enroll(self, cr):
        sc = StudentSelectedCourse(stud=self, course=cr)
        sc.save()

    def disenroll(self, cr):
        StudentSelectedCourse.objects.filter(stud=self, course=cr).delete()

    def get_courses(self):
        return Course.objects.filter(studentselectedcourse__stud=self)

class StudentSelectedCourse(models.Model):
    stud = models.ForeignKey(Student, on_delete = models.CASCADE)
    course = models.ForeignKey(Course, on_delete = models.CASCADE)

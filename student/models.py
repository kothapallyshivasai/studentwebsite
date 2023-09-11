from django.db import models

class Student(models.Model):
    student_roll_number = models.CharField(primary_key=True, max_length=100)
    student_first_name = models.CharField(max_length=40)
    student_last_name = models.CharField(max_length=40)
    student_date_of_birth = models.DateField()
    student_year = models.CharField(max_length=100, choices=(
        ("1st Year", "1st Year"), ("2nd Year", "2nd Year"), ("3rd Year", "3rd Year"), ("4th Year", "4th Year")
        ))
    student_branch = models.CharField(max_length=100, choices=(
        ("Computer Science & Engineering", "Computer Science & Engineering"),
        ("Mechanical Engineering", "Mechanical Engineering"),
        ("Civil Engineering", "Civil Engineering"),
        ("Electrical & Electronics Engineering", "Electrical & Electronics Engineering"),
        ("Electronics and Communications Engineering", "Electronics and Communications Engineering")
        ))
    student_picture = models.ImageField(upload_to="images/")
    student_phone_number = models.IntegerField(unique=True)
    student_description = models.TextField(max_length=200)
    student_address = models.TextField(max_length=200)

    def __str__(self):
        return self.student_roll_number
    

class ContactUs(models.Model):
    id = models.AutoField(primary_key=True)
    student_roll_number = models.TextField(max_length=150)
    subject = models.TextField(max_length=150)
    message = models.TextField(max_length=300)

    def __str__(self):
        return str(self.student_roll_number)

class Attendance(models.Model):
    student_roll_number = models.ForeignKey(Student, on_delete=models.CASCADE)
    january_attendance = models.IntegerField()
    febraury_attendance = models.IntegerField()
    march_attendance = models.IntegerField()
    april_attendance = models.IntegerField()
    may_attendance = models.IntegerField()
    june_attendance = models.IntegerField()
    july_attendance = models.IntegerField()
    august_attendance = models.IntegerField()
    september_attendance = models.IntegerField()
    october_attendance = models.IntegerField()
    november_attendance = models.IntegerField()
    december_attendance = models.IntegerField()
    
    def __str__(self):
        return str(self.student_roll_number)

    class Meta:
        unique_together = ('id', 'student_roll_number')

    @property
    def total_attendance(self):
        return (self.january_attendance + self.febraury_attendance + self.march_attendance + self.april_attendance + self.may_attendance + self.june_attendance
                        + self.july_attendance + self.august_attendance + self.september_attendance + self.october_attendance + self.november_attendance + self.december_attendance)/12

class Branch(models.Model):
    branch = models.TextField(primary_key=True)

class BranchSubjects(models.Model):
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)
    year = models.TextField(choices=(
        ("1st Year", "1st Year"), ("2nd Year", "2nd Year"), ("3rd Year", "3rd Year"), ("4th Year", "4th Year")
        ))
    subject_1 = models.TextField(max_length=50, unique=True)
    subject_2 = models.TextField(max_length=50, unique=True)
    subject_3 = models.TextField(max_length=50, unique=True)
    subject_4 = models.TextField(max_length=50, unique=True)

    def __str__(self):
        return str(self.branch) 
    
    class Meta:
        unique_together = ('branch', 'year')
    

class StudentMarks(models.Model):
    roll_number = models.ForeignKey(Student, on_delete=models.CASCADE)
    year = models.TextField(choices=(
        ("1st Year", "1st Year"), ("2nd Year", "2nd Year"), ("3rd Year", "3rd Year"), ("4th Year", "4th Year")
        ))
    subject_1 = models.IntegerField()
    subject_1_result = models.BooleanField()

    subject_2 = models.IntegerField()
    subject_2_result = models.BooleanField()

    subject_3 = models.IntegerField()
    subject_3_result = models.BooleanField()

    subject_4 = models.IntegerField()
    subject_4_result = models.BooleanField()

    # Constraint
    class Meta:
        unique_together = ('roll_number', 'year')

    def __str__(self):
        return str(self.roll_number) + " " + str(self.year)
    
class BranchDetails(models.Model):
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)
    description = models.TextField()
    points = models.TextField()

    def __str__(self):
        return str(self.branch)
    
    class Meta:
        unique_together = ('branch', 'id')
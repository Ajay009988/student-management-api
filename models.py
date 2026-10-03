from django.db import models
from django.contrib.auth.models import User

class Student(models.Model):
    COURSE = [('BCA','BCA'),('B.Tech CSE','B.Tech CSE'),('BBA','BBA'),('MBA','MBA'),('B.Sc','B.Sc'),('MCA','MCA')]
    YEAR = [('1st Year','1st Year'),('2nd Year','2nd Year'),('3rd Year','3rd Year'),('4th Year','4th Year')]
    
    owner = models.ForeignKey(User, on_delete=models.CASCADE) # Jiska data usi ko dikhega
    name = models.CharField(max_length=100)
    roll_no = models.CharField(max_length=50)
    course = models.CharField(max_length=50, choices=COURSE)
    year = models.CharField(max_length=20, choices=YEAR)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    photo = models.ImageField(upload_to='student_photos/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
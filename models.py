from django.db import models

#DataFlair Models

class Book(models.Model):
	name = models.CharField(max_length = 50)
	picture = models.ImageField()
	author = models.CharField(max_length = 30, default='anonymous')
	email = models.EmailField(blank = True)
	describe = models.TextField(default = 'DataFlair Django tutorials')

	def __str__(self):
		return self.name

class User(models.Model):
    email=models.EmailField(unique=True)
    password=models.CharField(max_length=20)
    otp=models.IntegerField(default=459)
    is_active=models.BooleanField(default=True)
    is_verfied=models.BooleanField(default=False)
    role=models.CharField(max_length=10)
    created_at=models.DateTimeField(auto_now_add=True,blank=False)
    updated_at=models.DateTimeField(auto_now=True,blank=False)

class Teacher(models.Model):
    user_id=models.ForeignKey(User,on_delete=models.CASCADE)
    firstname=models.CharField(max_length=50)
    lastname=models.CharField(max_length=50)
    qualification=models.CharField(max_length=100)
    mobile=models.CharField(max_length=10)
    stream=models.CharField(max_length=100,blank=True)
    address=models.CharField(max_length=500,blank=True)
    city=models.CharField(max_length=50)
    state=models.CharField(max_length=50,blank=True)
    gender=models.CharField(max_length=10)
    birthdate=models.DateField()
    password=models.CharField(max_length=10,default=5)


class Student(models.Model):
    user_id=models.ForeignKey(User,on_delete=models.CASCADE)
    firstname=models.CharField(max_length=50)
    lastname=models.CharField(max_length=50)
    mobile=models.CharField(max_length=10)
    address=models.CharField(max_length=500,blank=True)
    city=models.CharField(max_length=50)
    state=models.CharField(max_length=50,blank=True)
    gender=models.CharField(max_length=10)
    birthdate=models.DateField()

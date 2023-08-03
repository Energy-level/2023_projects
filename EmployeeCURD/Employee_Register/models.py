from django.db import models
class Position(models.Model):
    title=models.CharField(max_length=25)
    #Displaying the position names instead of objects in position field
    def __str__(self) -> str:
        return self.title
class Employee(models.Model):
    fullname=models.CharField(max_length=100)
    emp_code=models.CharField(max_length=3)
    mobile=models.CharField(max_length=15)
    position=models.ForeignKey(Position,on_delete=models.CASCADE)

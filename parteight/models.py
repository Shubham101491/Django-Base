from django.db import models

class Employee(models.Model):
    eid = models.CharField(max_length=20)
    ename = models.CharField(max_length=50)
    eemail = models.EmailField()
    econtact = models.CharField(max_length=15)
    eaddress = models.CharField(max_length=300)

    class Meta:
        db_table = "employees data"

'''Using Meta for showing database name accordingly 
othervies it will show by default'''
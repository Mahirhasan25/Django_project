from django.db import models

# Create your models here.
class AddTask(models.Model):
    title = models.CharField(max_length=50)
    start_date = models.DateTimeField(auto_now_add=True)
    end_date = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=20, default='INCOMPLETE')
    Choice = (
        ('ACADEMIC', 'ACADEMIC'),
        ('JOB', 'JOB'),
        ('PERSONAL', 'PERSONAL'),
    )
    catagory = models.CharField(max_length=20, choices=Choice)
    description = models.TextField(blank=True)
    edit_cnt = models.IntegerField(default=0)
    last_update = models.DateTimeField(null=True, blank=True)
    def save(self):
        self.status = self.status.upper()
        super().save()
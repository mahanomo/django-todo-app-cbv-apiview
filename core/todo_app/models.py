from django.db import models

# Create your models here.
class AddTodo(models.Model):
    user = models.ForeignKey("accounts.CustomUser",on_delete=models.CASCADE,null=True,blank=True)
    task = models.CharField(max_length=255)
    is_done = models.BooleanField(default=False)

    def __str__(self):
        return self.task

from django.db import models
from django.contrib.auth.models import User

class Entry(models.Model):
    entry_title  = models.CharField(max_length = 50,verbose_name ="عنوان")
    entry_text   = models.TextField(verbose_name ="متن")  
    entry_data   = models.DateTimeField(auto_now_add=True,verbose_name ="تاریخ")
    entry_author = models.ForeignKey(User,on_delete=models.CASCADE,verbose_name ="نویسنده")
    entry_url    = models.URLField(verbose_name="لینک",null = True, blank =True)
    #image        = models.ImageField(upload_to ="images/",null = True, blank =True,verbose_name ="تصویر")


    class Meta:
        verbose_name_plural = "مدل"

    def __str__(self):
        return self.entry_title
from __future__ import unicode_literals #là mô-đun giả mà lập trình viên có thể sử dụng để bật các tính năng ngôn ngữ mới không tương thích với trình thông dịch hiện tại
from django.db import models

# Create your models here.

class Main(models.Model):
    name = models.CharField(max_length = 30)
    about = models.TextField(default="-")
    fb = models.CharField(default="-", max_length = 30)
    tw = models.CharField(default="-", max_length = 30)
    yt = models.CharField(default="-", max_length = 30)
    tel = models.CharField(default="-", max_length = 30)
    link = models.CharField(default="-", max_length = 30)

    set_name = models.CharField(default="-", max_length = 30)

    # def __str__(self): #khai báo phương thức __str__() trong class để kiểm soát cách hiển thị kết quả được in ra.
        # return self.name
        # return self.name

    def __str__(self):
        return self.set_name + " | " + str(self.pk)


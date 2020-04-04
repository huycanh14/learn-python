from __future__ import unicode_literals #là mô-đun giả mà lập trình viên có thể sử dụng để bật các tính năng ngôn ngữ mới không tương thích với trình thông dịch hiện tại
from django.db import models

# Create your models here.

class Main(models.Model):
    name = models.TextField()

    def __str__(self): #khai báo phương thức __str__() trong class để kiểm soát cách hiển thị kết quả được in ra.
        # return self.name
        return self.name

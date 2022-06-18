from django.db import models
from Admins.models import AdminUser
# Create your models here.



class BookList(models.Model):

    title=models.TextField(blank=False, null=False)
    author=models.TextField(blank=True, null=True)
    published_date=models.DateTimeField( blank=True, null=True)
    genre=models.TextField(blank=True, null=True)

    added_by= models.ForeignKey(AdminUser, to_field='id', on_delete=models.CASCADE, blank=True, null=True)
    last_modified_time=models.DateTimeField(auto_now_add=True, blank=True, null=True)

    deleted_flag=models.BooleanField(default=False)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'book_list'



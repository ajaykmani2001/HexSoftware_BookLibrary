from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class userdetails(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    college_name=models.CharField(max_length=20)
    reg_no=models.CharField(max_length=30)
    roll_no=models.IntegerField()
    dept=models.CharField(max_length=30)
    phone=models.IntegerField()
    def __str__(self):
        return self.reg_no



class BookModel(models.Model):
    book_image=models.ImageField(upload_to='images/')
    book_name=models.CharField(max_length=50)
    author=models.CharField(max_length=50)
    book_id=models.CharField(max_length=50)
    genre=models.CharField(max_length=50)
    description=models.TextField()
    # ISBN=models.CharField(max_length=50,unique=True)
    available_copies=models.IntegerField()
    def __str__(self):
        return self.book_name



class BookrequestModel(models.Model):
    user=models.ForeignKey(userdetails,on_delete=models.CASCADE)
    book=models.ForeignKey(BookModel,on_delete=models.CASCADE)
    requested_date=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Request By {self.user.user.username} for {self.book.book_name}"

# auto_now_add field will automatically stores the date time in the os sm
# f is a formatter


class AcceptedBooks(models.Model):
    details=models.ForeignKey(BookrequestModel,on_delete=models.CASCADE)
    accepted_date=models.DateTimeField(auto_now_add=True)
    return_date=models.DateTimeField()
    fine=models.IntegerField(default=0)

    def __str__(self):
        return f"Accepted request sent from {self.details.user.user.username} for {self.details.book.book_name}"



#
# class BookRequest(models.Model):
#     user=models.ForeignKey(UserDetails,on_delete=models.CASCADE)
#     book=models.ForeignKey(Book,on_delete=models.CASCADE)
#     request_date=models.DateTimeField(auto_now_add=True)
#     def __str__(self):
#         return f"Request by {self.user.user.username} for {self.book.title}"
#

class AcceptedBooksModel(models.Model):
    book_name=models.CharField(max_length=50)
    author=models.CharField(max_length=50)
    requested_date=models.DateTimeField()
    userdetails=models.ForeignKey(userdetails,on_delete=models.CASCADE)
    accepted_date=models.DateTimeField(auto_now_add=True)
    fine=models.IntegerField(default=0)
    return_date=models.DateTimeField()

    def __str__(self):
        return f"request by {self.userdetails.user.username} for {self.book_name}"
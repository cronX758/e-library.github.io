from django.db import models
from datetime import date

class Student(models.Model):
    username = models.CharField(max_length=150, unique=True, null=True)
    full_name = models.CharField(max_length=255, null=True)
    email = models.EmailField(unique=True)
    password = models.CharField(default=0, max_length=255)

    def __str__(self):
        return self.username

class Admin(models.Model):
    username = models.CharField(max_length=150, unique=True, null=True)
    email = models.EmailField(unique=True)
    password = models.CharField(default=0, max_length=255)

    def __str__(self):
        return self.username

class Contact(models.Model):
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True,null=True)

    def __str__(self):
        return f"Message from {self.email}"

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    category = models.CharField(max_length=255)
    description = models.TextField()
    publication_date = models.DateField()
    available_copies = models.PositiveIntegerField(default=0)
    cover_image = models.ImageField(upload_to='book_covers/', blank=True, null=True)

    def __str__(self):
        return self.title

class Borrow(models.Model):
    student = models.ForeignKey('Student', on_delete=models.CASCADE, related_name='borrows')
    book = models.ForeignKey('Book', on_delete=models.CASCADE, related_name='borrows')
    start_date = models.DateField(default=date.today)
    return_date = models.DateField()
    returned = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.student.full_name} borrowed {self.book.title}"
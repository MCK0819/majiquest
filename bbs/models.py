from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
    code = models.CharField(max_length=20)
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"Category for {self.code} by {self.name}"

class Board(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    deadline = models.DateField(null=True, blank=True)
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"Board title = {self.title}, content = {self.content}, author = {self.author}"

class Client_Request(models.Model):
    board = models.ForeignKey(Board, related_name='cli_req', on_delete=models.CASCADE)
    requester = models.ForeignKey(User, related_name='req_made', on_delete=models.CASCADE)
    provider = models.ForeignKey(User, related_name='req_accepted', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    is_accepted = models.BooleanField(default=False)

    def __str__(self):
        return f"Request for {self.board.title} by {self.requester.username}"
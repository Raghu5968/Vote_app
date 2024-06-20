from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from django import template

register = template.Library()

class Category(models.Model):
    name=models.CharField(max_length=30)

    @staticmethod
    def get_all_categories():
        return Category.objects.all()
    
    def __str__(self) -> str:
        return self.name
class Gender(models.Model):
    CATEGORY=(
        ('Male','Male'),
        ('Female','Female'),
        ('Others','Others')
    )

class Voter(models.Model):
    user=models.OneToOneField(User,blank=True,null=True,on_delete=models.CASCADE)
    username=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    number=models.CharField(max_length=10,null=True)
    password=models.CharField(max_length=100)
    voterage=models.IntegerField(null=True)
    category=models.ForeignKey(Category,default=1,on_delete=models.CASCADE)
    profile_pic=models.ImageField(default="pic.png",null=True,blank=True)
    def __str__(self):
        return self.username

class Candidate(models.Model):
    candidatename=models.CharField(max_length=200,null=True)
    age=models.IntegerField(null=True)
    partyname=models.CharField(max_length=200,null=True)
    candidate_pic=models.ImageField(default="pic.png",null=True,blank=True)
    partysymbol=models.ImageField(default="pic.png",null=True,blank=True)
    total_votes = models.IntegerField(default=0)  # Add this line to track total votes for each candidate


    def __str__(self) -> str:
        return self.candidatename
    
    @staticmethod
    def get_all_candidates():
        return Candidate.objects.all()
    

class Vote(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE)
    voter = models.ForeignKey(Voter, on_delete=models.CASCADE,related_name="voter",null=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.voter.username} voted for {self.candidate.candidatename}"
class feedback(models.Model):
    username=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    subject=models.CharField(max_length=100)
    message=models.CharField(max_length=300)
    def __str__(self):
        return self.username
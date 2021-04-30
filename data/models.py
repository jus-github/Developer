from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator,MaxValueValidator

# Create your models here.

class Technology(models.Model):
    name=models.CharField(max_length=255)
    class Meta:
        verbose_name = "Technology"
        verbose_name_plural = "Technologies"
    def __str__(self):
        return self.name

class Domain(models.Model):
    name=models.CharField(max_length=255)
    class Meta:
        verbose_name = "Domain"
        verbose_name_plural = "Domains"
    def __str__(self):
        return self.name

class Project(models.Model):
    name=models.CharField(max_length=255)
    rating=models.FloatField(validators=[MinValueValidator(0), MaxValueValidator(5)])
    class Meta:
        verbose_name = "Project"
        verbose_name_plural = "Projects"
    def __str__(self):
        return self.name

class Blog(models.Model):
    title=models.CharField(max_length=255)
    rating=models.FloatField(validators=[MinValueValidator(0), MaxValueValidator(5)])
    class Meta:
        verbose_name = "Blog"
        verbose_name_plural = "Blogs"
    def __str__(self):
        return self.title

class QA(models.Model):
    question=models.CharField(max_length=255)
    rating=models.FloatField(validators=[MinValueValidator(0), MaxValueValidator(5)])
    class Meta:
        verbose_name = "QA"
        verbose_name_plural = "QAs"
    def __str__(self):
        return self.question

class Developer(models.Model):
    # user=models.OneToOneField(User)
    name=models.CharField(max_length=255)
    email=models.CharField(max_length=255)
    location=models.CharField(max_length=255)
    technology=models.ManyToManyField(Technology)
    domain=models.ManyToManyField(Domain)
    projects=models.ManyToManyField(Project)
    blogs=models.ManyToManyField(Blog)
    qa=models.ManyToManyField(QA)    
    score=models.FloatField(blank=True,null=True)


    class Meta:
        verbose_name = "Developer"
        verbose_name_plural = "Developers"

    def __str__(self):
        return self.name

    def getFullName(self):
        return self.user.first_name + self.user.last_name    





# from django.db import models

# # Create your models here.
# class Technology(models.Model) :
#     name=models.CharField(max_length=200)

#     def __str__(self) :
#         return self.name

# class Domain(models.Model) :
#     name=models.CharField(max_length=200)

#     def __str__(self) :
#         return self.name

# class Q_A(models.Model) :
#     ques=models.CharField(max_length=200)
#     rating=models.FloatField()

#     def __str__(self):
#         return self.ques

# class Blog(models.Model) :
#     title=models.CharField(max_length=200)
#     rating=models.FloatField()

#     def __str__(self):
#         return self.title



# class Project(models.Model) :
#     name=models.CharField(max_length=200)
#     rating=models.FloatField()

#     def __str__(self):
#         return self.name


# class Developer(models.Model) :
#     name=models.CharField(max_length=200)
#     email=models.CharField(max_length=100)
#     location=models.CharField(max_length=150)
#     technology=models.ForeignKey(Technology,on_delete=models.CASCADE)
#     domain=models.ForeignKey(Domain,on_delete=models.CASCADE)
#     q_a=models.ForeignKey(Q_A,on_delete=models.CASCADE)
#     blog=models.ForeignKey(Blog,on_delete=models.CASCADE)
#     project=models.ForeignKey(Project,on_delete=models.CASCADE)
#     score=models.FloatField()

#     def __str__(self):
#         return self.name
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from data.models import Developer


# @receiver(pre_save, sender=Developer)
# def pre_save_developer(sender, instance, **kwargs):
#     score = 0    
#     a =0
#     b =0
#     c =0
#     for project in instance.projects.all():
#         a +=project.rating
#         print(a)
#     for blog in instance.blogs.all():
#         b += blog.rating
#         # print(b)
#     for q in instance.qa.all():
#         c += q.rating
#         # print(c)

#     score=((a*20)+(b*30)+(c*50))/100
#     instance.score = score
    # score = projectRating + blogRating + qaRating
    
    # projectScore=(50*projectRating)/(5*len(instance.projects.all()))
    # blogScore=(30*blogRating)/(5*len(instance.blogs.all()))
    # qaScore=(20*qaRating)/(5*len(instance.qa.all()))

    # score=projectScore+blogScore+qaScore
    
    
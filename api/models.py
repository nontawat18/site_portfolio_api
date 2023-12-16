from django.db import models
from django.db.models.fields import BooleanField 

class Task(models.Model):
    title = models.CharField(max_length=80)
    description = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now_add=True)
    completed = models.BooleanField(default=False)

    class Meta:
        db_table = 'task'
        ordering = ['-date_created']

    def __str__(self):
        return self.title
    
def upload_to(instance, filename):
    return 'images/{filename}'.format(filename=filename)

class Skill(models.Model):
    name = models.CharField(max_length=80)
    

    class Meta:
        db_table = 'skill'

    def __str__(self):
        return self.name

class Experience(models.Model):
    company = models.CharField(max_length=255)
    position = models.CharField(max_length=255)
    company = models.CharField(max_length=255)
    accomplishments = models.TextField()
    start_date =  models.DateField()
    end_date =  models.DateField()
    status = models.BooleanField(default=False)
    

    class Meta:
        db_table = 'experience'

    def __str__(self):
        return self.position
    
class Education(models.Model):
    school = models.CharField(max_length=255)
    graduate = models.CharField(max_length=255)
    accomplishments = models.TextField()
    start_date =  models.DateField()
    end_date =  models.DateField()
    status = models.BooleanField(default=False)
    

    class Meta:
        db_table = 'education'

    def __str__(self):
        return self.school
    
class Profile(models.Model):
    fullname =  models.CharField(max_length=255)
    email =  models.CharField(max_length=255)
    phone =  models.CharField(max_length=255)
    profile_image = models.ImageField(upload_to=upload_to, blank=True, null=True)
    id = models.AutoField(primary_key=True)
    address = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now_add=True)
    summary_detail = models.TextField()
    skill = models.ManyToManyField(Skill)
    # authors = models.ManyToManyField(Skill, related_name="book_list", blank=True)

    experience = models.ManyToManyField(Experience)
    education = models.ManyToManyField(Education)
    class Meta:
        db_table = 'profile'

    def __str__(self):
        return self.fullname
# Profile.objects.create(skill={
#         'name': 'John',
       
# })
# Profile.objects.filter(
#         data__name='John',
# ).delete()

  

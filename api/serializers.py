# api/serializers.py

from rest_framework import serializers
from .models import Profile, Skill, Education, Experience

# class TaskSerializer(serializers.ModelSerializer):

#     class Meta:
#         model = Task
#         fields = ('id', 'title', 'description', 'completed')
class SkillSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Skill
        fields = '__all__'

class EducationSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Education
        fields = '__all__'
        
class ExperienceSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Experience
        fields = '__all__'
        
class ProfileSerializer(serializers.ModelSerializer):
    skill = SkillSerializer(many=True, read_only=True)
    education = EducationSerializer(many=True, read_only=True)
    experience = ExperienceSerializer(many=True, read_only=True)

    class Meta:
        model = Profile
        fields = ('id', 'fullname', 'email', 'phone','profile_image','address','summary_detail','skill','experience','education')
        


class StringArraySerializer(serializers.Serializer):
    items = serializers.ListField(child=serializers.CharField())
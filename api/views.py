from django.shortcuts import render
from .serializers import ProfileSerializer,StringArraySerializer,SkillSerializer,EducationSerializer, ExperienceSerializer
from .models import Task, Profile, Skill,Education, Experience
from rest_framework import generics, permissions, status, views  # New
from rest_framework.response import Response
from rest_framework.decorators import api_view

class StringArrayView(views.APIView):
    def post(self, request, *args, **kwargs):
        serializer = StringArraySerializer(data=request.data)

        if serializer.is_valid():
            # Access the validated data as a Python dictionary
            validated_data = serializer.validated_data

            # Perform any further processing with the data
            items = validated_data.get('items', [])

            return Response({'message': 'Array received successfully', 'items': items}, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ProfileListCreate(generics.ListCreateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

class ProfileDetailUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
        
# class TaskDetailUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Task.objects.all()
#     serializer_class = TaskSerializer
    

# class TaskListCreate(generics.ListCreateAPIView):
#     queryset = Task.objects.all()
#     serializer_class = TaskSerializer
    
#     # Authenticate this view
#     permission_classes = [permissions.IsAuthenticated]

URL = "http://localhost:8000/api"

@api_view(['GET'])
def apiList(request):
    api_urls = {
        'List': URL +'/profile-list/',
        'Detail View':URL + '/profile-detail/<int:pk>',
        'Create':URL + '/profile-create/',
        'Update':URL + '/profile-updates/<int:pk>',
        'Delete':URL + '/profile-delete/<int:pk>',
    }
    return Response(api_urls)

@api_view(['GET'])
def profileList(request):
    profiles = Profile.objects.all()
    serializer = ProfileSerializer(profiles, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def profileDetail(request, pk):
    profiles = Profile.objects.get(id=pk)
    serializer = ProfileSerializer(profiles, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def profileCreate(request):
    serializer = ProfileSerializer(data=request.data)
    print(serializer)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['POST'])
def profileUpdate(request, pk):
    profiles = Profile.objects.get(id=pk)
    serializer = ProfileSerializer(instance=profiles, data=request.data)
    print(serializer)

    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def profileDelete(request, pk):
    profiles = Profile.objects.get(id=pk)
    profiles.delete()
    
    return Response( "successfully delete!")



@api_view(['GET'])
def apiList(request):
    api_urls = {
        'List': URL +'/skills/',
        'Create':URL + '/skill/',
        'Update':URL + '/skill/<int:pk>',
        'Delete':URL + '/skill/<int:pk>',
    }
    return Response(api_urls)

@api_view(['GET'])
def skillList(request):
    skills = Skill.objects.all()
    serializer = SkillSerializer(skills, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def skillCreate(request):
    serializer = SkillSerializer(data=request.data)
    print(serializer)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['PATCH'])
def skillUpdate(request, pk):
    skills = Skill.objects.get(id=pk)
    serializer = SkillSerializer(instance=skills, data=request.data)
    print(serializer)

    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['DELETE'])
def skillDelete(request, pk):
    skills = Skill.objects.get(id=pk)
    skills.delete()

    return Response( " successfully delete!")


@api_view(['GET'])
def apiList(request):
    api_urls = {
        'List': URL +'/educations/',
        'Create':URL + '/education/',
        'Update':URL + '/education/<int:pk>',
        'Delete':URL + '/education/<int:pk>',
    }
    return Response(api_urls)

@api_view(['GET'])
def educationList(request):
    Educations = Education.objects.all()
    serializer = EducationSerializer(Educations, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def educationCreate(request):
    serializer = EducationSerializer(data=request.data)
    print(serializer)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['PATCH'])
def educationUpdate(request, pk):
    Educations = Education.objects.get(id=pk)
    serializer = EducationSerializer(instance=Educations, data=request.data)
    print(serializer)

    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['DELETE'])
def educationDelete(request, pk):
    Educations = Education.objects.get(id=pk)
    Educations.delete()

    return Response( " successfully delete!")

@api_view(['GET'])
def apiList(request):
    api_urls = {
        'List': URL +'/experiences/',
        'Create':URL + '/experience/',
        'Update':URL + '/experience/<int:pk>',
        'Delete':URL + '/experience/<int:pk>',
    }
    return Response(api_urls)

@api_view(['GET'])
def experienceList(request):
    Experiences = Experience.objects.all()
    serializer = ExperienceSerializer(Experiences, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def experienceCreate(request):
    serializer = ExperienceSerializer(data=request.data)
    print(serializer)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['PATCH'])
def experienceUpdate(request, pk):
    Experiences = Experience.objects.get(id=pk)
    serializer = ExperienceSerializer(instance=Experiences, data=request.data)
    print(serializer)

    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['DELETE'])
def experienceDelete(request, pk):
    Experiences = Experience.objects.get(id=pk)
    Experiences.delete()

    return Response( " successfully delete!")

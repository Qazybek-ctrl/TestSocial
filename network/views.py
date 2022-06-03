from unicodedata import category
from django.shortcuts import redirect, render
from matplotlib.pyplot import text
from matplotlib.style import context
from .models import SocialPerson, Post, PageImage, ImageFilter, Comments
from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password
from django.db import models
import requests
# Create your views here.

def profileEdit(request):
    person = SocialPerson.objects.get(user=request.user.id)

    if request.method == "POST" and 'changeFirstName' in request.POST:
        us = User.objects.get(id=request.user.id)
        firstName = request.POST['changeFirstName']
        lastName = request.POST['changeLastName']
        age = request.POST['changeAge']
        us.first_name = firstName
        us.last_name = lastName
        person = SocialPerson.objects.get(user=request.user.id)
        person.age = age
        us.save()
        person.save()

    context = {
        'isOwner': person.user.id == request.user.id,
        'error':'',
        'person':person
    }

    if request.method == 'POST' and 'currentPass' in request.POST:
        us = User.objects.get(id=request.user.id)
        currentPass = request.POST['currentPass']
        newPass1 = request.POST['newPass1']
        newPass2 = request.POST['newPass2']
        print(currentPass, " ", us.password)
        if check_password(currentPass, us.password):
            if newPass1 == newPass2:
                us.set_password(newPass1)
                us.save()
                context['error'] = "Your password succesfully changed!"
                return redirect("auth/")
            else:
                context['error'] = "New passwords aren't matching"
        else:
            context['error'] = "Your current password is wrong!"

    return render(request, 'network/edit.html', context)


def retrieveLocation(request):
    address = request.META.get('REMOTE_ADDR')
    key = '38154a99d1054c5f8563db3d404dbb25'
    url = f'https://api.ipgeolocation.io/ipgeo?apiKey={key}&ip={address}'
    r = requests.get(url).json()
    return "Almaty, Kazakshtan"


def index(request):     
    if request.method == "GET" and 'user_id' in request.GET:
        person = SocialPerson.objects.get(user=request.GET['user_id'])
    else:
        person = SocialPerson.objects.get(user=request.user.id)

    context = {
        'person': person,
        'comments':Comments.objects.filter(pageOwner=person.user.id),
        'posts' : Post.objects.filter(owner=person.user.id),
        'pageImages' : PageImage.objects.filter(owner = person.user.id),
        'filters' : ImageFilter.objects.filter(owner = person.user.id),
        'isOwner': person.user.id == request.user.id
    }

    if request.method == "POST" and 'deletePhoto' in request.POST:
        photo = PageImage.objects.get(id=request.POST['deletePhoto'])
        photo.delete()

    if request.method == "POST" and 'deletePost' in request.POST:
        post = Post.objects.get(id=request.POST['deletePost'])
        post.delete()

    if request.method == "POST" and 'addComment' in request.POST:
        if 'user_id' in request.GET:
            user = User.objects.get(id=request.GET['user_id'])
        else:
            user = User.objects.get(id=person.user.id)
        comment = Comments(
            pageOwner = user,
            commentOwner = SocialPerson.objects.get(user=request.user.id),
            text = request.POST['addComment']
        )
        comment.save()

    if request.method == 'POST' and 'DeleteComment' in request.POST:
        comment = Comments.objects.get(id=request.POST['DeleteComment'])
        comment.delete()


    try:
        context['back'] = f'background: url("{person.background.url}") top center;'
    except Exception:
        context['back'] = False

    return render(request, 'network/index.html', context)

def unauthorized_access(request):
    return render(request, 'network/unatrac.html')

def additionalSettings(request):
    person = SocialPerson.objects.get(user=request.user.id)
    
    context = {
        'isOwner' : request.user.id == person.user.id,
        'success' : '',
        'person' : person
    }

    if request.method == 'POST' and 'jobs' in request.POST:
        person = SocialPerson.objects.get(user=request.user.id)
        info = request.POST['info']
        jobs = request.POST['jobs']
        addInfo = request.POST['addInfo']
        person.info = info
        person.jobs = jobs
        person.addInfo = addInfo
        person.save()
        context['success'] = "Your informations are saved successfully"

    if request.method == "POST" and "newAvatar" in request.FILES:
        person.avatar = request.FILES['newAvatar']
        person.save()
    
    if request.method == "POST" and "newBackground" in request.FILES:
        person.background = request.FILES['newBackground']
        person.save()
    
    return render(request, 'network/settings.html', context)

def friendsPage(request):
    person = SocialPerson.objects.get(user=request.user.id)
    context = {
        'person' : person,
        'isOwner' : person.user.id == request.user.id,
        'friends' : '',
        'listofUsers' : ''
    }

    friends = []
    if person.friends != "":
        friends_id = person.friends.split(" ")
        for friend_id in friends_id:
            try:
                friends.append(SocialPerson.objects.get(id=int(friend_id)))
            except Exception:
                pass
    context['friends'] = friends

    listofUsers = []
    friendsOf = person.friends.split(" ")
    for i in range(0, 20):
        try:
            if i != person.id and str(i) not in friendsOf:
                listofUsers.append(SocialPerson.objects.get(id=i))
                print(i + " " + friendsOf)
        except Exception:
            pass
    context['listofUsers'] = listofUsers

    if request.method == 'POST' and 'addFriend' in request.POST:
        person = SocialPerson.objects.get(user=request.user.id)
        friend = SocialPerson.objects.get(id=request.POST['addFriend'])
        person1 = person.friends.split(" ")
        friend1 = friend.friends.split(" ")
        if len(person1) > 0:
            person.friends += f' {friend.id}'
        else:
            person.friends += f"{friend.id}"
        if len(friend1) > 0:
            friend.friends += f' {person.id}'
        else:
            friend.friends += f"{person.id}"
        person.save()
        friend.save()
        return redirect("friendsPage")
                      

    if request.method == 'POST' and 'DeleteFriend' in request.POST:
        idFriend = int(request.POST['DeleteFriend'])
        friend = SocialPerson.objects.get(user=idFriend)
        person = SocialPerson.objects.get(user=request.user.id)
        person1 = person.friends.split(" ")
        person2 = friend.friends.split(" ")
        person1.pop(person1.index(str(friend.id)))
        person2.pop(person2.index(str(person.id)))
        person.friends = "" + str(person1[0])
        friend.friends = "" + str(person2[0])
        for i in range(1, len(person1)):
            person.friends += f" {person1[i]}"
        for i in range(1, len(person2)):
            friend.friends += f" {person2[i]}"
        person.save()
        friend.save()
        return redirect("friendsPage")

    return render(request, 'network/friends.html', context)

def createPost(request):
    person = SocialPerson.objects.get(user=request.user.id)
    
    if request.method == 'POST' and "newPostImage" in request.FILES:
        post = Post()
        user = User.objects.get(id=request.user.id)
        post.owner = user
        post.title = request.POST['title']
        post.content = request.POST['content']
        try:
            post.postImage = request.FILES['newPostImage']
        except Exception:
            print("Post created without an image")
        post.location = retrieveLocation(request)
        post.save()

    context = {
        'person' : person        
    }
    return render(request, 'network/createPost.html', context) 

def createFilter(request):
    person = SocialPerson.objects.get(user=request.user.id)
    context = {
        'person' : person,
        'filters' : ImageFilter.objects.filter(owner=request.user),
        'isOwner' : person.user.id == request.user.id
    }

    if request.method == 'POST' and 'category' in request.POST:
        img = ImageFilter.objects.get(title=request.POST['category'], owner=request.user)
        pageImg = PageImage.objects.filter(category=request.POST['category'])
        if len(pageImg) > 0:
            for r in pageImg:
                r.delete()
        img.delete()
    
    if request.method == 'POST' and 'title' in request.POST:
        img = ImageFilter()
        img.title = request.POST['title']
        img.owner = request.user
        img.save()

    return render(request, 'network/createFilter.html', context)

def uploadPhoto(request):
    person = SocialPerson.objects.get(user=request.user.id)
    context = {
        'person' : person,
        'filters' : ImageFilter.objects.filter(owner=request.user),
        'isOwner' : person.user.id == request.user.id
    }

    if request.method == 'POST' and 'newGalleryImage' in request.FILES:
        pageImg = PageImage()
        pageImg.owner = request.user
        pageImg.title = request.POST['title']
        pageImg.location = request.POST['location']
        pageImg.image = request.FILES['newGalleryImage']
        pageImg.category = request.POST['category']
        pageImg.save()

    return render(request, 'network/uploadPhoto.html', context)
from django.shortcuts import render, redirect
from django.views import View
from classes.Administrator import Administrator
from classes.Instructor import Instructor
from classes.ta import TA
from .models import Users, Courses, Labs


# Create your views here.

class SignUp(View):

    # display sing up form
    def get(self, request):
        return render(request, "signup.html", {})

    # get user input form form
    def post(self, request):

        # variables for no existing user and bad password
        noUser = False
        badPassword = False

        # check if user exists
        try:
            m = Users.objects.get(userName=request.POST['username'])
            badPassword = (m.password1 != request.POST['pass1'])
        except:
            noUser = True

        rowCount = Users.objects.filter(group='Administrator').count()

        # if new user
        if rowCount == 0:
            # get new sign up info
            m = Users(userName=request.POST['username'], password1=request.POST['pass1'],
                      password2=request.POST['pass2'], group='Administrator')
            p1 = request.POST['pass1']
            p2 = request.POST['pass2']
            # make sure passwords are the same
            if p1 != p2:
                return render(request, "signup.html", {"message": "Passwords do not match"})
            # if passwords are the same save and redirect to login page
            else:
                m.save()
                request.session["username"] = m.userName
                return redirect('login')
        elif noUser:
            return redirect('login')
        elif badPassword:
            return render(request, "signup.html", {"message": "bad password"})
        # if user exists redirect to login page
        else:
            request.session["username"] = m.userName
            return render(request, "login.html", {"message": "You have an account. Please log in."})


class Login(View):

    # display login form
    def get(self, request):
        return render(request, "login.html", {})

    # get user input form form
    def post(self, request):

        if Administrator.check_for_existing_user(self, username=request.POST['username']):
            u = Users.objects.get(userName=request.POST['username'])
            badPass = (u.password1 != request.POST['pass1'])

            if badPass:
                return render(request, "login.html", {"message": "bad password"})
            elif u.group != 'Administrator':
                request.session["username"] = u.userName
                return redirect('userhomepage')
            else:
                request.session["username"] = u.userName
                return redirect('homepage')
        else:
            return render(request, "login.html", {"message": "Username not found. Please have the Administrator"
                                                             " create your account."})


class Homepage(View):

    # display homepage
    def get(self, request):
        return render(request, "homepage.html", {})


class UserHomepage(View):

    # display homepage
    def get(self, request):
        return render(request, "userHomepage.html", {})


class AddCourses(View):

    # display add courses page
    def get(self, request):
        return render(request, "addCourses.html", {})

    def post(self, request):
        # c = Courses(courseName=request.POST['coursename'], courseNum=request.POST['coursenum'],
        #            courseDay=request.POST['courseday'], courseTime=request.POST['coursetime'])
        # if Administrator.create_courses(coursenumber=c.courseNum, coursename=c.courseName, courseday=c.courseDay,
        #                                coursetime=c.courseTime):
        #    request.session["coursename"] = c.courseName
        #    return redirect('addcourses')
        # else:
        #    return render(request, "addCourses.html", {"message": "Course already exists."})
        if Administrator.check_for_existing_course(self, coursenumber=request.POST['coursenum']):
            return render(request, "addCourses.html", {"message": "Course already exists."})
        else:
            c = Courses(courseName=request.POST['coursename'], courseNum=request.POST['coursenum'],
                        courseDay=request.POST['courseday'], courseTime=request.POST['coursetime'])
            c.save()
            request.session["coursename"] = c.courseName
            return redirect('addcourses')


class AddUsers(View):

    # display add users page
    def get(self, request):
        return render(request, "addUsers.html", {})

    def post(self, request):
        if Administrator.check_for_existing_user(self, username=request.POST['username']):
            return render(request, "addUsers.html", {"message": "User already exists."})
        else:
            u = Users(userName=request.POST['username'], firstName=request.POST['fname'],
                      lastName=request.POST['lname'], email=request.POST['email'], password1=request.POST['pass1'],
                      group=request.POST['group'])
            u.save()
            request.session["username"] = u.userName
            return redirect('addusers')


class ViewCourses(View):
    # display add users page
    def get(self, request):
        return render(request, "", {})


class ViewUsers(View):

    # display add users page
    def get(self, request):
        return render(request, "", {})


class Assignments(View):

    # display add users page
    def get(self, request):
        return render(request, "", {})
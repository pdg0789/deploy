from django.shortcuts import render, redirect, reverse
import bcrypt
from .models import User

# Create your views here.

# def createErrorMessages(request, errors):
#     for error in errors:
#         messages.error(request, error)

def getCurrentUser(request):
    user_id = request.session['user_id']

    return User.objects.get(id=user_id)
def main(request):
    print "Inside the main method"
    return render(request, 'travel_buddy_app/main.html')

#Register User
def register(request):
    print "Inside the register method."

    if request.method == 'POST':
        errors = User.objects.register_validation(request.POST)

        if not errors:
            user = User.objects.create_user(request.POST)

            request.session['user_id'] = user.id

            return redirect(reverse('travels'))

        # createErrorMessages(request, errors)

    return redirect('/')

#Login User
def login(request):
    print "Inside the login method."

    if request.method == 'POST':
        errors = User.objects.login_validation(request.POST)

        #Check if type is a User Object
        if type(errors) == type(User()):
            user = errors #Changing the variable for clarity
            request.session['user_id'] = user.id

            return redirect(reverse('travels'))

        createErrorMessages(request, errors)

    return redirect('/')

#Logout User
def logout(request):
    print "Inside the logout method."

    request.session.pop('user_id')

    return redirect('/')

#Travels
def travels(request):
    print "Inside the travels method"
    return render(request, 'travel_buddy_app/travels.html')

#Destination
def destination(request):
    print "Inside the destination method"
    return render(request, 'travel_buddy_app/destination.html')

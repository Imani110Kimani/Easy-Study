from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from myapp.models import Students, Contact, Course
from django.http import JsonResponse
from myapp.forms import ContactForm

# Create your views here.

def register(request):
    if request.method == 'POST':
        # Retrieve data from the form
        firstName = request.POST['firstName']
        lastName = request.POST['lastName']
        email = request.POST['email']
        password = request.POST['password']

        # Check if a profile picture was uploaded
        profilePic = request.FILES.get('profilePic', None)  # Access the profile picture from request.FILES

        # Create the student instance
        student = Students(
            firstName=firstName,
            lastName=lastName,
            email=email,
            password=password,
            profilePic=profilePic,  # Save the uploaded file
        )

        student.save()  # Save the student object to the database
        return redirect('/login')  # Redirect to the login page after registration
    else:
        return render(request, 'register.html')
def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        # Check if all the required fields are present
        if not all([name, email, subject, message]):
            return HttpResponse('Missing fields', status=400)

        contact = Contact(name=name, email=email, subject=subject, message=message)
        contact.save()

        return HttpResponse('Your message has been sent. Thank you!')

    return render(request, 'contact.html')
def login(request):
    return render(request, 'login.html')


def index(request):
    if request.method == 'POST':
        # Check if username and password exist in the students model
        if Students.objects.filter(
                email=request.POST.get('email'),
                password=request.POST.get('password')
        ).exists():
            return render(request, 'index.html')  # Redirect to 'dashboard.html' if valid credentials
        else:
            # Pass an error message back to the login page
            return render(request, 'login.html')

    else:
        # Render the login page for GET requests
        return render(request, 'login.html')
def about(request):
    return render(request, 'about.html')

def courses(request):
    return render(request, 'courses.html')

def seecourse(request):
    return render(request,'course-details.html')
def events(request):
    return render(request, 'events.html')
def pricing(request):
    return render(request, 'pricing.html')
def starter(request):
    return render(request, 'starter-page.html')
def trainers(request):
    return render(request, 'trainers.html')

def search_engine(request):
    return render(request, 'search-engine-details.html')

def web_dev(request):
    return render(request, 'web-dev-details.html')


def copy_write(request):
    return render(request,'copyrighting.html')

def pay(request):
    courses = Course.objects.all()
    return render(request, 'payment-form.html', {'courses': courses})

def process_payment(request):
    if request.method == 'POST':
        course_id = request.POST.get('course_id')
        course = get_object_or_404(Course, id=course_id)
        # Add M-Pesa integration logic here
        return JsonResponse({'status': 'success', 'message': f'Payment for {course.name} submitted successfully!'})
    return JsonResponse({'status': 'error', 'message': 'Invalid request'}, status=400)

def show_contacts(request):
    allcontacts = Contact.objects.all()
    return render(request,'show_contacts.html', {'contacts': allcontacts})

def delete_contact(request,id):
    mycontact = Contact.objects.get(id=id)
    mycontact.delete()
    return redirect('/show_contacts')

def edit_contact(request,id):
   editcontact = Contact.objects.get(id=id)
   return render(request,'edit_contacts.html',{'contacting':editcontact})

def update_contact(request,id):
   update_contact= Contact.objects.get(id=id)
   contact_form = ContactForm(request.POST, instance=update_contact)
   if contact_form.is_valid():
       contact_form.save()
       return redirect('/show_contacts')
   else:
       return render(request,'edit_contacts.html')






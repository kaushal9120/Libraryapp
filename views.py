from django.shortcuts import render, redirect
from .models import Book
from .forms import BookCreate
from django.http import HttpResponse
from django.shortcuts import render,HttpResponseRedirect,reverse
from .models import *
from random import randint


#DataFlair
def index(request):
	shelf = Book.objects.all()
	return render(request, 'book/library.html', {'shelf': shelf})

def upload(request):
	upload = BookCreate()
	if request.method == 'POST':
		upload = BookCreate(request.POST, request.FILES)
		if upload.is_valid():
			upload.save()
			return redirect('index')
		else:
			return HttpResponse("""your form is wrong, reload on <a href = "{{ url : 'index'}}">reload</a>""")
	else:
		return render(request, 'book/upload_form.html', {'upload_form':upload})

def update_book(request, book_id):
	book_id = int(book_id)
	try:
		book_sel = Book.objects.get(id = book_id)
	except Book.DoesNotExist:
		return redirect('index')
	book_form = BookCreate(request.POST or None, instance = book_sel)
	if book_form.is_valid():
		book_form.save()
		return redirect('index')
	return render(request, 'book/upload_form.html', {'upload_form':book_form})

def delete_book(request, book_id):
	book_id = int(book_id)
	try:
		book_sel = Book.objects.get(id = book_id)
	except Book.DoesNotExist:
		return redirect('index')
	book_sel.delete()
	return redirect('index')

def mainpage(request):
    return render(request,"book/mainpage.html")

def loginpage(request):
    return render(request,"book/login.html")

def show(request):
    return render(request,"book/sucess.html")


def RegisterUser(request):
    try:
        if  request.POST['role'] == 'teacher':
            firstname= request.POST['firstname']
            lastname= request.POST['lastname']
            stream= request.POST['stream']
            mobile= str(request.POST['phone'])  
            city=request.POST['city']
            gender=request.POST['gender']
            birthdate= request.POST['birthdate']
            role = request.POST['role']
            password = request.POST['password']
            email = request.POST['email']
            #image=request.FILES['image']
            

 
            
            
            

            user = User.objects.filter(email=email)
            if user:
                message = 'This email already exists'
                return render(request, 'book/mainpage.html', {})
            else:
                otp=randint(100000,999999)
                newuser=User.objects.create(
                    email=email,password=password,role=role,otp=otp)
                newteacher=Teacher.objects.create(user_id=newuser,firstname=firstname,lastname=lastname,
                                                stream=stream,gender=gender,
                                                city=city,mobile=mobile,birthdate=birthdate)
                #return render(request, 'book/sucess.html', {})
                return HttpResponseRedirect(reverse('sucess'))
    
        else:
            
            firstname= request.POST['firstname']
            lastname= request.POST['lastname']
            mobile= str(request.POST['phone'])  
            city=request.POST['city']
            
            gender=request.POST['gender']
            birthdate= request.POST['birthdate']
            role = request.POST['role']
            password = request.POST['password']
            email = request.POST['email']
 
            
            
            

            user = User.objects.filter(email=email)
            if user:
                message = 'This email already exists'
                return render(request, 'book/mainpage.html', {})
            else:
                
                otp=randint(100000,999999)
                newuser=User.objects.create(
                            email=email,password=password,role=role,otp=otp)
                newteacher=Student.objects.create(user_id=newuser,firstname=firstname,lastname=lastname,
                                                gender=gender,
                                                city=city,mobile=mobile,birthdate=birthdate)
                return HttpResponseRedirect(reverse('sucess'))                
    

    
    except User.DoesNotExist:
        return render(request, 'book/mainpage.html',{})

def LoginUser(request):
    if request.POST['role']=="teacher":
        email=request.POST['email']
        password=request.POST['password']
        user=User.objects.filter(email=email)
        print(user)
        if user[0]:
                if user[0].password==password and user[0].role=='teacher':
                    teacher=Teacher.objects.filter(user_id=user[0])
                    request.session['email']=user[0].email
                    request.session['firstname']=teacher[0].firstname
    
                    request.session['lastname']=teacher[0].lastname
                    request.session['role']=user[0].role
                    request.session['id']=user[0].id

                    return HttpResponseRedirect(reverse("index"))
                else:
                    message = "Your password is incorrect or user doesn't exist'"
                    return render(request, 'book/login.html', {})
        else:
                message="user doesn't exist"
                return render(request, 'book/login.html', {})
    else:
        request.POST['role']=="student"
        email=request.POST['email']
        password=request.POST['password']
        user=User.objects.filter(email=email)
        print(user)
        if user[0]:
                if user[0].password==password and user[0].role=='student':
                    student=Student.objects.filter(user_id=user[0])
                    request.session['email']=user[0].email
                    request.session['firstname']=student[0].firstname
    
                    request.session['lastname']=student[0].lastname
                    request.session['role']=user[0].role
                    request.session['id']=user[0].id

                    return HttpResponseRedirect(reverse("index"))
                else:
                    message = "Your password is incorrect or user doesn't exist'"
                    return render(request, 'book/login.html', {})
        else:
                message="user doesn't exist"
                return render(request, 'book/login.html', {})    



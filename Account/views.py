from django.contrib.auth.models import User
from Account.forms import RegisterForm 
from django.http.response import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.http import HttpResponse, request
from django.contrib.auth import login,authenticate
from django.views.generic import View
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
# def SignUp(request):
#     if request.method=='POST':
#         #process the form data
#         form=UserForm(request.POST)
#         if form.is_valid():
#             #validate data
#             #redirect to new url
#             user=form.save()
#             login(request,user)
#             return HttpResponseRedirect('details/')
#             #return redirect('details')
    
#     else:
#         #create blan k form
#         form=UserForm(initial={'email':'@gmail.com'})
    
# #    template=loader.get_template('signup.html')
# #    context={
#  #       'form':form,
#  #   }
#   #  return HttpResponse(template.render(context,request))
#     return render(request, 'Account/signup.html',{'form':form}) 


# def Details(request):
#     if request.method=='POST':
#         form=UserDetailsForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('home')
#     else:
#         form=UserDetailsForm(initial={'username':request.user.username,'email':request.user.email})
#     return render(request, 'Account/signup.html',{'form':form})   

# class RegisterView(View):
#     form=UserCreationForm

#     def get(self,request):
#         print(request.POST)
#         context={
#             "form":self.form()
#         }
#         return render(request,"accounts/register.html",context)
    
#     def post(self,request):

#         form=self.form(request.POST)
#         if form.is_valid():
#             form.save()
#             username=form.cleaned_data.get("username")
#             password=form.cleaned_data.get("password1")
#             user=authenticate(username=username,password=password)
#             if user:
#                 login(request,user)
#                 return redirect("pages:index")

#         return render(request,"accounts/register.html",{"form":form})



def RegisterView(request):
    # if this is a POST request we need to process the form data
    template = 'account/signup.html'
   
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = RegisterForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            if User.objects.filter(username=form.cleaned_data['username']).exists():
                return render(request, template, {
                    'form': form,
                    'error_message': 'Username already exists.'
                })
            elif User.objects.filter(email=form.cleaned_data['email']).exists():
                return render(request, template, {
                    'form': form,
                    'error_message': 'Email already exists.'
                })
            elif form.cleaned_data['password'] != form.cleaned_data['password_repeat']:
                return render(request, template, {
                    'form': form,
                    'error_message': 'Passwords do not match.'
                })
            else:
                # Create the user:
                user = User.objects.create_user(
                    form.cleaned_data['username'],
                    form.cleaned_data['email'],
                    form.cleaned_data['password']
                )
                user.first_name = form.cleaned_data['first_name']
                user.last_name = form.cleaned_data['last_name']
                user.phone_number = form.cleaned_data['phone_number']
                user.save()
               
                # Login the user
                login(request, user)
               
                # redirect to accounts page:
                return HttpResponseRedirect('/')

   # No post data availabe, let's just show the page.
    else:
        form = RegisterForm()

    return render(request, template, {'form': form})
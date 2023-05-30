from django.shortcuts import render,redirect
from .models import visitors,contactus,depadmin
from django.contrib import messages
from .forms import depforms

# Create your views here.
def homepage(request):
    return render(request,'index.html')
def aboutus(request):
    return render(request,'about.html')
def signup(request):
    if request.method=='POST':
        name=request.POST["name"]
        phonenumber=request.POST["phonenumber"]
        address=request.POST["address"]
        email=request.POST["email"]
        password=request.POST["password"]
        confirmpassword=request.POST["confirmpassword"]

        emailexist=visitors.objects.filter(email=email)
        numberexist=visitors.objects.filter(phonenumber=phonenumber)
        passwordexist=visitors.objects.filter(password=password)
        if emailexist:
            messages.info(request,'This email is already exist..')
            return render(request,'registration.html')
        elif numberexist:
            messages.info(request,'number is already exist...')
            return render(request,'registration.html')
        elif passwordexist:
            messages.info(request,'password is already exist...')
            return render(request,'registration.html')
        elif password != confirmpassword:
            messages.info(request,'incorrect password...')
            return render(request,'registration.html')
        else:
            visitors(name=name,address=address,phonenumber=phonenumber,email=email,password=password,confirmpassword=confirmpassword).save()
            messages.success(request,'The user'+""+request.POST['name']+""+ 'registration succesful')
            return redirect('loginpage')
    return render(request,'registration.html')
        
def loginpage(request):
    if request.method=="POST":

        try:
            customerdetails=visitors.objects.get(email=request.POST['email'],password=request.POST['password'])
            request.session['email']=customerdetails.email
            return redirect('/')
        except visitors.DoesNotExist as e:
            messages.info(request,'invalid email')
    return render(request,'login.html')

def contactpage(request):
    if request.method=='POST':
        name=request.POST['name']
        email=request.POST['email']
        subject=request.POST['subject']
        message=request.POST['messages']
        contactus(name=name,email=email,subject=subject,messages=message).save()
        messages.info(request,"hai"+" "+request.POST['name']+" "+"Thanks for your feedback.")
    return render(request,'contact.html')

def doctorspage(request):
    return render(request,'doctor.html')

def departmentpage(request):
    departmentlist=depadmin.objects.all()
    return render(request,'departments.html',{'departmentlist':departmentlist})

def medicinepage(request,depadmin_id):

    medidetails=depadmin.objects.get(id=depadmin_id)
    
   
    return render(request,'medicines.html',{'medidetails':medidetails})

def adddep(request):
    if request.method=='POST':
        form=depforms(request.POST or None,request.FILES)
        if form.is_valid():
            try:
                form.save()
                return redirect('departmentpage')
            except:
                messages.info(request,'Invalid')

    else:
        form=depforms()
    return render(request,'formpage.html',{'form':form})

def updatedep(request,depadmin_id):
    updating=depadmin.objects.get(id=depadmin_id)
    form=depforms(request.POST or None,request.FILES,instance=updating)
    if form.is_valid():
        form.save()
        return redirect('departmentpage')
    return render(request,'update.html',{'updating':updating,'form':form})

def deletedep(request,depadmin_id):
    deleting=depadmin.objects.get(id=depadmin_id)
    deleting.delete()
    return redirect('departmentpage')






from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.views import generic
from .forms import *
from django.urls import reverse_lazy
from .models import *
from django.contrib.auth.models import User


# Create your views here.



def index(request):
    return render(request,'index.html')


class register(generic.CreateView):
    template_name = 'userregister.html'
    form_class = student
    success_url=reverse_lazy('login')

    def form_valid(self, form):
        user = form.save(commit=False)
        password = form.cleaned_data['password']
        user.set_password(password)
        user.save()
        dept = form.cleaned_data['dept']
        roll_no = form.cleaned_data['roll_no']
        reg_no = form.cleaned_data['reg_no']
        college_name = form.cleaned_data['college_name']
        phone=form.cleaned_data['phone']

        userdetails.objects.create(user=user, reg_no=reg_no, dept=dept, college_name=college_name, roll_no=roll_no,phone=phone)
        return super().form_valid(form)




from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login
from django.contrib.auth import authenticate



class studlog(generic.View):
    form_class = AuthenticationForm
    template_name ='userlogin.html'

    def get(self,request):
        form= AuthenticationForm
        return render(request,'userlogin.html',{'form':form})
    def post(self,request):
        form = AuthenticationForm(request,data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password =form.cleaned_data.get('password')
            user = authenticate(username=username,password=password)
            if user is not None:
                request.session['userid']=user.id
                login(request,user)
                return redirect("view")
            else:
                return HttpResponse('Invalid Credentials')
        else:
            return HttpResponse('Form is not valid')



from django.shortcuts import get_object_or_404

class UserprofileView(generic.DetailView):
    model = userdetails
    # userdetails model is used bcz it  provides a one to one connection with the user model
    template_name = 'userprofile.html'
    context_object_name = 'data'

    def get_object(self):
        user=self.request.user
        # userdet=userdetails.objects.filter(user_id=user_id)
        return get_object_or_404(userdetails,user=user)















# #
# class EditprofileView(generic.UpdateView):
#     model=User
#     form_class='editprofileform'
#     template_name='editprofile.html'
#     success_url=reverse_lazy('editprofile')
#
#
#
#     def get_object(self):
#         user = super().get_object() #pk there i get the object with the specific id passing into the url
#         self.userdetails_instances = userdetails.objects.get(user=user)
#         # the instance value which is used in django forms to specify which particular instance the form is pre-filled
#         # what happens is that the form is filled with the data from the particular record
#         #add your extra fields
#         self.userdetails_instances = userdetails.objects.get(user=user)
#         self.userdetails_instances = userdetails.objects.get(college_name=college_name)
#         self.userdetails_instances = userdetails.objects.get(roll_no=roll_no)
#         self.userdetails_instances = userdetails.objects.get(reg_no=reg_no)
#         self.userdetails_instances = userdetails.objects.get(dept=dept)
#         return user
#
#
#     def get_form(self, form_class=None): #view the form
#         form = super().get_form(form_class) #this step we get the form_class
#         form.fields['dept'].initial = self.userdetails_instances.dept
#         form.fields['college_name'].initial = self.userdetails_instances.college_name
#         form.fields['roll_no'].initial = self.userdetails_instances.roll_no
#         form.fields['reg_no'].initial = self.userdetails_instances.reg_no
#         form.fields['user'].initial = self.userdetails_instances.user
#         #add your extra datas
#         return form
#
#     def form_valid(self, form):
#         response = super().form_valid(form)
#         self.userdetails_instances.department = form.cleaned_data['dept']
#         self.userdetails_instances.department = form.cleaned_data['college_name']
#         self.userdetails_instances.department = form.cleaned_data['roll_no']
#         self.userdetails_instances.department = form.cleaned_data['reg_no']
#         self.userdetails_instances.department = form.cleaned_data['roll_no']
#         self.userdetails_instances.department = form.cleaned_data['user']
#
#         #save all other datas
#         self.userdetails_instances.save()
#         return response
#
#




class Bookuploadview(generic.CreateView):
    form_class = bookform
    template_name = 'bookupload.html'
    success_url = reverse_lazy('bookdisplayinuser')


class Bookdisplayview(generic.ListView):
    model = BookModel
    template_name = 'bookdisplayinuser.html'
    context_object_name = 'data'


class Bookdetailuser(generic.DetailView):
    model = BookModel
    template_name = 'bookdetailviewinuser.html'


class Libbookdisplayview(generic.ListView):
    model = BookModel
    template_name = 'bookdisplayinlibrarian.html'
    context_object_name = 'data'

class Libbookdetailview(generic.DetailView):
    model = BookModel
    template_name = 'bookdetailviewinlib.html'


class Libbookupdate(generic.UpdateView):
    model = BookModel
    template_name = 'bookupdateinlib.html'
    fields = ['book_image','book_name','genre','description','author','available_copies']
    success_url = reverse_lazy('bookdisplayviewinlib')

class Libbookdelete(generic.DeleteView):
    model = BookModel
    template_name = 'bookdeleteinlib.html'
    success_url = reverse_lazy('bookdisplayviewinlib')
#


#
# from django.shortcuts import get_object_or_404
#
# class ProfileView(generic.DetailView):
#     model = userdetails
#     template_name = 'userprofile.html'
#     context_object_name = 'profile'
#
#     def get_object(self):
#         user = self.request.user  #this is the method that is used to get the details of current logged in user
#         return get_object_or_404(userdetails,user=user)
#     #it return userdetails that matches the user datas that are logged in





#

class CreateBookRequest(generic.View):
    def get(self,request,pk):
        book= get_object_or_404(BookModel,pk=pk)  #book detsils fetching
        user_details=get_object_or_404(userdetails,user=request.user)

        #check if the user already requested this book
        if BookrequestModel.objects.filter(user=user_details,book=book).exists():
            return redirect('requestsentmessageview')
            # return HttpResponse('you have already requested this book')

        else:
            BookrequestModel.objects.create(user=user_details,book=book)
            return HttpResponse('your request has been sent')

def RequestsentmessageView(request):
    return render(request,'requestsent_message.html')


def RequestalreadysentmessageView(request):
    return render(request,'requestalreadysent_message.html')


#
class RequestedBookViewinUser(generic.ListView):
    model = BookrequestModel
    template_name = 'requested_bookviewpageinuser.html'
    context_object_name = 'requested_books'
    #you can override  your query in ListView using get_quesryset()
    #get_quesryset()--it is a fn that is used to override the List View parent class
    def get_queryset(self):
        user=self.request.user
        return BookrequestModel.objects.filter(user__user__id=user.id)



class RequestedBookViewinLib(generic.ListView):
    model = BookrequestModel
    template_name = 'requested_bookviewpageinlib.html'
    context_object_name = 'requested_books'







# class AcceptBooksRequestView(generic.View):
#     def get(self,request,pk,accepted_date=None):
#         book_request=get_object_or_404(BookrequestModel,id=pk)
#         accepted_book=AcceptedBooks.objects.create(
#         details=book_request,
#         fine=0,
#         return_date=timezone.now()+timedelta(days=10))
#
#         accepted_date=accepted_book.accepted_date
#         current_date=timezone.now()
#         return_date=accepted_date+timedelta(days=10)
#
#
#         if current_date > return_date:
#
#
#             overdue_days = (current_date - return_date).days
#             fine= overdue_days * 10
#             accepted_book.return_date=return_date
#             accepted_book.fine=fine
#         accepted_book.save()
#         # book_request.delete()
#         return HttpResponse('item accepted')
#         # return redirect(AcceptBooksView)


from datetime import datetime,timedelta
from django.utils import timezone



class AcceptBookRequestView(generic.View):
    def get(self,request,pk):
        book_request=get_object_or_404(BookrequestModel,id=pk)

        #create the accepted book entry
        AcceptedBooksModel.objects.create(
            book_name=book_request.book.book_name,
            author=book_request.book.author,
            requested_date=book_request.requested_date,
            userdetails=book_request.user,
            return_date=timezone.now() + timedelta(days=10)

        )
        #deelte the BookRewqest instance
        book_request.delete()

        return redirect('requestedbookviewpageinlib')






class AcceptBooksView(generic.ListView):
    model=AcceptedBooksModel
    template_name='Acceptedbooksview.html '
    context_object_name = 'data'

    def get_queryset(self):
        queryset=super().get_queryset()  #objects.all()is the quesry to get
        current_date=timezone.now()


        #data preprocess

        for accepted_book in queryset:
            if current_date > accepted_book.return_date:
                overdue_days=(current_date - accepted_book.return_date).days
                accepted_book.fine=overdue_days * 10
            else:
                accepted_book.fine = 0

            accepted_book.save() #save the calculated fine if you want to store it
        return queryset


from django.contrib.auth import logout

class LogoutView(generic.View):
    def get(self,request):
        logout(request)
        return redirect('index')



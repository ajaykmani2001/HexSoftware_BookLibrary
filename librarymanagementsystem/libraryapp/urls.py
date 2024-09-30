from django.urls import path
from .views import *


urlpatterns=[
    path('index/',index,name='index'),
    path('userreg/',register.as_view(),name='reg'),
    path('userlog/',studlog.as_view(),name='login'),
    path('userprofile/',UserprofileView.as_view(),name='view'),
    # path('editprofile/<pk>',EditprofileView.as_view(),name='editprofile'),
    path('bookupload/',Bookuploadview.as_view(),name='bookupload'),

    path('bookdisplayinuser/',Bookdisplayview.as_view(),name='bookdisplayinuser'),
    path('bookdetailviewinuser/<pk>', Bookdetailuser.as_view(), name='detailviewinuser'),
    path('bookdisplayviewinlib/',Libbookdisplayview.as_view(),name='bookdisplayviewinlib'),
    path('bookdetailviewinlib/<pk>',Libbookdetailview.as_view(),name='bookdetailviewinlib'),
    path('bookupdateinlib/<pk>',Libbookupdate.as_view(),name='bookupdateinlib'),
    path('bookdeleteinlib/<pk>',Libbookdelete.as_view(),name='bookdeleteinlib'),
    path('createbookrequest/<pk>',CreateBookRequest.as_view(),name='createbookrequest'),
    path('requestedbookviewpageinuser/',RequestedBookViewinUser.as_view(),name='requestedbookviewpageinuser'),
    path('requestedbookviewpageinlib/',RequestedBookViewinLib.as_view(),name='requestedbookviewpageinlib'),
    path('acceptbookrequest/<pk>',AcceptBookRequestView.as_view(),name='acceptbookrequest'),
    path('acceptedbooksview/',AcceptBooksView.as_view(),name='acceptedbooksview'),
    path('requestsentmessageview/',RequestsentmessageView,name='requestsentmessageview'),
    path('logout/',LogoutView.as_view(),name='logout')


]







    #
    # path('bookreequest/<pk>',BookRequest.as_view(),name='bookrequest'),



from django.contrib.auth import user_logged_in 
from django.contrib.auth.models import User 
from django.dispatch import receiver 



@receiver(user_logged_in , sender=User )
def login_success(sender , request , user , **kwargs):
    # print("------------------------------------") not write in production 
    # print("----------logged in signals ... run intro ")
    # geeting ip with request 
    ip = request.META.get('REMOTE_ADDR') # we can store it / or we set into a session so we can easily get it into template 
    # print("client" , ip )
    request.session['ip']= ip
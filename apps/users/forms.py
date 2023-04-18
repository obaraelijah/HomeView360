from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from .models import User

class CustomCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = User
        fields = ["email", "username", "first_name", "last_name"]
        error_class = "error"
        
        
class CustomCreationForm(UserChangeForm):
    class Meta:
        model = User
        fields = ["email", "username", "first_name", "last_name"]
        error_class = "error"

        
    
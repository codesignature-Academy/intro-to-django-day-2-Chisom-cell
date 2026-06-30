from django.shortcuts import HttpResponse

def home(request):
    return HttpResponse("<h1>Welcome to Chronicles of Calm 🕊️📝")

def about(request):
    return HttpResponse("""  
Documenting life, practicing mindfulness, and finding beauty in the everyday.  
Pause for a moment. Write it down. Let it settle.  
Breathe in. Write it out. Let it go.
  
Join the community and start your journaling ritual today.  
""")
    
def contact(request):
    return HttpResponse("<h1>Email: hello@chroniclesofcalm")
# Create your views here.

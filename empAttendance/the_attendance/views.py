from django.shortcuts import render
from the_attendance.models import Attend

#def the_attendance(request):
#   return render(request, 'attendance.html', {})
def attend_index(request):
    the_attendance = Attend.objects.all()

    
    context = {
        'the_attendance': the_attendance
    }
    return render(request, 'attend_index.html', context)



# Create your views here.

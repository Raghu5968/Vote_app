from django.shortcuts import render,redirect,get_object_or_404

from .forms import *

from .models import *

from django.contrib import messages
from django.contrib.auth.models import Group

from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required

from django.http import HttpResponseRedirect
from django.urls import reverse
from django.http import JsonResponse

# Create your views here.

def index(request):
    return render(request,'index.html')
def about(request):
    return render(request,"about.html")
def contact(request):
    return render(request,"contact.html")

def registerpage(request):
    if request.user.is_authenticated:
        return redirect('votingpage')
    else:
        form=CreateUserForm()
        if request.method=='POST':
            form=CreateUserForm(request.POST)
            if form.is_valid():
                user=form.save()
                username=form.cleaned_data.get('username')
                group=Group.objects.get(name='voters')
                user.groups.add(group)
                Voter.objects.create(user=user,username=user.username,email=user.email)
                messages.success(request,'User Successfully created for '+username)
                return redirect('registerpage')
    context={'form':form}        
    return render(request,'registration.html',context)


def loginpage(request):
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        user =authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('/') 
        else:
            messages.info(request,'username or password error')
            print("username or password error ")
            return redirect('loginpage')
    return render(request,'login.html')

def logoutpage(request):
    logout(request)
    return redirect('/')

def votingpage(request):
    candidates=Candidate.get_all_candidates()
    context={'candidates':candidates}
    return render(request,'votingpage.html',context)

# multiple votes

# def vote(request, candidate_id):
#     try:
#         candidate = Candidate.objects.get(pk=candidate_id)
#         if request.method == 'POST':
#             vote_instance = Vote(candidate=candidate, user=request.user)
#             vote_instance.save()
#             candidate.total_votes += 1
#             candidate.save()

#             messages.success(request, f"You have successfully voted for {candidate.candidatename}.")
#             return redirect('votingpage')

#         return render(request, 'votingpage.html', {'candidate': candidate})
#     except Candidate.DoesNotExist:
#         messages.error(request, "Candidate not found.")
#         return redirect('votingpage')
# def vote(request, candidate_id):
#     try:
#         candidate = Candidate.objects.get(pk=candidate_id)
#         user = request.user

#         # Check if the user has already voted for this candidate
#         if Vote.objects.filter(candidate=candidate, user=user).exists():
#             messages.warning(request, f"You have already voted.")
#             return redirect('votingpage')

#         if request.method == 'POST':
#             vote_instance = Vote(candidate=candidate, user=user)
#             vote_instance.save()
#             candidate.total_votes += 1
#             candidate.save()

#             messages.success(request, f"You have successfully voted .")
#             return redirect('votingpage')

#         return render(request, 'votingpage.html', {'candidate': candidate})
#     except Candidate.DoesNotExist:
#         messages.error(request, "Candidate not found.")
#         return redirect('votingpage')



# from django.db import transaction
# from django.http import JsonResponse

# def vote(request, candidate_id):
#     try:
#         candidate = Candidate.objects.get(pk=candidate_id)
#         user = request.user

#         # Check if the user has already voted for this candidate
#         if Vote.objects.filter(candidate=candidate, user=user).exists():
#             messages.warning(request, f"You have already voted for {candidate.candidatename}.")
#             return redirect('votingpage')

#         if request.method == 'POST':
#             with transaction.atomic():
#                 vote_instance = Vote(candidate=candidate, user=user)
#                 vote_instance.save()
#                 candidate.total_votes += 1
#                 candidate.save()

#             # Show a success message with SweetAlert2
#             success_message = f"You have successfully voted for {candidate.candidatename}."
#             script = f"Swal.fire('Success!', '{success_message}', 'success');"

#             return render(request, 'votingpage.html', {'candidate': candidate, 'popup_script': script})

#         return render(request, 'votingpage.html', {'candidate': candidate})
#     except Candidate.DoesNotExist:
#         messages.error(request, "Candidate not found.")
#         return redirect('votingpage')

from django.db import transaction
from django.http import JsonResponse

def vote(request, candidate_id):
    try:
        candidate = Candidate.objects.get(pk=candidate_id)
        user = request.user

        # Check if the user has already voted for any candidate
        if Vote.objects.filter(user=user).exists():
            messages.warning(request, "You have already voted..")
            return redirect('votingpage')

        if request.method == 'POST':
            # Check if the user has already voted for this specific candidate
            if Vote.objects.filter(candidate=candidate, user=user).exists():
                messages.warning(request, f"You have already voted for {candidate.candidatename}.")
                

            with transaction.atomic():
                vote_instance = Vote(candidate=candidate, user=user)
                vote_instance.save()
                candidate.total_votes += 1
                candidate.save()

            # Show a success message with SweetAlert2
            # success_message = f"You have successfully voted for {candidate.candidatename}."
            # script = f"Swal.fire('Success!', '{success_message}', 'success');"

            # return render(request, 'votingpage.html', {'candidate': candidate,'success_message':success_message})
        messages.warning(request, f"You have successfully voted for {candidate.candidatename}")
        return redirect('votingpage')
    except Candidate.DoesNotExist:
        messages.error(request, "Candidate not found.")
        return redirect('votingpage')




    
def admin_dashboard(request):
    votes=Vote.objects.all()
    candidates = Candidate.objects.all()
    total_votes=votes.count()


    candidates_with_votes = []
    for candidate in candidates:
        candidate.total_votes = Vote.objects.filter(candidate=candidate).count()
        candidates_with_votes.append(candidate)

    context = {
        'candidates': candidates_with_votes,'total_votes':total_votes
    }
    return render(request, 'admin_dashboard.html', context)


def Feedback(request):
    if request.method == 'POST':
        form = feedbackform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contact')
    else:
        form = feedbackform()

    return render(request, 'feedback.html', {'form': form})
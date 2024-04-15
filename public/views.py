from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import TemplateView,View,CreateView,ListView
from public.forms import UserGarbageBinForm,ComplaintForm,userform
from my_work.models import Area, UserGarbageBin,Complaint, CollectionRequest,GarbageBin,RequestTable
from django.urls import reverse_lazy
from django.contrib import messages



class HomePage(TemplateView):
    template_name="public/home.html"




class RequestBin(CreateView):
    template_name='public/bin_request.html'
    form_class=UserGarbageBinForm
    model=UserGarbageBin
    success_url=reverse_lazy('home_2')

    def form_valid(self, form):
        form.instance.user=self.request.user
        return super().form_valid(form)
              
    
class PendingRequestsView(View):
    def get(self, request):
        pending_requests = UserGarbageBin.objects.filter(status=' pending')
        return render(request, "public/request_details.html", {"pending_requests": pending_requests})

class AcceptRequestView(View):
    def post(self, request, pk):
        user_garbage_bin = get_object_or_404(UserGarbageBin, pk=pk)
        user_garbage_bin.status = 'accepted'
        user_garbage_bin.save()   
        return redirect('pending_requests')

class RejectRequestView(View):
    def post(self, request, pk):
        user_garbage_bin = get_object_or_404(UserGarbageBin, pk=pk)
        user_garbage_bin.status = 'rejected'
        user_garbage_bin.save()
        return redirect('pending_requests')
    
def pending_requests_view(request):
    pending_requests = UserGarbageBin.objects.filter(status='pending')
    return render(request, 'public/pending_requests.html', {'pending_requests': pending_requests})



def send_complaint(request):
    if request.method == 'POST':
        issue = request.POST.get('issue', '')
        if issue:
            complaint = Complaint.objects.create(user=request.user, issue=issue)
            messages.success(request, 'Complaint sent successfully!')
            return redirect('home_2')  
        else:
            messages.error(request, 'Please provide an issue for the complaint.')
    return render(request, 'public/send_complaint.html')  

def view_complaint(request, complaint_id):
    complaint = Complaint.objects.get(id=complaint_id)
    if request.user == complaint.user:  
        return render(request, 'public/view_complaint.html', {'complaint': complaint})
    else:
        messages.error(request, 'You are not authorized to view this complaint.')
        return redirect('home_2')  


def accept_complaint(request, complaint_id):
    complaint = Complaint.objects.get(id=complaint_id)
    if request.method == 'POST':
        complaint.accepted = True
        complaint.save()
        messages.success(request, 'Complaint accepted successfully!')
        return redirect('home_2')  
    return render(request, 'public/accept_complaint.html', {'complaint': complaint})


def reject_complaint(request, complaint_id):
    complaint = Complaint.objects.get(id=complaint_id)
    if request.method == 'POST':
        complaint.rejected = True
        complaint.save()
        messages.success(request, 'Complaint rejected successfully!')
        return redirect('home_2')  
    return render(request, 'public/reject_complaint.html', {'complaint': complaint})



def list_complaints(request):
    user_complaints = Complaint.objects.filter(user=request.user)
    return render(request, 'public/list_complaints.html', {'user_complaints': user_complaints})




from django.db.models import F

class CollectionRequestDetailView(TemplateView):
    template_name = 'public/detailstemplate.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user_location = self.request.user.location  
        user_id = self.request.user.id
        bins = UserGarbageBin.objects.filter(user=user_id)
    
        for i in bins:
            collection_requests = CollectionRequest.objects.filter(
                area=user_location, 
                bin_id=i.bin.id
        )

        context['collection_request'] = collection_requests
        return context



class ConformRequest(CreateView):
    template_name = 'public/collection_conform.html'
    form_class = userform
    model = RequestTable
    success_url = reverse_lazy('home_2')

    def form_valid(self, form):
        id = self.kwargs.get('pk')
        form.instance.user = self.request.user
        form.instance.request_id = id  
        return super().form_valid(form)
    


class Taskupdate(View):
    def get(self,request,*args,**kwargs):
        form=userform()
        id=kwargs.get("pk")
        qs=RequestTable.objects.get(id=id)
        if qs.result == True:
            qs.result = False
            qs.save()
        # elif qs.result == False:
        #     qs.result = True
        #     qs.save()
        return redirect("home_2")
    




# class CollectionRequestDetailView(TemplateView):
#     template_name = 'public/conform.html'
    
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         user_location = self.request.user.location  
#         user_id = self.request.user.id
#         bins = UserGarbageBin.objects.filter(user=user_id)
    
#         for i in bins:
#             collection_requests = CollectionRequest.objects.filter(
#                 area=user_location, 
#                 bin_id=i.bin.id
#         )

#         context['collection_request'] = collection_requests
#         return context




    




    







        





   



    













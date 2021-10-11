from Account.models import User
from django import forms
from Notes.models import createnotes
from django.shortcuts import redirect, render
from Notes.form import NoteForm
from django.http.response import HttpResponseNotFound
from django.views.generic import FormView,ListView,UpdateView,DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def welcomenote_view(request):
    #firstNotes=notes.objects.get(pk=1)
    user=request.user
    filterNotes=createnotes.objects.filter(user_id=user.id)
   # allNotes=createnotes.objects.all().order_by("updated_at").reverse()
    return render(request,'Notes/homenotepage.html',{'object_list':filterNotes})



def product_details_view(request,pk:int):
    try:
        user=request.user
        createnote=createnotes.objects.get(id=pk,user_id=user.id)
    except createnotes.DoesNotExist:
        return HttpResponseNotFound()    
    return render(request,"Notes/notes_detail.html",{"object":createnote})




class NotesListView(ListView,LoginRequiredMixin):
    model=createnotes
    template_name="Notes/homenotepage.html"
    paginate_by=3    
    def get_queryset(self):
        user=self.request.user
        return createnotes.objects.filter(user_id=user.id).order_by('-created_date')

class NotesFormView(FormView,LoginRequiredMixin):

    template_name="notes/createnote.html"
    form_class=NoteForm
    success_url="/notes/"



    def form_valid(self, form):
                      
        instance=form.save()
        print(instance.user_id)
        
        user=self.request.user
        instance.user_id=user.id
        

        print(user.id) 
        #pk=instance.id
        instance.save()
        #return super().form_valid(form)
        #return redirect(request,"products/product_detail.html",{"object":product})
        return redirect("notes:welcomenote")


    # def createnote_view(request):
    #     print ("hello")
    #     return render(request,'Notes/createnote.html')


class NotesUpdateView(UpdateView,LoginRequiredMixin):
    model = createnotes
    fields = ["title","text","image"]
    template_name="notes/createnote.html"
    success_url="/notes/"

class NotesDeleteView(DeleteView,LoginRequiredMixin):
    model=createnotes
    success_url="/notes/"
    
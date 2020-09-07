from .forms import ContactForm, FormBornout, FormConsent
from django.views.generic.edit import FormView
from django.shortcuts import redirect, render
from django.urls import reverse_lazy , reverse

class ConsentiView(FormView):
    template_name = 'formv/consent.html'
    form_class = FormConsent
   
    success_url = 'contact'
  

class ContactView(FormView):
    template_name = 'formv/valid.html'
    form_class = ContactForm
    success_url = '../bornout'
    

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        form.send_email()
        return super().form_valid(form)

def BornoutView(request):
    bform = FormBornout()
    if request.method == 'POST':
        var1 = request.POST.get('que1','')
        var2 = request.POST.get('que2','')
        var3 = request.POST.get('que3','')
        var4 = request.POST.get('que4','')
        var5 = request.POST.get('que5','')
        var6 = request.POST.get('que6','')
        var7 = request.POST.get('que7','')
        var8 = request.POST.get('que8','')
        var9 = request.POST.get('que9','')
        var10 = request.POST.get('que10','')
        var11 = request.POST.get('que11','')
        var12 = request.POST.get('que12','')
        var13 = request.POST.get('que13','')
        var14 = request.POST.get('que14','')
        var15 = request.POST.get('que15','')
        var16 = request.POST.get('que16','')
        var17 = request.POST.get('que17','')
        var18 = request.POST.get('que18','')
        var19 = request.POST.get('que19','')
        var20 = request.POST.get('que20','')
        var21 = request.POST.get('que21','')
        var22 = request.POST.get('que22','')
        
        res = int(var1)+int(var2)+int(var3)+int(var4)+int(var5)+int(var6)+int(var7)+int(var8)+int(var9)+int(var10)+int(var11)+int(var12)+int(var13)+int(var14)+int(var15)+int(var16)+int(var17)+int(var18)+int(var19)+int(var20)+int(var21)+int(var22)

        print(res)
        return redirect(reverse('modules1')+'?'+str(res))
    return render(request, 'formv/formBornout.html',{'form':bform})
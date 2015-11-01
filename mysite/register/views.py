from django.shortcuts import render

# Create your views here.
def register(request):
    if request.method == 'POST':
        uf = UserForm(request.POST, prefix='user')
        upf = UserProfileForm(request.POST, prefix='userprofile')
        if uf.is_valid() * upf.is_valid():
            user = uf.save()
            userprofile = upf.save(commit=False)
            userprofile.user = user
            userprofile.save()
            return django.http.HttpResponseRedirect(…something…)
    else:
        uf = UserForm(prefix='user')
        upf = UserProfileForm(prefix='userprofile')
    return django.shortcuts.render_to_response('register.html', 
                                               dict(userform=uf,
                                                    userprofileform=upf),
                                               context_instance=django.template.RequestContext(request))

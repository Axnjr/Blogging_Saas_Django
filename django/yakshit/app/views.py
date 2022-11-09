from http.client import HTTPResponse
from django.shortcuts import render , redirect , get_object_or_404
#from django.http import HttpResponse , Http404 ,HttpResponseRedirect , JsonResponse
#from django.views.decorators.csrf import csrf_exempt
#from .models import Blog , Mailing_list , Categories , Question #, Comment
from django.contrib import messages
from django.contrib.auth import authenticate , login , logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .models import Videos

#SIGN UP VIEW FUNCTION

def sign(request):
    if request.method == 'POST':
        f = UserCreationForm(request.POST)
        if f.is_valid():
            f.save()
            user_n = f.cleaned_data['username']
            user_pass = f.cleaned_data['password1']
            user = authenticate(username=user_n,password=user_pass)
            login(request,user)
            return redirect('/')
        else:
            err = "An error occured pls try again..."
            return render(request,'sign.html',{'form':f,'err':err})
    else:
        f = UserCreationForm(request.POST)
        messages.info(request, 'Three credits remain in your account.')
        return render(request,'sign.html',{'form':f})

# LOGIN VIEW FUNCTION

def log(request):
    if request.method == 'POST':
        user_n = request.POST['user_n']
        user_pass = request.POST['user_pass']
        us = authenticate(username=user_n,password=user_pass)
        if us:
            login(request,us)
            return redirect('/')
        else:
            return redirect('sign')
    else:
        return render(request,'login.html')

@login_required
def log_out(request):
    logout(request)
    return redirect('/')

def load_database(request):
    lis =   """
    https://www.youtube.com/watch?v=I3091K49RXc
    https://www.youtube.com/watch?v=I3091K49RXc
    https://www.youtube.com/watch?v=SVvr3ZjtjI8
    https://www.youtube.com/watch?v=UXsomnDkntI
    https://www.youtube.com/watch?v=Zdcth9NndEA
    https://www.youtube.com/watch?v=mvNaGlFPjfc
    https://www.youtube.com/user/lalgovinddaschannel1
    https://www.youtube.com/watch?v=Mpr-xdDtIOQ
    https://www.youtube.com/watch?v=UQffgnJ8N6k
    https://www.youtube.com/watch?v=PmlRbfSavbI
    https://www.youtube.com/watch?v=QKlgJRWTwvc
    https://www.youtube.com/watch?v=QKlgJRWTwvc
    https://www.youtube.com/watch?v=oPK2PuIQC1w
    https://www.youtube.com/watch?v=oPK2PuIQC1w
    https://www.youtube.com/c/Aniruddhacharyaji
    https://www.youtube.com/watch?v=d8pJkuSp1iI
    https://www.youtube.com/user/MrBeast6000
    https://www.youtube.com/watch?v=h2VmL2Q6WNU
    https://www.youtube.com/watch?v=vyqbNFMDRGQ
    https://www.youtube.com/c/ChrisCourses
    https://www.youtube.com/watch?v=nrIqDr0qetI
    https://www.youtube.com/watch?v=nrIqDr0qetI
    https://www.youtube.com/c/Awlecs
    https://www.youtube.com/watch?v=BtO52EDi7Fs
    https://www.youtube.com/watch?v=BtO52EDi7Fs
    https://www.youtube.com/c/ThatsAmazing
    https://www.youtube.com/watch?v=4Slg41svR3A
    https://www.youtube.com/watch?v=4Slg41svR3A
    https://www.youtube.com/c/SADHNAGOLD
    https://www.youtube.com/watch?v=JZocTmtOn30
    https://www.youtube.com/watch?v=JZocTmtOn30
    https://www.youtube.com/c/KaraandNate
    https://www.youtube.com/watch?v=Nauz59NC1jM
    https://www.youtube.com/watch?v=Nauz59NC1jM
    https://www.youtube.com/watch?v=TIe2oerd25c
    https://www.youtube.com/watch?v=TIe2oerd25c
    https://www.youtube.com/c/veritasium
    https://www.youtube.com/watch?v=hyHcWI16ujY
    https://www.youtube.com/watch?v=hyHcWI16ujY
    https://www.youtube.com/c/ZachKingVine
    https://www.youtube.com/watch?v=CG__N4SS1Fc
    https://www.youtube.com/watch?v=CG__N4SS1Fc
    https://www.youtube.com/kepowob
    https://www.youtube.com/watch?v=3TDn9a0e6qA
    https://www.youtube.com/watch?v=3TDn9a0e6qA
    https://www.youtube.com/c/theHacksmith
    https://www.youtube.com/watch?v=VyV3aj2-PmM
    https://www.youtube.com/watch?v=VyV3aj2-PmM
    https://www.youtube.com/c/VishnuSharmaAjmer
    https://www.youtube.com/watch?v=8JJ101D3knE
    https://www.youtube.com/watch?v=8JJ101D3knE
    https://www.youtube.com/c/programmingwithmosh
    https://www.youtube.com/watch?v=TDiXxsQ0w2Q
    https://www.youtube.com/watch?v=TDiXxsQ0w2Q
    https://www.youtube.com/user/MrBeast6000
    https://www.youtube.com/watch?v=jtFmBhSx2hE
    https://www.youtube.com/watch?v=jtFmBhSx2hE
    https://www.youtube.com/c/TheSupaStrikas
    https://www.youtube.com/watch?v=CJkKDX8SXuY
    https://www.youtube.com/watch?v=CJkKDX8SXuY
    https://www.youtube.com/c/FidiasPanayiotou
    https://www.youtube.com/watch?v=tx2R2YRL3E8
    https://www.youtube.com/watch?v=tx2R2YRL3E8
    https://www.youtube.com/channel/UCJPb_8895oKoRPXexDd4J3w
    https://www.youtube.com/watch?v=wgiW1uFZYr8&t=1s
    https://www.youtube.com/watch?v=wgiW1uFZYr8&t=1s
    https://www.youtube.com/c/CSDojo
    https://www.youtube.com/watch?v=zMVwpn4UZ5Q
    https://www.youtube.com/watch?v=zMVwpn4UZ5Q
    https://www.youtube.com/c/SADHNAGOLD
    https://www.youtube.com/watch?v=SdL55HWNPRM
    https://www.youtube.com/watch?v=SdL55HWNPRM
    https://www.youtube.com/c/JaredOwen
    https://www.youtube.com/watch?v=nz3ZJ8IU-lo
    https://www.youtube.com/watch?v=nz3ZJ8IU-lo
    https://www.youtube.com/c/DesignCourse
    https://www.youtube.com/watch?v=_6RBgBhpKAc
    https://www.youtube.com/watch?v=_6RBgBhpKAc
    https://www.youtube.com/c/HoustonIskcon
    https://www.youtube.com/watch?v=PKtnafFtfEo
    https://www.youtube.com/watch?v=PKtnafFtfEo
    https://www.youtube.com/user/MrBeast6000
    https://www.youtube.com/watch?v=xHxW8UvwrKc
    https://www.youtube.com/watch?v=xHxW8UvwrKc
    https://www.youtube.com/c/ColinAmazing
    https://www.youtube.com/watch?v=48sCx-wBs34
    https://www.youtube.com/watch?v=48sCx-wBs34
    https://www.youtube.com/c/veritasium
    https://www.youtube.com/watch?v=uklQx6-maIs
    https://www.youtube.com/watch?v=uklQx6-maIs
    https://www.youtube.com/user/lalgovinddaschannel1
    https://www.youtube.com/watch?v=rq8cL2XMM5M
    https://www.youtube.com/watch?v=rq8cL2XMM5M
    https://www.youtube.com/c/Coreyms
    https://www.youtube.com/watch?v=8F1J51GSPYY
    https://www.youtube.com/watch?v=8F1J51GSPYY
    https://www.youtube.com/c/BeastReacts
    https://www.youtube.com/watch?v=gAJmz50yb2w
    https://www.youtube.com/watch?v=gAJmz50yb2w
    https://www.youtube.com/c/hitaambrish
    https://www.youtube.com/watch?v=4Ey7GI7jn1o
    https://www.youtube.com/watch?v=4Ey7GI7jn1o
    https://www.youtube.com/c/GodhamPathmedaOfficial
    https://www.youtube.com/watch?v=yEKtJGha3yM
    https://www.youtube.com/watch?v=yEKtJGha3yM
    https://www.youtube.com/c/akshaymarch7
    https://www.youtube.com/watch?v=7bmcjp8TVo8
    https://www.youtube.com/watch?v=7bmcjp8TVo8
    https://www.youtube.com/channel/UCSZDbqcilUCANp96e1-AS1g
    https://www.youtube.com/watch?v=DuQbOQwVaNE
    https://www.youtube.com/watch?v=DuQbOQwVaNE
    https://www.youtube.com/user/MrBeast6000
    https://www.youtube.com/watch?v=nMkW5JXyclg
    https://www.youtube.com/watch?v=nMkW5JXyclg
    https://www.youtube.com/c/PeekabooKids
    https://www.youtube.com/watch?v=PKwu15ldZ7k
    https://www.youtube.com/watch?v=PKwu15ldZ7k
    https://www.youtube.com/c/WebDevSimplified
    https://www.youtube.com/watch?v=HPtesL6nxTk
    https://www.youtube.com/watch?v=HPtesL6nxTk
    https://www.youtube.com/c/RadhakrishnaJiMaharaj
    https://www.youtube.com/watch?v=qlsQbTPduAU
    https://www.youtube.com/watch?v=qlsQbTPduAU
    https://www.youtube.com/channel/UCGT-UX074p3xUbibCpNAg_A
    https://www.youtube.com/watch?v=2ktgs-JKoWk
    https://www.youtube.com/watch?v=2ktgs-JKoWk
    https://www.youtube.com/c/FidiasPanayiotou
    https://www.youtube.com/watch?v=M0_U1FHwACk
    https://www.youtube.com/watch?v=M0_U1FHwACk
    https://www.youtube.com/c/MarkRober
    https://www.youtube.com/watch?v=0NGWT9COcEI
    https://www.youtube.com/watch?v=0NGWT9COcEI
    https://www.youtube.com/user/MrBeast6000
    https://www.youtube.com/watch?v=pTnEG_WGd2Q
    https://www.youtube.com/watch?v=pTnEG_WGd2Q
    https://www.youtube.com/c/TheMathSorcerer
    https://www.youtube.com/watch?v=7UNWrkkD3BQ
    https://www.youtube.com/watch?v=7UNWrkkD3BQ
    https://www.youtube.com/channel/UC-UT5nVET2QpkS2pOk6bi6A
    https://www.youtube.com/watch?v=Rv6RQqrSlYg
    https://www.youtube.com/watch?v=Rv6RQqrSlYg
    https://www.youtube.com/user/seanscrafts
    https://www.youtube.com/watch?v=pYrKeJbjbsM
    https://www.youtube.com/watch?v=pYrKeJbjbsM
    https://www.youtube.com/c/LakshyaTvchannel
    https://www.youtube.com/watch?v=XE9pUM9MEFA
    https://www.youtube.com/watch?v=XE9pUM9MEFA
    https://www.youtube.com/user/MrBeast6000
    https://www.youtube.com/watch?v=abbdJ4Yfm54
    https://www.youtube.com/watch?v=8IljDF-seBQ
    https://www.youtube.com/channel/UCQSorv0AJj2S3TD7DejHA8A
    https://www.youtube.com/watch?v=yyE1RTsFqwo
    https://www.youtube.com/user/lalgovinddaschannel1
    https://www.youtube.com/watch?v=Lww6AJaGFrM
    https://www.youtube.com/watch?v=Qf-D1Upn-KU
    https://www.youtube.com/watch?v=7iNZLNwZod8 """ 
    res = []
    r = lis.split()
    r = list(dict.fromkeys(r))
    for x in r :
        res.append(x.replace("https://www.youtube.com/watch?v=","https://www.youtube.com/embed/"))
    for w in res:
        y = w.replace("https://www.youtube.com/c/","")
        z = w.replace("https://www.youtube.com/user/","")
        q = w.replace("https://www.youtube.com/channel/","")
        if len(y) < 30:
            res.remove(w)
        if len(z) < 30:
            res.remove(w)
        if len(q) < 30:
            res.remove(w)
    for i in range(len(res)-1):
        added_link = Videos.objects.create(link_to_vid = res[i])  
        added_link.save()
    return redirect('/')

def home(request):
    con = Videos.objects.order_by("link_to_vid")[:1]
    content = {'con':con}
    return render(request,'index.html',content)
from ast import Try
from functools import total_ordering
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .forms import usersform
from service.models import Service
from enquire.models import Enquire
from news.models import News
from django.core.paginator import Paginator
from django.core.mail import send_mail, EmailMultiAlternatives


def HomePage(request):
    """
    send mail with html code
    """
    """subject = 'testing django mail'
    from_email='chandradutt.patel@geta-job.com'
    msg='<p>welcome to your <b>website</b></p>'
    to='chandradutt1999@gmail.com'
    msg=EmailMultiAlternatives(subject, msg, from_email, [to])
    msg.content_subtype='html'
    msg.send()"""

    """send only mail"""
    """send_mail(
        'Testind Mail',
        'message show',
        'chandradutt.patel@geta-job.com',
        ['chandradutt1999@gmail.com'],
        fail_silently=False
    )"""
    """
        Search services 
    """
    # __icontains means search the item by every character
    servicedata = Service.objects.all()
    if request.method == 'GET':
        st = request.GET.get('servicename')
        if st != None:
            servicedata = Service.objects.filter(service_title__icontains=st)

    ServiceData = Service.objects.all()
    paginator = Paginator(ServiceData, 2)
    page_number = request.GET.get('page')
    servicedatafinal = paginator.get_page(page_number)
    totalpage = servicedatafinal.paginator.num_pages
    """
    search complete
    """


    """
    Getting News
    """

    newsdata = News.objects.all()
    """
    completed news
    """

    """
    Pagination code
    """
    # ServiceData = Service.objects.all()
    # paginator = Paginator(ServiceData, 2)
    # page_number = request.GET.get('page')
    # servicedatafinal = paginator.get_page(page_number)
    data = {
        # 'title': 'Home Page',
        # 'list':['Python', 'Django', 'HTML'],
        # 'student_details': [
        #     {'name':'chandradutt', 'phone':'1234567890'},
        #     {'name':'dipak', 'phone':'1233423212'},
        #     ],
        # 'numbers': [3,4,2,4,-2,-7,-1],
        # 'num': [-1,-2,-3]
        'servicedata': servicedatafinal,
        'newsdata': newsdata,
        'lastpage': totalpage,
        'totalpagelist': [n+1 for n in range(totalpage)]
        # 'servicedatafinal': servicedatafinal,
    }
    #print icon start
    servicedata = Service.objects.all().order_by('service_icon')
    for a in servicedata:
        print(a.service_icon)

    # print icon stop
    return render(request, "homepage.html", data)

def newsDetail(request, slug):
    newsDetail = News.objects.get(news_slug=slug)
    data = {
        'newsDetail': newsDetail,
    }
    return render(request, 'newsdetail.html', data)

def aboutUs(request):
    if request.method == 'GET':
        output = request.GET.get('output')
        return render(request, "aboutUs.html", {'output': output})

def course(request):
    return render(request, "course.html")
    # return HttpResponse('course page')

def coursedetail(request, courseid):
    return HttpResponse(courseid)

def userForm(request):
    ans = 0
    fn = usersform()
    data = {'form':fn}
    try:
        if request.method == 'POST':
            num1 = int(request.POST.get('num1'))
            num2 = int(request.POST.get('num2'))
            ans = num1 + num2
        data = {
                'num1':num1,
                'num2':num2,
                'ans':ans,
                'form':fn,
            }
        url = '/about-us/?output={}'.format(ans)
        return HttpResponseRedirect(url)
    except:
        pass
    return render(request, 'userform.html', data)


def calculator(request):
    c = ''
    try:
        if request.method == 'POST':
            n1 = eval(request.POST.get('num1'))
            n2 = eval(request.POST.get('num2'))
            opr = request.POST.get('opr')

            if opr == '+':
                c = n1 + n2
            elif opr == '-':
                c = n1 - n2
            elif opr == '*':
                c = n1 * n2
            elif opr == '/':
                c = n1 / n2
    except:
        c = 'Invalid opr...'
    return render(request, 'calculator.html', {'c':c})


def evenodd(request):
    res = ''
    try:
        if request.method == 'POST':
            if request.POST.get('num1') == '':
                return render(request, 'evenodd.html', {'error':True})
            n1 = eval(request.POST.get("num1"))
            if n1 % 2 == 0:
                res = 'Even number'
            else:
                res = 'Odd number'
    except:
        res = 'Invalid Input'
    return render(request, 'evenodd.html', {'res': res})


def marksheet(request):
    total = 0
    div = ''
    if request.method == 'POST':
        s1 = eval(request.POST.get('sub1'))
        s2 = eval(request.POST.get('sub2'))
        s3 = eval(request.POST.get('sub3'))
        s4 = eval(request.POST.get('sub4'))
        s5 = eval(request.POST.get('sub5'))

        total = s1 + s2 + s3 + s4 + s5
        per = (total * 100) / 500

        if per >= 80:
            div = 'Distinction'
        elif per >= 70:
            div = 'First'
        elif per >= 60:
            div = 'Second'
        elif per >= 50:
            div = 'Third'
        else:
            div = 'Fail'
        
        data = {
            'total':total,
            'per':per,
            'div':div,
        }
    return render(request, 'marksheet.html', data)


def service(request):
    servicedata = Service.objects.all()
    if request.method == 'GET':
        st = request.GET.get('servicename')
        if st != None:
            servicedata = Service.objects.filter(service_title__icontains=st)
    
    ServiceData = Service.objects.all()
    paginator = Paginator(ServiceData, 2)
    page_number = request.GET.get('page')
    servicedatafinal = paginator.get_page(page_number)
    totalpage = servicedatafinal.paginator.num_pages
    
    data = {
        'servicedata':servicedatafinal,
        'lastpage': totalpage,
        'totalpagelist': [n+1 for n in range(totalpage)],
        # 'servicedatafinal': servicedatafinal, 
        
    }
    return render(request, 'service.html', data)


def enquire(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        address = request.POST.get('address')
        mobile = request.POST.get('mobile')
        # query1 = request.POST.get('query')
        edata = Enquire(name=name, email=email, mobile=mobile, address=address)
        edata.save()

    return render(request, 'enquire.html')
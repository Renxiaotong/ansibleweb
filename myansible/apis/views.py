from django.shortcuts import render ,HttpResponse,redirect
from apis.models import Groups,Hosts,Module,Argument
import subprocess
import subprocess
# Create your views here.

def index(request):
    return render(request,"index.html");
def info(request):
    #subprocess.run("ansible all -m setup --tree /tmp/myyservers",shell=True);
    #subprocess.run("ansible-cmdb /tmp/myysetvers/ > ..//tempales/servers/servers.html",shell=True);
    return render(request,"servers.html");
def addhost(request):
    if request.method == "POST":
        group = request.POST.get('group').strip();
        ip = request.POST.get('ip').strip();
        hostname = request.POST.get('hostname').strip();
        if group:
            g = Groups.objects.get_or_create(GroupName=group)[0];
            if ip and hostname:
                g.hosts_set.get_or_create(HostName=hostname,HostIp=ip);
    groups = Groups.objects.all();
    #hosts = Hosts.objects.get_or_creat
    return render(request,"addhost.html",{"groups":groups});
def deletehost(request):
    if request.method == "POST":
        group = request.POST.get('group').strip();
        ip = request.POST.get('ip').strip();
        hostname = request.POST.get('hostname').strip();
        if group:
            g = Groups.objects.get(GroupName=group);
            if ip and hostname:
                host = g.hosts_set.get(HostIp=ip,HostName=hostname);
                if host:
                    host.delete();
                else:
                    return HttpResponse("no such note");
            if not ip and not hostname:
                return HttpResponse("you want to delete groups try SQLL");
        else:
            return HttpResponse("no such note");
    return HttpResponse("delete succsful");
def tasks(request):
    if request.method == "POST":
        module = request.POST.get('module').strip();
        argument = request.POST.get('argument').strip();
        if module:
            m = Module.objects.get_or_create(ModuleName=module);
            if argument:
                Module.objects.get(ModuleName=module).argument_set.get_or_create(ArgumentText=argument);
    modules = Module.objects.all();
    return render(request,"tasks.html",{"modules":modules});
def deletetask(request):
    if request.method == "POST":
        module = request.POST.get('module').strip();
        argument = request.POST.get('argument').strip();
        if module:
            m = Module.objects.get(ModuleName=module);
            if argument:
                m.argument_set.get(ArgumentText=argument).delete();
            else:
                return HttpResponse("you want to delete module please try SQL");
    return HttpResponse("delete succssful");
def run(request):
    if request.method == "POST":
        group = request.POST.get('group').strip();
        host = request.POST.get('host').strip();
        module = request.POST.get('module').strip();
        argument = request.POST.get('argument').strip();
        target = None;
        if host:
            target = host;
        else:
            target = group;
        print("ansible %s -m %s -a '%s'" % (target,module,argument));
        subprocess.run("ansible %s -m %s -a '%s'" % (target,module,argument),shell=True);
    hosts = Hosts.objects.all();
    groups = Groups.objects.all();
    modules = Module.objects.all();
    retval = {"hosts":hosts,"groups":groups,"modules":modules,};
    return render(request,"run.html",retval);
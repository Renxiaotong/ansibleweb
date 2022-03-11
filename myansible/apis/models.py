from django.db import models
# Create your models here.
class Groups(models.Model):
    GroupName = models.CharField(max_length=50);
    def __str__(self):
        return "%s" % self.GroupName
class Hosts(models.Model):
    HostName = models.CharField(max_length=200);
    HostIp = models.CharField(max_length=15);
    Group = models.ForeignKey(Groups,on_delete=models.CASCADE);
    def __str__(self):
        return "%s : %s" % (self.Group,self.HostName);
class Module(models.Model):
    ModuleName = models.CharField(max_length=100);
    def __str__(self):
        return "%s" % (self.ModuleName);
class Argument(models.Model):
    ArgumentText = models.CharField(max_length=100);
    Module = models.ForeignKey(Module,on_delete=models.CASCADE);
    def __str__(self):
        return "%s : %s" % (self.Module,self.ArgumentText);
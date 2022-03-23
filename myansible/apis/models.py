from django.db import models
# 建立映射到数据库的模板，方便views调用
# 主机组模板
class Groups(models.Model):
    GroupName = models.CharField(max_length=50);
    def __str__(self):
        return "%s" % self.GroupName
# 主机信息模板
class Hosts(models.Model):
    HostName = models.CharField(max_length=200);
    HostIp = models.CharField(max_length=15);
    Group = models.ForeignKey(Groups,on_delete=models.CASCADE);
    def __str__(self):
        return "%s : %s" % (self.Group,self.HostName);
# 任务模快模板
class Module(models.Model):
    ModuleName = models.CharField(max_length=100);
    def __str__(self):
        return "%s" % (self.ModuleName);
# 任务参数模板
class Argument(models.Model):
    ArgumentText = models.CharField(max_length=100);
    Module = models.ForeignKey(Module,on_delete=models.CASCADE);
    def __str__(self):
        return "%s : %s" % (self.Module,self.ArgumentText);

from django.db import models

class Application(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    region = models.CharField(max_length=100)
    framework = models.CharField(max_length=100)
    plan_type = models.CharField(max_length=50)
    database_type = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

class Environment(models.Model):
    application = models.ForeignKey(Application, related_name='environments', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    branch_name = models.CharField(max_length=100)

class Instance(models.Model):
    environment = models.ForeignKey(Environment, related_name='instances', on_delete=models.CASCADE)
    config = models.CharField(max_length=100)
    status = models.CharField(max_length=100)

class EnvironmentVariable(models.Model):
    environment = models.ForeignKey(Environment, related_name='variables', on_delete=models.CASCADE)
    key = models.CharField(max_length=100)
    value = models.CharField(max_length=500)

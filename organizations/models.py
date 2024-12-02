from django.db import models
from django_tenants.models import TenantMixin, DomainMixin


class Organization(TenantMixin):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField()
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)
    email = models.EmailField(unique=True)
    website = models.URLField(blank=True, null=True)
    industry = models.CharField(max_length=100, blank=True)
    status = models.CharField(max_length=50, choices=(('active', 'Active'), ('inactive', 'Inactive')))
    on_trial = models.BooleanField(default=True)
    subscription_paid = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    auto_create_schema = True

    def __str__(self):
        return self.name


class Domain(DomainMixin):
    pass

class Branch(models.Model):
    name = models.CharField(max_length=255)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE, related_name="branches")
    address = models.CharField(max_length=255, blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    status = models.CharField(max_length=50, choices=[('active', 'Active'), ('inactive', 'Inactive')], default='active')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Department(models.Model):
    name = models.CharField(max_length=255, unique=True)
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE, related_name="departments")
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Group(models.Model):
    name = models.CharField(max_length=255)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE, related_name="groups")
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name="groups", null=True, blank=True)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
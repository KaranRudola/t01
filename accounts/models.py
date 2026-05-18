from django.db import models

# Matches SYS_USERS table
class SysUser(models.Model):
    user_id = models.AutoField(primary_key=True)  # NUMBER PK, identity
    employee_number = models.CharField(max_length=20, unique=True)  # VARCHAR2(20), unique, not null
    password_hash = models.CharField(max_length=255)  # VARCHAR2(255), not null
    full_name = models.CharField(max_length=100)  # VARCHAR2(100)
    email = models.CharField(max_length=150)  # VARCHAR2(150)
    department = models.CharField(max_length=100, null=True, blank=True)  # VARCHAR2(100)
    role = models.CharField(
        max_length=50,
        default='USER',
        choices=[('ADMIN', 'Admin'), ('MANAGER', 'Manager'), ('USER', 'User')]
    )  # VARCHAR2(50), check constraint
    is_active = models.BooleanField(default=True)  # NUMBER(1), check constraint
    created_at = models.DateTimeField(auto_now_add=True)  # TIMESTAMP, default current
    last_login = models.DateTimeField(null=True, blank=True)  # TIMESTAMP

    def __str__(self):
        return f"{self.full_name} ({self.employee_number})"


# Matches SYS_MODULE table
class SysModule(models.Model):
    module_id = models.AutoField(primary_key=True)  # NUMBER PK
    name = models.CharField(max_length=100)  # VARCHAR2(100)
    parent_module_id = models.ForeignKey(
        'self',
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name='submodules'
    )  # parent-child hierarchy

    def __str__(self):
        return self.name


# Matches SYS_COMPONENT table
class SysComponent(models.Model):
    component_id = models.AutoField(primary_key=True)  # NUMBER PK
    name = models.CharField(max_length=100)  # VARCHAR2(100)
    module = models.ForeignKey(SysModule, on_delete=models.CASCADE, related_name='components')

    def __str__(self):
        return f"{self.name} (Module: {self.module.name})"
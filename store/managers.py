from django.contrib.auth.base_user import BaseUserManager

class CustomManager(BaseUserManager):
    def create_user(self,email,password,**extra_fields):
        if not email:
            raise ValueError('email is required')
        email=self.normalize_email(email)
        user = self.model(email=email,**extra_fields)
        user.set_password(password)
        user.save()

    def create_superuser(self,email,password,**extra_fields):
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_staff', True)
        return self.create_user(email,password,**extra_fields)
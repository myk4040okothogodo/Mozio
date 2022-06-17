from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.utils.translation import ugettext_lazy as _

class UserManager(BaseUserManager):
    def create_user(self, email ,password=None, **kwargs):
        """Create and return a `User` with an email, phone_number, and password."""
        if email is None:
            raise TypeError("User must have an email.")
        
        user = self.model(email=self.normalize_email(email))
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email,password):
        """ Create and return a `User` with superuser(admin) permissions."""
        if password is None:
            raise TypeError('Superusers must have a password')
        if email is None:
            raise TypeError('Superusers must have an email')

        user = self.create_user(email, password)
        user.is_superuser = True
        user.is_staff = True
        user.save(using= self._db)

        return user




class ImageUpload(models.Model):
    image = models.ImageField(upload_to="images")

    def __str__(self):
        return str(self.image)




class Provider(AbstractBaseUser, PermissionsMixin):

    KISWAHILI  = 1
    ENGLISH    = 2
    FRENCH     = 3
    GERMAN     = 4
    RUSSIAN    = 5
    SPANISH    = 6
    ARABIC     = 7
    SWEDISH    = 8
    INDIAN     = 9
    LANGUAGE = (
        (KISWAHILI, _('kiswahili')),
        (ENGLISH,  _('english')),
        (FRENCH,   _('french')),
        (GERMAN,   _('german')),
        (RUSSIAN,  _('russian')),
        (SPANISH,  _('spanish')),
        (ARABIC,  _('arabic')),
        (SWEDISH,  _('swedish')),
        (INDIAN,   _('indian')),
            )
    
    SHILLING = 1
    DOLLAR   = 2
    YUAN     = 3
    PESO     = 4
    POUND    = 5
    EURO     = 6
    YEN       = 7
    DINAR    = 8
    FRANC    = 9
    LIRA     = 10
    RIYAL    = 11
    RUPEE    = 12
    KRONE    = 13
    CURRENCY = (
        (SHILLING, _('shilling')),
        (DOLLAR, _('dollar')),
        (YUAN, _('yuan')),
        (PESO, _('peso')),
        (POUND, _('pound')),
        (EURO, _('euro')),
        (YEN,  _('yen')),
        (DINAR, _('dinar')),
        (FRANC, _('franc')),
        (LIRA, _('lira')),
        (RIYAL, _('riyal')),
        (RUPEE, _('rupee')),
        (KRONE, _('krone')),
            )

    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=100, default="yourfirstname")
    last_name = models.CharField(max_length=100, default="yourlastname")
    language = models.PositiveSmallIntegerField(choices=LANGUAGE, default=ENGLISH)
    currency = models.PositiveSmallIntegerField(choices=CURRENCY, default=DOLLAR)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    USERNAME_FIELD = "email"
    objects = UserManager()

    def __str__(self):
        return self.email

    def save(self, *args, **kwargs):
        super().full_clean()
        super().save(*args, **kwargs)


class ProviderProfile(models.Model):

   
    provider  =  models.OneToOneField(Provider, related_name="user_profile", on_delete=models.CASCADE)
    profile_picture = models.ForeignKey(ImageUpload, related_name="user_images", on_delete=models.SET_NULL, null=True)
    dob = models.DateField()
    country_code = models.CharField(default="+234", max_length=5)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.email



class ProviderAddress(models.Model):

    provider_profile = models.ForeignKey(ProviderProfile, related_name="user_addresses", on_delete=models.CASCADE)
    street = models.TextField()
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=100, default="Nigeria")
    is_default = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user_profile.user.email
        




from django.db import models

class Category(models.Model):
    category = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.category
    

class Gmail(models.Model):
    email = models.EmailField()

    def __str__(self):
        return self.email


# Phone Model
class Phone(models.Model):
    phone_number = models.CharField(max_length=15)

    def __str__(self):
        return self.phone_number


# Image Model
class Image(models.Model):
    image = models.ImageField(upload_to='images/', blank=True, null=True)

    def __str__(self):
        return f"Image {self.id}"
# models.py

class Counselling(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    given_name = models.CharField(max_length=100)
    gender = models.CharField(max_length=10, choices=[('Female', 'Female'), ('Male', 'Male'), ('Other', 'Other')])
    born_date = models.DateField()
    born_place = models.CharField(max_length=255)
    born_country = models.CharField(max_length=255)

    # These fields will store multiple Gmail addresses, phone numbers, and images.
    gmail_addresses = models.ManyToManyField('Gmail', blank=True)
    phone_numbers = models.ManyToManyField('Phone', blank=True)
    images = models.ManyToManyField('Image', blank=True)

    document = models.FileField(upload_to='documents/', null=True, blank=True)
    position = models.CharField(max_length=255)
    organization = models.CharField(max_length=255)
    division = models.CharField(max_length=255)

    # Address fields
    street = models.CharField(max_length=255)
    number = models.CharField(max_length=50)
    zip_code = models.CharField(max_length=10)
    place = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=100)

    # Contact details
    phone_number = models.CharField(max_length=15)
    mail_address = models.EmailField(max_length=255)

    def __str__(self):
        return f"{self.first_name} {self.surname}"
    

class Notes(models.Model):
    person = models.ForeignKey(Counselling, on_delete=models.CASCADE)
    note = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.person.first_name





class FamilyMember(models.Model):
    counselling = models.ForeignKey(Counselling, on_delete=models.CASCADE, related_name='family_members')
    first_name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    given_name = models.CharField(max_length=100)
    gender = models.CharField(max_length=10, choices=[('Female', 'Female'), ('Male', 'Male'), ('Other', 'Other')])
    born_date = models.DateField()
    born_place = models.CharField(max_length=255)
    born_country = models.CharField(max_length=255)

    # Contact details
    phone_number = models.CharField(max_length=15)
    mail_address = models.EmailField(max_length=255)



    def __str__(self):
        return f"{self.first_name} {self.surname}"

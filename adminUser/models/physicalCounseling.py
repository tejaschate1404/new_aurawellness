from django.db import models


# Category Model
class CategoryPhysical(models.Model):
    category = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.category
    

# Gmail Model
class GmailPhysical(models.Model):
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.email


# Phone Model
class PhonePhysical(models.Model):
    phone_number = models.CharField(max_length=15, unique=True)

    def __str__(self):
        return self.phone_number


# Image Model
class ImagePhysical(models.Model):
    image = models.ImageField(upload_to='images/', blank=True, null=True)

    def __str__(self):
        return f"Image {self.id}"


# Main Counseling Model
class CounsellingPhysical(models.Model):
    category = models.ForeignKey(CategoryPhysical, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    given_name = models.CharField(max_length=100)
    gender = models.CharField(max_length=10, choices=[('Female', 'Female'), ('Male', 'Male'), ('Other', 'Other')])
    born_date = models.DateField()
    born_place = models.CharField(max_length=255)
    born_country = models.CharField(max_length=255)

    # Many-to-Many Relations
    gmail_addresses = models.ManyToManyField(GmailPhysical, blank=True)
    phone_numbers = models.ManyToManyField(PhonePhysical, blank=True)
    images = models.ManyToManyField(ImagePhysical, blank=True)

    document = models.FileField(upload_to='documents/', null=True, blank=True)
    position = models.CharField(max_length=255)
    organization = models.CharField(max_length=255)
    division = models.CharField(max_length=255)

    # Address Fields
    street = models.CharField(max_length=255)
    house_number = models.CharField(max_length=50)
    zip_code = models.CharField(max_length=10)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.first_name} {self.surname}"


# Notes Model
class NotesPhysical(models.Model):
    person = models.ForeignKey(CounsellingPhysical, on_delete=models.CASCADE, related_name="notes")
    note = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Note for {self.person.first_name}"

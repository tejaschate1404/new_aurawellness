from django.shortcuts import render, redirect , get_object_or_404
from django.contrib import messages
from adminUser.models import Category  # Ensure that you import your Category model
from adminUser.models import Counselling, Category, Gmail, Phone, Image
from adminUser.models import Notes
from django.utils import timezone


def indexAdmin(request):
    pass

def addCounseling(request):
    if request.method == "POST":
        category_id = request.POST.get("category")

        # Ensure category exists
        category = get_object_or_404(Category, id=category_id)

        # Get form data
        first_name = request.POST.get("firstName")
        surname = request.POST.get("lastName")
        given_name = request.POST.get("givenName")
        gender = request.POST.get("gender")
        born_date = request.POST.get("dob")
        born_place = request.POST.get("place")
        born_country = request.POST.get("country")
        position = request.POST.get("description")
        organization = request.POST.get("companyName")
        division = request.POST.get("division")
        street = request.POST.get("streetNumber")
        zip_code = request.POST.get("zip")
        state = request.POST.get("state")
        country = request.POST.get("addressCountry")
        phone_number = request.POST.get("phone")
        mail_address = request.POST.get("title")

        # Create Counseling instance
        counseling = Counselling.objects.create(
            category=category,
            first_name=first_name,
            surname=surname,
            given_name=given_name,
            gender=gender,
            born_date=born_date,
            born_place=born_place,
            born_country=born_country,
            position=position,
            organization=organization,
            division=division,
            street=street,
            zip_code=zip_code,
            state=state,
            country=country,
            phone_number=phone_number,
            mail_address=mail_address,
        )

        # Handle ManyToMany fields
        if mail_address:
            gmail, _ = Gmail.objects.get_or_create(email=mail_address)
            counseling.gmail_addresses.add(gmail)

        if phone_number:
            phone_obj, _ = Phone.objects.get_or_create(phone_number=phone_number)
            counseling.phone_numbers.add(phone_obj)

        if "image" in request.FILES:
            image_obj = Image.objects.create(image=request.FILES["image"])
            counseling.images.add(image_obj)

        return redirect('viewCounseling')  # Change to your actual success URL

    # Fetch categories for dropdown
    categories = Category.objects.all()

    return render(request, 'admin/counseling/addCounseling.html' ,{'categories': categories})




    
def viewCounseling(request):
    counseling_records = Counselling.objects.all()  # Fetch all records
    return render(request, 'admin/counseling/view-counseling.html', {'counseling_records': counseling_records})




def view_counseling_details(request, record_id):
    # Fetch the counseling record
    record = get_object_or_404(Counselling, id=record_id)
    

    # Check if the request method is POST (form submission)
    if request.method == "POST":
        note = request.POST.get("note")  # Get the note content
        print(note)
        date = timezone.now()  # Get the date (ensure it’s in a correct format)

        if note and date:  # If both fields are filled
            # Create the note linked to the counseling record
            Notes.objects.create(person=record, note=note, created_at=date)
            messages.success(request, "Note added successfully!")
        else:
            messages.error(request, "Please fill in both the note and the date.")


    show_notes = Notes.objects.filter(person=record)  

    context = {
        'current_date': timezone.now(),
        'record': record,
        'show_note': show_notes
               }
    return render(request, 'admin/counseling/view_counseling_details.html',context)





def delete_counseling(request, record_id):
    record = get_object_or_404(Counselling, id=record_id)
    record.delete()
    return redirect('viewCounseling')  # Redirect back to the counseling list





# View for adding category
def addCategory(request):
    if request.method == 'POST':
        # Retrieve category and description from POST data
        category_name = request.POST.get('category')  # Match the field name 'category'
        description = request.POST.get('description')

        # Ensure both fields are filled
        if category_name and description:
            # Create a new Category instance and save it
            new_category = Category(category=category_name, description=description)
            new_category.save()

            # Add a success message and redirect
            messages.success(request, 'Category has been added successfully.')
            return redirect('addCategory')  # Make sure 'addCategory' is a valid URL name

        else:
            messages.error(request, 'Please fill in all fields.')

    return render(request, 'admin/counseling/add-category.html')




from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.utils import timezone
from adminUser.models import DistanceHealing, CategoryDistance, GmailDistance, PhoneDistance, ImageDistance, NotesDistance

# def addDistanceHealing(request):
#     if request.method == "POST":
#         category_id = request.POST.get("category")

#         # Ensure category exists
#         category = get_object_or_404(CategoryDistance, id=category_id)

#         # Get form data
#         first_name = request.POST.get("firstName")
#         surname = request.POST.get("lastName")
#         given_name = request.POST.get("givenName")
#         gender = request.POST.get("gender")
#         born_date = request.POST.get("dob")
#         born_place = request.POST.get("place")
#         born_country = request.POST.get("country")
#         position = request.POST.get("description")
#         organization = request.POST.get("companyName")
#         division = request.POST.get("division")
#         street = request.POST.get("streetNumber")
#         zip_code = request.POST.get("zip")
#         state = request.POST.get("state")
#         country = request.POST.get("addressCountry")
#         phone_number = request.POST.get("phone")
#         mail_address = request.POST.get("title")

#         # Create Distance Healing instance
#         distance_healing = DistanceHealing.objects.create(
#             category=category,
#             first_name=first_name,
#             surname=surname,
#             given_name=given_name,
#             gender=gender,
#             born_date=born_date,
#             born_place=born_place,
#             born_country=born_country,
#             position=position,
#             organization=organization,
#             division=division,
#             street=street,
#             zip_code=zip_code,
#             state=state,
#             country=country,
#         )

#         # Handle ManyToMany fields
#         if mail_address:
#             gmail, _ = GmailDistance.objects.get_or_create(email=mail_address)
#             distance_healing.gmail_addresses.add(gmail)

#         if phone_number:
#             phone_obj, _ = PhoneDistance.objects.get_or_create(phone_number=phone_number)
#             distance_healing.phone_numbers.add(phone_obj)

#         if "image" in request.FILES:
#             image_obj = ImageDistance.objects.create(image=request.FILES["image"])
#             distance_healing.images.add(image_obj)

#         return redirect('viewDistanceHealing')  # Change to your actual success URL

#     # Fetch categories for dropdown
#     categories = CategoryDistance.objects.all()
#     return render(request, 'admin/distance_healing/addCounseling.html', {'categories': categories})





def addDistanceHealing(request):
    if request.method == "POST":
        category_id = request.POST.get("category")
        category = get_object_or_404(CategoryDistance, id=category_id)

        # Get form data
        first_name = request.POST.get("first_name")
        surname = request.POST.get("surname")
        given_name = request.POST.get("given_name")
        gender = request.POST.get("gender")
        born_date = request.POST.get("born_date")
        born_place = request.POST.get("born_place")
        born_country = request.POST.get("born_country")
        position = request.POST.get("position")
        organization = request.POST.get("organization")
        division = request.POST.get("division")
        street = request.POST.get("street")
        house_number = request.POST.get("house_number")
        zip_code = request.POST.get("zip_code")
        state = request.POST.get("state")
        country = request.POST.get("country")
        phone_number = request.POST.get("phone_number")
        email_address = request.POST.get("email_address")

        # Create DistanceHealing instance
        distance_healing = DistanceHealing.objects.create(
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
            house_number=house_number,
            zip_code=zip_code,
            state=state,
            country=country,
        )

        # Handle ManyToMany fields
        if email_address:
            gmail, _ = GmailDistance.objects.get_or_create(email=email_address)
            distance_healing.gmail_addresses.add(gmail)

        if phone_number:
            phone_obj, _ = PhoneDistance.objects.get_or_create(phone_number=phone_number)
            distance_healing.phone_numbers.add(phone_obj)

        if "image" in request.FILES:
            image_obj = ImageDistance.objects.create(image=request.FILES["image"])
            distance_healing.images.add(image_obj)

        return redirect('viewDistanceHealing')  # Update with the correct success URL

    categories = CategoryDistance.objects.all()
    return render(request, 'admin/distance_healing/addCounseling.html', {'categories': categories})




















































def viewDistanceHealing(request):
    distance_healing_records = DistanceHealing.objects.all()  # Fetch all records
    return render(request, 'admin/distance_healing/view-counseling.html', {'distance_healing_records': distance_healing_records})


def view_distance_healing_details(request, record_id):
    # Fetch the distance healing record
    record = get_object_or_404(DistanceHealing, id=record_id)

    # Check if the request method is POST (form submission)
    if request.method == "POST":
        note = request.POST.get("note")  # Get the note content
        date = timezone.now()  # Get the current date

        if note:  # If note is not empty
            NotesDistance.objects.create(person=record, note=note, created_at=date)
            messages.success(request, "Note added successfully!")
        else:
            messages.error(request, "Please enter a note.")

    show_notes = NotesDistance.objects.filter(person=record)

    context = {
        'current_date': timezone.now(),
        'record': record,
        'show_note': show_notes
    }
    return render(request, 'admin/distance_healing/view_distance_healing_details.html', context)


def delete_distance_healing(request, record_id):
    record = get_object_or_404(DistanceHealing, id=record_id)
    record.delete()
    return redirect('viewDistanceHealing')  # Redirect back to the Distance Healing list


# View for adding category
def addCategoryDistance(request):
    if request.method == 'POST':
        category_name = request.POST.get('category')
        description = request.POST.get('description')

        if category_name and description:
            new_category = CategoryDistance(category=category_name, description=description)
            new_category.save()

            messages.success(request, 'Category has been added successfully.')
            return redirect('addCategoryDistance')  # Ensure 'addCategoryDistance' is in your URL mappings

        else:
            messages.error(request, 'Please fill in all fields.')

    return render(request, 'admin/distance_healing/add-category.html')

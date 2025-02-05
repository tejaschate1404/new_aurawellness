from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.utils import timezone
from adminUser.models import (
    CounsellingPhysical,
    CategoryPhysical,
    GmailPhysical,
    PhonePhysical,
    ImagePhysical,
    NotesPhysical
)


# View for adding Physical Healing record
def addPhysicalHealing(request):
    if request.method == "POST":
        category_id = request.POST.get("category")
        category = get_object_or_404(CategoryPhysical, id=category_id)

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

        # Create Physical Healing instance
        physical_healing = CounsellingPhysical.objects.create(
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
            gmail, _ = GmailPhysical.objects.get_or_create(email=email_address)
            physical_healing.gmail_addresses.add(gmail)

        if phone_number:
            phone_obj, _ = PhonePhysical.objects.get_or_create(phone_number=phone_number)
            physical_healing.phone_numbers.add(phone_obj)

        if "image" in request.FILES:
            image_obj = ImagePhysical.objects.create(image=request.FILES["image"])
            physical_healing.images.add(image_obj)

        messages.success(request, "Physical Healing record added successfully!")
        return redirect('viewPhysicalHealing')

    categories = CategoryPhysical.objects.all()
    return render(request, 'admin/physical_healing/add_counseling_physical.html', {'categories': categories})


# View all Physical Healing records
def viewPhysicalHealing(request):
    physical_healing_records = CounsellingPhysical.objects.all()
    return render(request, 'admin/physical_healing/view-counseling.html', {'physical_healing_records': physical_healing_records})


# View details of a specific Physical Healing record
def viewPhysicalHealingDetails(request, record_id):
    record = get_object_or_404(CounsellingPhysical, id=record_id)

    if request.method == "POST":
        note = request.POST.get("note")
        if note:
            NotesPhysical.objects.create(person=record, note=note, created_at=timezone.now())
            messages.success(request, "Note added successfully!")
        else:
            messages.error(request, "Please enter a note.")

    show_notes = NotesPhysical.objects.filter(person=record)

    context = {
        'current_date': timezone.now(),
        'record': record,
        'show_notes': show_notes
    }
    return render(request, 'admin/physical_healing/view_physical_healing_details.html', context)


# Delete a Physical Healing record
def deletePhysicalHealing(request, record_id):
    record = get_object_or_404(CounsellingPhysical, id=record_id)
    record.delete()
    messages.success(request, "Record deleted successfully!")
    return redirect('viewPhysicalHealing')


# Add a new category for Physical Healing
def addCategoryPhysical(request):
    if request.method == 'POST':
        category_name = request.POST.get('category')
        description = request.POST.get('description')

        if category_name and description:
            new_category = CategoryPhysical(category=category_name, description=description)
            new_category.save()
            messages.success(request, 'Category added successfully!')
            return redirect('addCategoryPhysical')
        else:
            messages.error(request, 'Please fill in all fields.')

    return render(request, 'admin/physical_healing/add_category_physical.html')

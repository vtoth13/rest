from .forms import BookingForm
from django.http import JsonResponse
from django.shortcuts import render, redirect
from .models import Table, MenuItem, Booking
from django.contrib.auth.decorators import login_required
 
def index(request):
    return render(request, 'index.html')

def table_list(request):
    tables = Table.objects.filter(available=True)
    return render(request, 'tables.html', {'tables': tables})

def menu_list(request):
    menu_items = MenuItem.objects.all()
    return render(request, 'menu.html', {'menu_items': menu_items})

@login_required
def booking_create(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user
            booking.save()
            Table.objects.filter(id=booking.table.id).update(available=False)
            return redirect('booking_list')
    else:
        form = BookingForm()
    return render(request, 'booking_form.html', {'form': form})

@login_required
def booking_list(request):
    bookings = Booking.objects.filter(user=request.user)
    return render(request, 'bookings.html', {'bookings': bookings})

@login_required
def cancel_booking(request, booking_id):
    booking = Booking.objects.get(id=booking_id)
    if request.method == 'POST':
        Table.objects.filter(id=booking.table.id).update(available=True)
        booking.delete()
        return redirect('booking_list')
    return redirect('booking_list')

def check_table_availability(request, table_id, number_of_people):
    table = Table.objects.get(id=table_id)
    if table.seats >= int(number_of_people):
        return JsonResponse({'is_available': True})
    else:
        return JsonResponse({'is_available': False})
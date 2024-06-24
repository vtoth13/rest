from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Table, MenuItem, Booking
from .forms import BookingForm
from django.contrib import messages
 
def index(request):
    return render(request, 'index.html')

@login_required
def table_list(request):
    tables = Table.objects.filter(available=True)
    return render(request, 'tables.html', {'tables': tables})

@login_required
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

def cancel_booking(request, booking_id):
    booking = Booking.objects.get(id=booking_id)
    if request.method == 'POST':
        Table.objects.filter(id=booking.table.id).update(available=True)
        booking.delete()
        messages.success(request, 'Booking cancelled successfully!')
        return redirect('booking_list')
    return redirect('booking_list')
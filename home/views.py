from django.shortcuts import render, redirect


from accounts.models import BookingManager
from .models import Sport, Booking
import datetime
from .forms import tabletennis, basketball, squash

def past_bookings(request):
    username = None
    if request.user.is_authenticated:
        username = request.user.username

    past_booking_output = []
    temp = BookingManager.objects.get(userid=username)
    bookings = temp.upcoming_bookings.split('|')[:-1]

    for booking in bookings:

        booking_dict = {}
        date = datetime.datetime.strptime(booking[0:10], "%Y-%m-%d")
        now = datetime.datetime.now()

        # create a dictionary to be used in HTML file
        booking_dict['name'] = booking

        booking_objects = Booking.objects.get(dt=date.date())
        bi = booking_objects.lt.split('|')
        booking_index = bi.index(booking[11:])
        sts = booking_objects.st.split('|')[:-1][booking_index].split(',')[:-1]
        booking_dict['users'] = ["users booked:"] + sts

        if date < now:
            past_booking_output.append(booking_dict)

    return past_booking_output

def upcoming_booking(request):
    username = None
    if request.user.is_authenticated:
        username = request.user.username

    upcoming_booking_output = []
    temp = BookingManager.objects.get(userid=username)
    bookings = temp.upcoming_bookings.split('|')[:-1]

    for booking in bookings:

        booking_dict = {}
        booking_date = booking[0:10]
        # print(booking_date)
        date = datetime.datetime.strptime(booking_date, "%Y-%m-%d")
        now = datetime.datetime.now()

        if date > now:

            #create a dictionary to be used in HTML file
            booking_dict['name'] = booking

            booking_objects = Booking.objects.get(dt=date.date())
            bi = booking_objects.lt.split('|')
            booking_index = bi.index(booking[11:])
            sts = booking_objects.st.split('|')[:-1][booking_index].split(',')[:-1]
            booking_dict['users'] = ["users booked:"] + sts

            upcoming_booking_output.append(booking_dict)
    return upcoming_booking_output

def index(request):
    print(10)
    username = None
    if request.user.is_authenticated:
        username = request.user.username

    # admin = BookingManager(userid='admin', past_bookings="", upcoming_bookings="")
    # admin.save()
    #
    # output = "University Sports Center, Court 4 0700 : 0800|University Sports Center, Court 4 0800 : 0900|University Sports Center, Court 4 0900 : 1000|University Sports Center, Court 4 1000 : 1100|University Sports Center, Court 4 1100 : 1200|University Sports Center, Court 4 1200 : 1300|University Sports Center, Court 4 1300 : 1400|University Sports Center, Court 4 1400 : 1500|University Sports Center, Court 4 1500 : 1600|University Sports Center, Court 4 1600 : 1700|University Sports Center, Court 4 1700 : 1800|University Sports Center, Court 3 0800 : 0900|University Sports Center, Court 3 0900 : 1000|University Sports Center, Court 3 1000 : 1100|University Sports Center, Court 3 1100 : 1200|University Sports Center, Court 3 1200 : 1300|University Sports Center, Court 3 1300 : 1400|University Sports Center, Court 3 1400 : 1500|University Sports Center, Court 3 1500 : 1600|University Sports Center, Court 3 1600 : 1700|University Sports Center, Court 3 1700 : 1800|University Sports Center, Court 3 1800 : 1900|University Sports Center, Court 2 0900 : 1000|University Sports Center, Court 2 1000 : 1100|University Sports Center, Court 2 1100 : 1200|University Sports Center, Court 2 1200 : 1300|University Sports Center, Court 2 1300 : 1400|University Sports Center, Court 2 1400 : 1500|University Sports Center, Court 2 1500 : 1600|University Sports Center, Court 2 1600 : 1700|University Sports Center, Court 2 1700 : 1800|University Sports Center, Court 2 1800 : 1900|University Sports Center, Court 2 1900 : 2000|University Sports Center, Court 1 1000 : 1100|University Sports Center, Court 1 1100 : 1200|University Sports Center, Court 1 1200 : 1300|University Sports Center, Court 1 1300 : 1400|University Sports Center, Court 1 1400 : 1500|University Sports Center, Court 1 1500 : 1600|University Sports Center, Court 1 1600 : 1700|University Sports Center, Court 1 1700 : 1800|University Sports Center, Court 1 1800 : 1900|University Sports Center, Court 1 1900 : 2000|University Sports Center, Court 1 2000 : 2100|Caged Court, Prince George's Park Residences 0700 : 0800|Caged Court, Prince George's Park Residences 0800 : 0900|Caged Court, Prince George's Park Residences 0900 : 1000|Caged Court, Prince George's Park Residences 1000 : 1100|Caged Court, Prince George's Park Residences 1100 : 1200|Caged Court, Prince George's Park Residences 1200 : 1300|Caged Court, Prince George's Park Residences 1300 : 1400|Caged Court, Prince George's Park Residences 1400 : 1500|Caged Court, Prince George's Park Residences 1500 : 1600|Caged Court, Prince George's Park Residences 1600 : 1700|Caged Court, Prince George's Park Residences 1700 : 1800|Court 1, Prince George's Park Residences 0800 : 0900|Court 1, Prince George's Park Residences 0900 : 1000|Court 1, Prince George's Park Residences 1000 : 1100|Court 1, Prince George's Park Residences 1100 : 1200|Court 1, Prince George's Park Residences 1200 : 1300|Court 1, Prince George's Park Residences 1300 : 1400|Court 1, Prince George's Park Residences 1400 : 1500|Court 1, Prince George's Park Residences 1500 : 1600|Court 1, Prince George's Park Residences 1600 : 1700|Court 1, Prince George's Park Residences 1700 : 1800|Court 1, Prince George's Park Residences 1800 : 1900|Court 2, Prince George's Park Residences 0900 : 1000|Court 2, Prince George's Park Residences 1000 : 1100|Court 2, Prince George's Park Residences 1100 : 1200|Court 2, Prince George's Park Residences 1200 : 1300|Court 2, Prince George's Park Residences 1300 : 1400|Court 2, Prince George's Park Residences 1400 : 1500|Court 2, Prince George's Park Residences 1500 : 1600|Court 2, Prince George's Park Residences 1600 : 1700|Court 2, Prince George's Park Residences 1700 : 1800|Court 2, Prince George's Park Residences 1800 : 1900|Court 2, Prince George's Park Residences 1900 : 2000|Main Court, University Sports Centre 1000 : 1100|Main Court, University Sports Centre 1100 : 1200|Main Court, University Sports Centre 1200 : 1300|Main Court, University Sports Centre 1300 : 1400|Main Court, University Sports Centre 1400 : 1500|Main Court, University Sports Centre 1500 : 1600|Main Court, University Sports Centre 1600 : 1700|Main Court, University Sports Centre 1700 : 1800|Main Court, University Sports Centre 1800 : 1900|Main Court, University Sports Centre 1900 : 2000|Main Court, University Sports Centre 2000 : 2100|Table Tennis : Prince George's Park Residences, PGPH 1200 : 1300|Table Tennis : Prince George's Park Residences, PGPH 1300 : 1400|Table Tennis : Prince George's Park Residences, PGPH 1400 : 1500|Table Tennis : Prince George's Park Residences, PGPH 1500 : 1600"
    # slots = ''
    # peer_reqd = ''
    #
    # for i in range(0, 93):
    #     slots += 'free|'
    #     peer_reqd += 'yes|'
    #
    # for i in range(0, 365):
    #     print("today's date", datetime.date.today)
    #     trial = Booking(dt=datetime.date.today() + datetime.timedelta(days=i), lt=output, st=slots[:-1],
    #                     peer=peer_reqd[:-1])
    #     trial.save()
    booking_output = upcoming_booking(request)
    return render(request, 'home/Navbar.html', {"username": username, "bookings": booking_output})

    # temp = Sport.objects.all()
    # sports = []
    #
    # for x in temp:
    #     sport = {}
    #     sport['name'] = x.sport
    #     l = x.location.split(';')
    #     t = x.Timing.split(';')
    #     sport['lt'] = []
    #     for i in range(len(l)):
    #         sport['lt'].append(l[i] + ' - ' + t[i])
    #     sports.append(sport)
    #
    # output = ''
    # slots = ''
    # for i in range(len(sports)):
    #
    #     for j in range(len(sports[i]['lt'])):
    #         start = int(sports[i]['lt'][j][-9:-7])
    #         stop = int(sports[i]['lt'][j][-4:-2])
    #         array = ''
    #         for k in range(start,stop):
    #
    #             if k < 9:
    #                 array += sports[i]['lt'][j][:-11] + '0' + str(k) + '00:0' + str(k+1) + '00|'
    #             elif k == 9:
    #                 array += sports[i]['lt'][j][:-11] + '0' + str(k) + '00:' + str(k + 1) + '00|'
    #             else:
    #                 array += sports[i]['lt'][j][:-11] + '' + str(k) + '00:' + str(k + 1) + '00|'
    #             slots += 'free|'
    #         file.write(array)
    #         output += array

def sports(request):
    temp = Sport.objects.all()
    sports = []

    for x in temp:
        sport = {}
        sport['name'] = x.sport
        l = x.location.split(';')
        t = x.Timing.split(';')
        sport['lt'] = []
        sport['url'] = '/forms/' + sport['name']
        for i in range(len(l)):
            sport['lt'].append(l[i] + ' - ' + t[i])
        sports.append(sport)

    return render(request, 'home/facilities.html', {'sports': sports})

def bookSlot(request, sport):
    username = None
    if request.user.is_authenticated:
        username = request.user.username

    temp = BookingManager.objects.get(userid=username)
    past_booking = past_bookings(request)

    if request.method == 'POST':

        if sport == 'Basketball':
            form = basketball(request.POST)
            if form.is_valid():
                form = form.cleaned_data
                current = Booking.objects.get(dt=form['date'])
                pr = form['peer_reqd']
                print(pr)
                peers = current.peer.split('|')
                lts = current.lt.split('|')
                slots = current.st.split('|')
                i = lts.index(form['lt'])

                if slots[i] == 'free':
                    slots[i] = ''

                if peers[i] == 'no':
                    return render(request, 'home/nobooking.html', {"past_bookings": past_booking})

                if username not in slots[i]:
                    slots[i] += username + ','
                    peers[i] = pr
                    print(form['date'])
                    temp.upcoming_bookings += str(form['date']) + ';' + form['lt'] + '|'
                    temp.save()

                current.st = '|'.join(slots)
                current.peer = '|'.join(peers)
                current.save()

        if sport == 'Table Tennis':
            form = tabletennis(request.POST)
            if form.is_valid():
                form = form.cleaned_data
                current = Booking.objects.get(dt=form['date'])
                pr = form['peer_reqd']
                print(pr)
                peers = current.peer.split('|')
                lts = current.lt.split('|')
                slots = current.st.split('|')
                i = lts.index(form['lt'])

                if slots[i] == 'free':
                    slots[i] = ''

                if peers[i] == 'no':
                    return render(request, 'home/nobooking.html', {"past_bookings": past_booking})

                if username not in slots[i]:
                    slots[i] += username + ','
                    peers[i] = pr
                    temp.upcoming_bookings += str(form['date']) + ';' + form['lt'] + '|'
                    temp.save()

                current.st = '|'.join(slots)
                current.peer = '|'.join(peers)
                current.save()

        if sport == 'Squash':
            form = squash(request.POST)
            if form.is_valid():
                form = form.cleaned_data
                current = Booking.objects.get(dt=form['date'])
                pr = form['peer_reqd']
                print(pr)
                peers = current.peer.split('|')
                lts = current.lt.split('|')
                slots = current.st.split('|')
                i = lts.index(form['lt'])

                if slots[i] == 'free':
                    slots[i] = ''

                if peers[i] == 'no':
                    return render(request, 'home/nobooking.html', {"past_bookings": past_booking})

                if username not in slots[i]:
                    slots[i] += username + ','
                    peers[i] = pr
                    temp.upcoming_bookings += str(form['date']) + ';' + form['lt'] + '|'
                    temp.save()

                current.st = '|'.join(slots)
                current.peer = '|'.join(peers)
                current.save()

        booking_output = upcoming_booking(request)

        return render(request, 'home/bookingsuccessful.html', {"username": username, "bookings": booking_output})

    form = basketball()

    if sport == 'Basketball':
        form = basketball()

    if sport == 'Table Tennis':
        form = tabletennis()

    if sport == 'Squash':
        form = squash()

    return render(request, 'home/forms.html', {"form": form})

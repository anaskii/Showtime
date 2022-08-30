from django.shortcuts import render
import razorpay
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseBadRequest
from user.models import *
import simplejson as json
# authorize razorpay client with API Keys.
razorpay_client = razorpay.Client(
    auth=(settings.RAZOR_KEY_ID, settings.RAZOR_KEY_SECRET))


def Payment(request):
    booking_id = request.session['booking_id']
    print(booking_id)
    seat_length=request.session['seat_length']

    currency = 'INR'
    amount = 10000*int(seat_length)  # Rs. 100

    # Create a Razorpay Order
    razorpay_order = razorpay_client.order.create(dict(amount=amount,
                                                       currency=currency,
                                                       payment_capture='0'))

    # order id of newly created order.
    razorpay_order_id = razorpay_order['id']
    callback_url = 'paymenthandler/'

    # we need to pass these details to frontend.
    context = {}
    context['razorpay_order_id'] = razorpay_order_id
    context['razorpay_merchant_key'] = settings.RAZOR_KEY_ID
    context['razorpay_amount'] = amount
    context['currency'] = currency
    context['callback_url'] = callback_url

    return render(request, 'payment.html', context=context)


@csrf_exempt
def paymenthandler(request):
    # only accept POST request.
    if request.method == "POST":
        try:

            # get the required parameters from post request.
            payment_id = request.POST.get('razorpay_payment_id', '')
            razorpay_order_id = request.POST.get('razorpay_order_id', '')
            signature = request.POST.get('razorpay_signature', '')
            params_dict = {
                'razorpay_order_id': razorpay_order_id,
                'razorpay_payment_id': payment_id,
                'razorpay_signature': signature
            }

            # verify the payment signature.
            result = razorpay_client.utility.verify_payment_signature(params_dict)
            if result is not None:
                seat_length = request.session['seat_length']
                amount = 10000*int(seat_length)  # Rs. 100
                try:

                    # capture the payemt
                    razorpay_client.payment.capture(payment_id, amount)


                    try:
                        booking_id = request.session['booking_id']
                        booking = MovieBooking.objects.get(id=booking_id)
                        print(booking)
                        booking.paid = True
                        booking.save()
                        jsonDec = json.decoder.JSONDecoder()

                        seats_available_id = request.session['seats_available']
                        seats_available = Seat.objects.get(id=seats_available_id)

                        booked_seat_list = jsonDec.decode(seats_available.seats)

                        seat_list = request.session['booked_seats']
                        print(seat_list)

                        booked_seat_list = booked_seat_list + seat_list
                        print(booked_seat_list)

                        seats_available.seats = json.dumps(booked_seat_list)
                        seats_available.save()
                    except:
                        pass

                    # render success page on successful caputre of payment
                    return render(request, 'paymentsuccess.html')
                except:

                    # if there is an error while capturing payment.
                    return render(request, 'paymentfail.html')
            else:

                # if signature verification fails.
                return render(request, 'paymentfail.html')
        except:

            # if we don't find the required parameters in POST data
            return HttpResponseBadRequest()
    else:
        # if other than POST request is made.
        return HttpResponseBadRequest()

# Create your views here.

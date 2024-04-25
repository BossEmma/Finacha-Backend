from django.shortcuts import render
# Create your views here.
from django.shortcuts import render , redirect , get_object_or_404
from django.http import HttpResponse , HttpResponseRedirect , HttpRequest 
from django.contrib.auth import authenticate ,login ,logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.conf import settings
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User 
import random,datetime
import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
# Create your views here.
import datetime,time,requests

from itertools import zip_longest
import stripe

email_password = 'death2025'
sender_email = 'service@finacha.com'

def emailclient(text,html,receiver_email,message):
    part1 = MIMEText(text, "plain")
    part2 = MIMEText(html, "html")

    message.attach(part1)
    message.attach(part2)

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("mail.privateemail.com", 465, context=context) as server:
        server.login(sender_email, email_password)
        server.sendmail(
            sender_email, receiver_email, message.as_string()
        )
    pass


stripe.api_key = "sk_test_51P9QB3P58KTe8Zo2xl2mNQQPoAOFFkhA6h1GUSXX9YR5cowo0LXAvoAVl8h3y7lfEbdegR1csKZC46Kr4etO0XVY00pVFw7CcL"

# Set your secret key. Remember to switch to your live secret key in production.
# See your keys here: https://dashboard.stripe.com/apikeys
stripe.api_key = 'sk_test_51P9QB3P58KTe8Zo2xl2mNQQPoAOFFkhA6h1GUSXX9YR5cowo0LXAvoAVl8h3y7lfEbdegR1csKZC46Kr4etO0XVY00pVFw7CcL'

cardholder = stripe.issuing.Cardholder.create(
  name="Mark Smith",
  email="agwumafamelody@yahoo.com",
  phone_number="(+44) (0)1234 567890",
  status="active",
  type="individual",
  individual={
    "first_name": "Mark",
    "last_name": "Smith",
    "dob": {"day": 1, "month": 11, "year": 1981},
  },
  billing={
    "address": {
      "line1": "12 Upper Street",
      "city": "BIRMINGHAM",
      "postal_code": "B12 8RD",
      "country": "GB",
    },
  },
)

def Stripecard(request):
    cardholder = stripe.issuing.Cardholder.create(
      name="Mark Smith",
      email="agwumafamelody@yahoo.com",
      phone_number="(+44) (0)1234 567890",
      status="active",
      type="individual",
      individual={
        "first_name": "Mark",
        "last_name": "Smith",
        "dob": {"day": 1, "month": 11, "year": 1981},
      },
      billing={
        "address": {
          "line1": "12 Upper Street",
          "city": "BIRMINGHAM",
          "postal_code": "B12 8RD",
          "country": "GB",
        },
      },
    )
    pass
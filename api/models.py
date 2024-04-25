from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.conf import settings
from django.core import validators
from django.core.exceptions import ValidationError
from django_countries.fields import CountryField
from django.contrib.auth import get_user_model
import secrets
import smtplib, ssl
import datetime
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from django.contrib.auth.models import User as user_id
import random
from storages.backends.s3boto3 import S3Boto3Storage
from django.db.models.signals import pre_delete
from django.dispatch import receiver
import string
from django.utils import timezone
from .email_otp import text,otptext
# Create your models here.
User    = settings.AUTH_USER_MODEL


password = 'death2025'
sender_email = 'service@westpremiuminsured.com'

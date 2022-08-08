import pyotp
from django.conf import settings
from twilio.rest import Client
from decouple import config

account_sid = settings.TWILIO_ACCOUNT_SID
auth_token = settings.TWILIO_AUTH_TOKEN
twilio_phone = settings.TWILIO_PHONE_NUMBER
client = Client(account_sid, auth_token)


# send sms to phone number

def send_sms(phone_number, message):
    return client.messages.create(
        body=message,
        from_=twilio_phone,
        to=phone_number
    )


def generate_time_otp(user_key):
    time_otp = pyotp.TOTP(user_key, interval=int(config('TIME_OTP_DURATION', default=600)))
    time_otp = time_otp.now()
    return time_otp

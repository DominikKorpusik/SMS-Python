# config.py : where I keep my keys as constants
import config
from twilio.rest import Client

# Set environment variables for your credentials
client = Client(config.ACCOUNT_SID, config.AUTH_TOKEN)

message = client.messages.create(
    body="Check your EMAIL...",
    from_=config.FROM,
    to=config.TO
)

print(message.sid)

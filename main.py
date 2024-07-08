import base64
import os
from twilio.rest import Client
source_number = ###### a number that you want to use, for example from twilio
destination_number = ####### your targets
def hello_pubsub(event, context):
    """Triggered from a message on a Cloud Pub/Sub topic.
    Args:
         event (dict): Event payload.
         context (google.cloud.functions.Context): Metadata for the event.
    """
    pubsub_message = base64.b64decode(event['data']).decode('utf-8')
    print(pubsub_message)

    account_sid = ''
    auth_token = ''
    client = Client(account_sid, auth_token)
    
    message = client.messages.create(
                              body='Message from twillo pubsub : ' +pubsub_message,
                              from_=source_number,
                              to=destination_number
                          )

    print(message.sid)

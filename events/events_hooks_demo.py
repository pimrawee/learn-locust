from locust import HttpUser, task, constant
from locust.event import EventHook


# Create custom events using EventHook
send_email_notifications = EventHook()  # Event to handle email notifications
send_text_notifications = EventHook()   # Event to handle SMS text notifications


# Function to handle sending email notifications
def email(i, j, req_id, message=None, **kwargs):
    print("Sending", message, "in Email for the request", req_id)

# Add email function as listener for the send_email_notifications event
send_email_notifications.add_listener(email)


# Function to handle sending SMS text notifications
def sms_text(i, j, req_id, message=None, **kwargs):
    print("Sending", message, "in SMS for the request", req_id)

# Add sms_text function as listener for the send_text_notifications event
send_text_notifications.add_listener(sms_text)


class LoadTest(HttpUser):
    wait_time = constant(1)

    @task
    def home_page(self):
        # Send GET request to the home page
        with self.client.get("/", name="T00_HomePage", catch_response=True) as response:
            # Fire email and text notifications for success 
            if response.status_code == 200:
                send_email_notifications.fire(i=1, j=2, req_id=1, message="success")
                send_text_notifications.fire(i=1, j=2, req_id=2, message="success")
            # Fire email and text notifications for failure
            else:       
                send_email_notifications.fire(i=1, j=2, req_id=1, message="failed")
                send_text_notifications.fire(i=1, j=2, req_id=2, message="failed")

        # Send GET request to a failed page
        with self.client.get("/test", name="T10_FailedHomePage", catch_response=True) as response:
            # If the request is successful (status code 200)
            if response.status_code == 200:
                # Fire email and text notifications for success
                send_email_notifications.fire(i=1, j=2, req_id=3, message="success")
                send_text_notifications.fire(i=1, j=2, req_id=4, message="success")
            else:
                # Fire email and text notifications for failure
                send_email_notifications.fire(i=1, j=2, req_id=3, message="failed")
                send_text_notifications.fire(i=1, j=2, req_id=4, message="failed")


# locust -f path/file.py --config locust.conf
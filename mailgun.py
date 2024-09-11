import requests
import json

def send_simple_message():
    try:
        url = "https://api.mailgun.net/v3/mg.logichive.in/messages"
        api_key = "21a0c5d7feb30bcef6fd549eb5ea932f-623e10c8-3baf961c"  # Replace with your Mailgun API key
        template_name = "alert_share_link_host"
        from_email = "Mailgun Sandbox <postmaster@mg.logichive.in>"
        to_email = "Prathik Pai <shaheer@logichive.in>"
        mailgun_variables = {"test": "test"}  # Your custom variables for the template
        
        response = requests.post(
            url,
            auth=("api", api_key),
            data={
                "from": from_email,
                "to": to_email,
                "subject": "Hello Prathik Pai",
                "template": template_name,
                "h:X-Mailgun-Variables": json.dumps(mailgun_variables)  # Convert dict to JSON string
            }
        )
        
        response.raise_for_status()
        print(response)  # Raise an error for bad status codes
        
        print("Email sent successfully!")
    except requests.exceptions.RequestException as e:
        print(f"Error sending email: {e}")

send_simple_message()


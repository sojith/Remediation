# Remediation

webhook.py is a python script which hosts an end point. Dynatrace or any monitoring tool can be configured to sent alerts to this endpoint
Webhook.py upon recieving the alert will call the trigger.sh

Webhook.py can be updated to introduce a condition which checks for the nature of the alert (Fer e.g. check if the alert has "disk space" in it. Check for the server name and check for the filesystem)
If the conditon is fulfilled then the Webhook.py can call the appropriate trigger script (For e.g. a script to shh to the server name captured in the alert, and then run a cleanup script on the filesystem provided in the alert)

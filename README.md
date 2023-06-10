# SelfHealing or AutoRemediation 

This project is meant to show how commonly occuring operations alerts can be resolved automatically. For e.g. a disk space alert can be use to automaticlaly trigger a clean up script which clears space in the disk/filesystem

_webhook.py_ is a python script which hosts an end point. Dynatrace or any monitoring tool can be configured to sent alerts to this endpoint. Webhook.py upon recieving the alert  calls the trigger.sh

Webhook.py can be customized to introduce a condition which checks for the nature of the alert (Fer e.g. check if the alert has "disk space" in it. Check for the server name and check for the filesystem)
If the conditon is fulfilled then the Webhook.py can call the appropriate trigger script (For e.g. a script to shh to the server name captured in the alert, and then run a cleanup script on the filesystem provided in the alert)

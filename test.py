from azure.servicebus import QueueClient


queue_client = QueueClient.from_connection_string(conn_str=
    "Endpoint=sb://servicebusproject.servicebus.windows.net/;SharedAccessKeyName=RootManageSharedAccessKey;SharedAccessKey=4wFxuRDN0Bnlvsjq4w+VzuwQmzVaegpIf+ASbHF+vKE=",
    name="notificationque"
)



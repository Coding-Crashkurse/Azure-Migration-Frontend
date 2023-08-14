import os

app_dir = os.path.abspath(os.path.dirname(__file__))

class BaseConfig:
    DEBUG = True
    POSTGRES_URL="azureudacitydb.postgres.database.azure.com"
    POSTGRES_USER="codingcrashcourses"
    POSTGRES_PW="123Password"
    POSTGRES_DB="techconfdb"
    DB_URL = 'postgresql://{user}:{pw}@{url}/{db}'.format(user=POSTGRES_USER,pw=POSTGRES_PW,url=POSTGRES_URL,db=POSTGRES_DB)
    SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI') or DB_URL
    CONFERENCE_ID = 1
    SECRET_KEY = 'LWd2tzlprdGHCIPHTd4tp5SBFgDszm'
    SERVICE_BUS_CONNECTION_STRING = "Endpoint=sb://servicebusproject.servicebus.windows.net/;SharedAccessKeyName=RootManageSharedAccessKey;SharedAccessKey=4wFxuRDN0Bnlvsjq4w+VzuwQmzVaegpIf+ASbHF+vKE="
    ADMIN_EMAIL_ADDRESS: 'datamastery87@gmail.com'
    SENDGRID_API_KEY = "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"

class DevelopmentConfig(BaseConfig):
    DEBUG = True


class ProductionConfig(BaseConfig):
    DEBUG = False
import os
from dotenv import load_dotenv
import sys

load_dotenv()

sys.path.append('/srv/http/scims')
sys.path.append('/srv/http/scims/scims')
sys.path.append('/srv/http/scims/venv/lib/python3.9/site-packages')


from django.core.wsgi import get_wsgi_application
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'scims.settings')
application = get_wsgi_application()

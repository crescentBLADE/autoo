#!C:\Users\zh\AppData\Local\Programs\Python\Python36\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'django==2.0','console_scripts','django-admin'
__requires__ = 'django==2.0'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('django==2.0', 'console_scripts', 'django-admin')()
    )

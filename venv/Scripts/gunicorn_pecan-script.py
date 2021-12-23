#!c:\users\sensai\desktop\serverless\fastapi_serverless-1\venv\scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'pecan==1.4.1','console_scripts','gunicorn_pecan'
__requires__ = 'pecan==1.4.1'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('pecan==1.4.1', 'console_scripts', 'gunicorn_pecan')()
    )

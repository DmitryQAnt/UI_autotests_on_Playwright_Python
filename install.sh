#! /bin/sh -eu
python3 -m pip install -r ./sms_web/requirements.txt --quiet
playwright install --with-deps
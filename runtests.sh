#!/bin/sh
export DATABASE_URL='postgres://postgres:@/test_controlinterface'
export DJANGO_SETTINGS_MODULE="controlinterface.testsettings"
./manage.py test "$@"
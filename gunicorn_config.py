command = '/var/www/redhaus/env/bin/gunicorn'
pythonpath = '/var/www/redhaus/redhaus_project/'
bind = '127.0.0.1:8001'
workers = 3
user = 'tyshbyr'
limit_request_fields = 32000
limit_request_fields_size = 0
rav_env = 'DJANGO_SETTINGS_MODULE=config.settings'

# Access log - records incoming HTTP requests
accesslog = "/var/log/gunicorn.access.log"

# Error log - records Gunicorn server goings-on
errorlog = "/var/log/gunicorn.error.log"

# Whether to send Django output to the error log
capture_output = False

# How verbose the Gunicorn error logs should be
loglevel = "info"
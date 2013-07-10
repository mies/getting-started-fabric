import os

def number_of_cpus():
  if not hasattr(os, "sysconf"):
    raise RuntimeError("No sysconf detected.")
  return os.sysconf("SC_NPROCESSORS_ONLN")
bind = "0.0.0.0:5000"
workers = number_of_cpus() * 2 + 1
backlog = 2048
worker_class = "gevent"
debug = True
daemon = True
pidfile =  "/tmp/gunicorn.pid"
logfile = "/tmp/gunicorn.log"

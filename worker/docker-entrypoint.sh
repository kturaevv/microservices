#!/bin/sh

# Start celery daemons
/etc/init.d/celeryd start

# Start consuming messages from rabbit
cd .. && python3 -m worker.main
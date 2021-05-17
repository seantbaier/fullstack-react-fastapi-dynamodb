#! /usr/bin/env sh
set -e

DEFAULT_MODULE_NAME=app.main

MODULE_NAME=${MODULE_NAME:-$DEFAULT_MODULE_NAME}
VARIABLE_NAME=${VARIABLE_NAME:-app}
export APP_MODULE=${APP_MODULE:-"$MODULE_NAME:$VARIABLE_NAME"}

HOST=${HOST:-0.0.0.0}
PORT=${PORT:-80}
LOG_LEVEL=${LOG_LEVEL:-info}

# # If there's a prestart.sh script in the / directory or other path specified, run it before starting
PRE_START_PATH=${PRE_START_PATH:-/bin/prestart.sh}
echo "Checking for script in $PRE_START_PATH"

if [ -f $PRE_START_PATH ] ; then
    echo "Running script $PRE_START_PATH"
    . "$PRE_START_PATH"
else 
    echo "There is no script $PRE_START_PATH"
fi

# Start Uvicorn with live reload
exec uvicorn --reload --reload-dir $VARIABLE_NAME --host $HOST --port $PORT --log-level $LOG_LEVEL "$APP_MODULE"
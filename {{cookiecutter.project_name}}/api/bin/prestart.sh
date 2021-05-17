#! /usr/bin/env bash

# Let the DB start
python /scripts/pre_start.py

# Run migrations here

# Create initial data in DB
python /scripts/initial_data.py

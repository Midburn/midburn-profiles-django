#!/usr/bin/env bash
waitress-serve --port=7550 --threads=5 --connection-limit=100 src.wsgi:application
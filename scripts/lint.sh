#!/bin/bash -e

APP_PATH="app"

ruff $APP_PATH 
black $APP_PATH --check
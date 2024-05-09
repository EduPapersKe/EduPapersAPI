#!/bin/bash -e

APP_PATH="app"

ruff $APP_PATH --fix
black $APP_PATH
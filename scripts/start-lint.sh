#!/bin/bash

# Project Folders
TARGET_FOLDERS="app"

# Run Tools
isort $TARGET_FOLDERS -c --diff
black --check --diff $TARGET_FOLDERS 
pycodestyle $TARGET_FOLDERS
flake8 $TARGET_FOLDERS
mypy $TARGET_FOLDERS

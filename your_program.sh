#!/bin/sh
#
# Use this script to run your program LOCALLY.
#
# Note: Changing this script WILL NOT affect how CodeCrafters runs your program.
#
# Learn more: https://codecrafters.io/program-interface

set -e # Exit early if any commands fail

# Copied from .codecrafters/run.sh
#
# - Edit this to change how your program runs locally
# - Edit .codecrafters/run.sh to change how your program runs remotely

SCRIPT_DIR="$(dirname "$0")" # <- dirname will extract the file directory name

# echo $0 # <- "$0" provides the name of where the file is being run from, if I'm in the main directory it would be ".", a diff directory would be "another/directory/bro"

# echo $SCRIPT_DIR 

PYTHONSAFEPATH=1 PYTHONPATH="$SCRIPT_DIR" exec uv run \
  --project "$SCRIPT_DIR" \
  --quiet \
  -m app.main \
  "$@"

#!/bin/bash
cd "$(dirname "$0")"
echo "Running run_timer..."
wine "run_timer" || ./"run_timer" "$@"

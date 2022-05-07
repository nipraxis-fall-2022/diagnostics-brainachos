#!/bin/bash
# Write, test, unwrite and check
# This is script only to prepare exercise.
nxt-proc-solutions write-solutions
pytest findoutlie
python scripts/validate_data.py data/group-*
nxt-proc-solutions write
nxt-proc-solutions check

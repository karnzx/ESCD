#!/bin/bash

if [[ -z "$1" ]]; then
  echo "usage: $0 {testfile.py}"
  exit -1
fi

python -m unittest -v $1

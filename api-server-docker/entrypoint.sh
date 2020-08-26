#!/usr/bin/env bash

service ssh start
echo "ENTRYPOINT: $@"
eval "$@"
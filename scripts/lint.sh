#!/bin/bash

set -e

RISK="${0%/*}"/..

pushd $RISK
uv ruff format
popd
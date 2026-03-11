#!/bin/bash

set -e

RISK="${0%/*}"/..

pushd $RISK
uv run ruff format
popd
#!/usr/bin/env bash
set -e

apt-get update && apt-get install -y gcc

cd /sauna
pip install pyinstaller
pip install -r requirements.txt

# pyinstaller part
pyinstaller sauna.spec
./dist/sauna --version
rm -rf build/

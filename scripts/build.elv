#!/usr/bin/env elvish

mkdir -p dist
rm -r dist/*

cp micropython/boot.py dist/boot.py

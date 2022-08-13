#!/usr/bin/env elvish

mkdir -p dist
rm -r dist/*

echo "=== Copying micropython code..."
cp micropython/boot.py dist/boot.py

echo "=== Building Svelte app..."
cd svelte
npm run build
cd ../
echo "=== Copying Svelte app..."
cp -R svelte/public dist/
echo "=== Done!"

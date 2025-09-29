#!/bin/bash
for file in "$@"; do
  if ! head -n 1 "$file" | grep -q "/\*\* @odoo-module \*/"; then
    echo "Fixing $file (adding @odoo-module header)"
    tmpfile=$(mktemp)
    echo "/** @odoo-module */" > "$tmpfile"
    cat "$file" >> "$tmpfile"
    mv "$tmpfile" "$file"
  fi
done

#!/bin/bash
for file in "$@"; do
  if ! head -n 1 "$file" | grep -q "# -*- coding: utf-8 -*-"; then
    echo "Fixing $file (adding utf-8 header)"
    tmpfile=$(mktemp)
    echo "# -*- coding: utf-8 -*-" > "$tmpfile"
    cat "$file" >> "$tmpfile"
    mv "$tmpfile" "$file"
  fi
done

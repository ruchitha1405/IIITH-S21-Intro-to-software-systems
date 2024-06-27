
#!/bin/bash

echo "1. Words - start with ‘s’ and is not follow by ‘a’"
echo `grep -E -ow "(s[b-zA-Z0-9][a-zA-Z0-9]*|s)"  $1`
echo "2. Words - start with ‘w’ and is  followed by ‘h’"
echo `grep -E -ow "wh[a-zA-Z0-9]*"  $1`

echo "3. Words - start with ‘t’ and is followed by 'h'"
echo `grep -E -ow "th[a-zA-Z0-9]*"  $1`

echo "4. Words - start with ‘a’ and is not followed by ‘n’"
echo `grep -E -ow "(a[a-mo-zA-Z0-9][a-zA-Z0-9]*|a)"  $1`



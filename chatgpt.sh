#!/bin/sh

echo "\n[+] Loading..."

curl=`cat <<EOS
curl -s https://api.openai.com/v1/completions \
  -H 'Content-Type: application/json' \
  -H "Authorization: Bearer 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" \
  -d '{
  "model": "text-davinci-003",
  "prompt": "$1",
  "max_tokens": 4000,
  "temperature": 1.0

}' \
--insecure
EOS`

eval ${curl}

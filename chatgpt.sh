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
--insecure | jq -r '.choices[]'.text
EOS`

eval ${curl}

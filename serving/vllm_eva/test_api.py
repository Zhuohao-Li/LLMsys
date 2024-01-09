#!/bin/bash

python -m vllm.entrypoints.api_server

VLLM_USE_MODELSCOPE=True python -m vllm.entrypoints.api_server \
   --model="qwen/Qwen-7B-Chat" \
   --revision="v1.1.8" \
   --trust-remote-code

curl http://localhost:8000/generate \
    -d '{
        "prompt": "San Francisco is a",
        "use_beam_search": true,
        "n": 4,
        "temperature": 0
    }'

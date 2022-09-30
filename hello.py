# Took code from Lab-Session
#!/usr/bin/env python3

import os, json

env ={}

for env_key, env_value in os.environ.items():
    env[env_key] = env_value

print("Content-Type: application/json")
print()

print(json.dumps(env))
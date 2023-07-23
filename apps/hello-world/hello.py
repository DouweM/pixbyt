import sys
import json

input = json.loads(sys.argv[1])
name = input["name"]

response = f"Hello, {name}!"

output = {"response": response}
print(json.dumps(output))

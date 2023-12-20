import json

# Open the 'data.json' file in read mode and store its content in a variable
with open('data.json', 'r') as f:
    content = f.read()

# Parse the JSON-formatted string into a dictionary
data = json.loads(content)

# Add a new key-value pair to the dictionary
data["country"] = "Morocco"  

# Open the 'data.json' file in write mode and overwrite its content with the modified data
with open('data.json', 'w') as f:
    json.dump(data, f, indent=2)

# Open the 'data.json' file again in read mode to retrieve the modified content
with open('data.json', 'r') as f:
    new_content = f.read()

print(new_content)  # Display the modified content of the 'data.json' file

import json

# Read the us.txt file
with open('us.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()

# Extract college names (middle column)
college_names = []
for line in lines:
    parts = line.strip().split('\t')
    if len(parts) >= 2:
        college_name = parts[1]
        college_names.append(college_name)

# Save to JSON file
with open('college_names.json', 'w', encoding='utf-8') as f:
    json.dump(college_names, f, indent=2, ensure_ascii=False)

print(f"Extracted {len(college_names)} college names")
print("Output saved to college_names.json")

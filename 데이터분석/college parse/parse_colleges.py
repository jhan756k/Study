import json

# Read the us.txt file
with open('us.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()

# Extract college names with their numbers
colleges = []
for line in lines:
    parts = line.strip().split('\t')
    if len(parts) >= 2:
        number = parts[0]
        college_name = parts[1]
        # Try to convert number to int for proper sorting, skip if not a number
        try:
            num = int(number)
            colleges.append((num, college_name))
        except ValueError:
            # Skip lines where the first column is not a number (like "Un")
            pass

# Sort by number
colleges.sort(key=lambda x: x[0])

# Extract just the college names in sorted order
college_names = [name for num, name in colleges]

# Save to JSON file
with open('college_names.json', 'w', encoding='utf-8') as f:
    json.dump(college_names, f, indent=2, ensure_ascii=False)

print(f"Extracted {len(college_names)} college names")
print("Output saved to college_names.json")

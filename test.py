import json

# Load the taxonomy data from the JSON file
with open('taxonomy2.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

# Initialize a dictionary to hold categories for each modality
modality_categories = {
    'text': [],
    'visual': [],
    'speech': [],
    'other': []
}

# Loop through the data to populate the dictionary with categories
for modality in data:
    modality_name = modality['name'].lower()  # Normalize the modality name
    if modality_name in modality_categories:
        for category in modality['values']:
            modality_categories[modality_name].append(category['name'])

# Print out the categories for each modality
for modality_name, categories in modality_categories.items():
    print(f"{modality_name.capitalize()} Modality Categories:")
    print(categories)
    print()  # Print a newline for better readability

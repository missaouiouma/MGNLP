import json

from matplotlib import pyplot as plt

with open("taxonomy.json", 'r', encoding='utf-8') as file:
    modified_data = json.load(file)

category_counts = {}
task_counts = {}

for modality in modified_data:
    modality_name = modality["name"]
    category_counts[modality_name] = len(modality["values"])
    task_counts[modality_name] = sum(len(category["values"]) for category in modality["values"])

category_counts, task_counts

fig, axs = plt.subplots(1, 2, figsize=(14, 6))

# Histogramme pour le nombre de catégories dans chaque modalité
axs[0].bar(category_counts.keys(), category_counts.values(), color='skyblue')
axs[0].set_title('Nombre de catégories par modalité')
axs[0].set_xlabel('Modalité')
axs[0].set_ylabel('Nombre de catégories')

# Histogramme pour le nombre de tâches dans chaque modalité
axs[1].bar(task_counts.keys(), task_counts.values(), color='lightgreen')
axs[1].set_title('Nombre de tâches par modalité')
axs[1].set_xlabel('Modalité')
axs[1].set_ylabel('Nombre de tâches')

plt.tight_layout()
plt.show()



import json

# Assuming 'data' is your JSON object that includes multiple records like those you provided
with open('datasets_info+card.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

# Fusionner 'tags' et 'task_ids' en un seul label 'task_ids'
for item in data:
    if item is not None and 'cardData' in item:
        cardData = item['cardData']
        if cardData is not None:
            # S'assurer que 'tags' et 'task_ids' existent et sont des listes
            if 'tags' in cardData and 'task_ids' in cardData:
                combined_ids = list(set(cardData['tags'] + cardData['task_ids']))
            elif 'tags' in cardData:
                combined_ids = list(set(cardData['tags']))
            elif 'task_ids' in cardData:
                combined_ids = list(set(cardData['task_ids']))
            else:
                combined_ids = []

            # Mettre à jour 'task_ids' avec les identifiants combinés
            cardData['task_ids'] = combined_ids

# Créer un tableau unique pour les catégories avec leurs tâches
unique_category_task_pairs = []
seen_pairs = set()  # Pour contrôler la redondance

for item in data:
    if item is not None and 'cardData' in item:
        cardData = item['cardData']
        if cardData is not None and 'task_categories' in cardData and 'task_ids' in cardData:
            for category in cardData['task_categories']:
                for task_id in cardData['task_ids']:
                    pair = (category, task_id)
                    if pair not in seen_pairs:
                        seen_pairs.add(pair)
                        unique_category_task_pairs.append({'category': category, 'task': task_id})

# Afficher ou retourner la liste des paires uniques
print(unique_category_task_pairs)
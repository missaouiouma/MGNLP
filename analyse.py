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

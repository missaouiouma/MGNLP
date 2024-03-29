"""""
import json
json_file_path = 'metadata_v2.json'

# Charger les données JSON
with open(json_file_path, 'r', encoding='utf-8') as file:
    data = json.load(file)


tasks_to_categories = {
    "automatic-speech-recognition": "speech-recognition",
    "data-mining": "text-mining",
    "parsing": "natural-language-processing",
    "translation": "synthetic-language",
    "knowledge-base": "conversational",
    "NCI-PID-PubMed": "conversational",
    "head-pose-estimation": "computer-vision",
    "image-self-supervised": "image-classification"
}

# Changements spécifiques des noms de tâches
task_renames = {
    "other-other-query-based-multi-document-summarization": "query-based-multi-document-summarization",
    "text-classification-other-sarcasm-detection": "sarcasm-detection",
    "other-other-knowledge-base": "knowledge-base",
    "text-classification-other-simplification-evaluation": "simplification-evaluation",
    "summarization-other-patent-summarization": "patent-summarization",
    "summarization-other-bills-summarization": "bills-summarization",
    "other-other-head-pose-estimation": "head-pose-estimation",
    "other-other-translation": "translation",
    "other-other-knowledge-extraction": "knowledge-extraction",
    "other-other-relation-extraction": "relation-extraction",
    "other-other-disambiguation": "disambiguation",
    "token-classification-other-fused-head-identification": "fused-head-identification",
    "other-image-self-supervised": "image-self-supervised",
    "other-other-data-mining":"data-mining",
    "other-other-NCI-PID-PubMed":"NCI-PID-PubMed"
}

for entry in data:
    entry_data = entry.get("data", {})
    tasks = entry_data.get("tasks", [])
    updated_tasks = [task_renames.get(task, task) for task in tasks]
    entry_data["tasks"] = updated_tasks

# Saving the corrected data to a new JSON file
corrected_file_path = "updated_metadata_v3.json"
with open(corrected_file_path, "w", encoding="utf-8") as file:
    json.dump(data, file, indent=4, ensure_ascii=False)

"""""
import json

file_path = 'updated_metadata_v3.json'

with open(file_path, 'r', encoding='utf-8') as file:
    data = json.load(file)

tasks_to_categories = {
    "automatic-speech-recognition": "speech-recognition",
    "data-mining": "text-mining",
    "parsing": "natural-language-processing",
    "translation": "synthetic-language",
    "knowledge-base": "conversational",
    "NCI-PID-PubMed": "conversational",
    "head-pose-estimation": "computer-vision",
    "image-self-supervised": "image-classification"
}

for dataset in data:
    if "tasks" in dataset["data"]:
        tasks = dataset["data"]["tasks"]
        categories = dataset["data"].get("categories", [])

        for task in tasks:
            if task in tasks_to_categories:
                new_category = tasks_to_categories[task]
                if new_category not in categories:
                    categories.append(new_category)

        dataset["data"]["categories"] = categories

final_updated_file_path = "updated_metadata_v3.json"
with open(final_updated_file_path, "w", encoding="utf-8") as file:
    json.dump(data, file, indent=4, ensure_ascii=False)
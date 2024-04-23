import json
# Charger les données depuis le fichier JSON
with open('C:/Users\hp\OneDrive\Documents\datasets_info+card.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

# Mots-clés pour classifier les tâches
keywords = {
    'text': ['text-classification', 'token-classification',
             'question-answering', 'text-generation',
             'fill-mask',  'translation', 'summarization',
             'text2text-generation',  'multiple-choice', 'text-retrieval',
             'conversational', 'visual-question-answering',
             'tabular-to-text', 'table-to-text',
             'automatic-speech-recognition', 'image-to-text',
             'zero-shot-classification', 'sequence-modeling',
             'zero-shot-retrieval', 'information-retrieval',
             'zero-shot-information-retrieval', 'structure-prediction',
             'conditional-text-generation', 'paraphrase',
             'paraphrase detection', 'news-classification',
             'named-entity-recognition', 'sentence-similarity',
             'text-scoring', 'other-test',
             'named-entity-disambiguation',
             'code-generation', 'textual-entailment',
             'natural-language-inference', 'sentiment-analysis',
             'machine-translation', 'text-mining',
             'text_classification', 'Automatic-Speech-Recognition',
             'question-answering-retrieval', 'text',
             'linear-regression', 'table-question-answering',
             'tabular-classification', 'text-to-image',
             'paraphrase-mining', 'commonsense-reasoning',
             'moral-reasoning', 'social-reasoning',
             'coreference resolution', 'commonsense reasoning',
             'text-understanding', 'text-comprehension',
             'natural-language-understanding', 'natural-language-generation',
             'reinforcement-learning', 'tabular-regression'],

    'speech': ['audio-classification', 'speech-processing',
               'audio-to-audio', 'text-to-speech', 'text-to-audio'],

    'visual' : ['image-classification', 'image-segmentation',
                'object-detection', 'masked-auto-encoding',
                'rendered-language-modelling', 'video-captionning',
                'feature-extraction', 'zero-shot-image-classification',
                'image-to-image', 'image-generation', 'unconditional-image-generation',
                'video-classification', 'image-to-3d']

}

# Structure modifiée basée sur le modèle de taxonomie avec 'other' ajouté
modified_json = [{'name': 'text', 'type': 'modality', 'values': []},
                 {'name': 'speech', 'type': 'modality', 'values': []},
                 {'name': 'visual', 'type': 'modality', 'values': []},
                 {'name': 'other', 'type': 'modality', 'values': []}]

def classify_category_based_on_keywords(category, keywords):
    category_lower = category.lower()
    for modality, kws in keywords.items():
        if any(keyword.lower() in category_lower for keyword in kws):
            return modality
    return 'other'  # Retourne 'other' si aucune correspondance n'est trouvée

def add_task_to_category_in_modality(category_name, task_name, modality_name, modified_json):
    for modality in modified_json:
        if modality["name"] == modality_name:
            category = next((cat for cat in modality["values"] if cat["name"] == category_name), None)
            if not category:
                category = {"name": category_name, "type": "category", "values": []}
                modality["values"].append(category)
            if not any(task["name"] == task_name for task in category["values"]):
                category["values"].append({"name": task_name, "type": "task"})
            break

for item in data:
    if item is not None and 'cardData' in item:
        cardData = item['cardData']
        if 'task_categories' in cardData and 'task_ids' in cardData:
            task_categories = cardData['task_categories']
            task_ids = cardData['task_ids']
            for category in task_categories:
                modality_name = classify_category_based_on_keywords(category, keywords)
                for task in task_ids:
                    add_task_to_category_in_modality(category, task, modality_name, modified_json)

# Sauvegarder dans un nouveau fichier JSON
with open('taxonomy2.json', 'w', encoding='utf-8') as modified_file:
    json.dump(modified_json, modified_file, indent=4)
    print("done")


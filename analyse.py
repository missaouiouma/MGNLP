import json

# Chemins des fichiers
input_file_path = 'taxonomy2.json'
output_file_path = 'final_version.json'

import json
# Chargement des données de taxonomie
with open(input_file_path, 'r', encoding='utf-8') as file:
    taxonomy_data = json.load(file)


# Filtrer les données
filtered_data = [item for item in taxonomy_data if not (item.get('modality', '') == 'other' and item.get('category', '') == 'other')]

with open('taxonomy2.json', 'w', encoding='utf-8') as file:
    json.dump(filtered_data, file, indent=4, ensure_ascii=False)

# Chargement des données de taxonomie
with open(input_file_path, 'r', encoding='utf-8') as file:
    taxonomy_data = json.load(file)

# Filtrer les données
filtered_data = [item for item in taxonomy_data if
                 not (item.get('modality', '') == 'other' and item.get('category', '') == 'other')]

with open('taxonomy2.json', 'w', encoding='utf-8') as file:
    json.dump(filtered_data, file, indent=4, ensure_ascii=False)

renaming_rules = {
    "other": {
        "abstractive-qa": "Q&A",
        "extractive-qa": "Q&A",
        "multiple-choice-qa": "Assessment",
        "open-domain-qa": "Open QA",
        "closed-domain-qa": "Closed QA",
        "natural-language-inference": "NLI",
        "language-modeling": "Language Processing",
        "masked-language-modeling": "Language Processing",
        "dialogue-modeling": "Dialogue Systems",
        "parsing": "Text Analysis",
        "sentiment-classification": "Text Analysis",
        "slot-filling": "Text Analysis",
        "named-entity-recognition": "Text Analysis",
        "part-of-speech": "Text Analysis",
        "coreference-resolution": "Text Analysis",
        "semantic-similarity-classification": "Text Analysis",
        "lemmatization": "Text Analysis",
        "intent-classification": "Dialogue Systems",
        "fact-checking": "Information Verification",
        "multi-class-classification": "Text Analysis",
        "multi-label-classification": "Text Analysis",
        "text-scoring": "Text Analysis",
        "hate-speech-detection": "Text Analysis",
        "image-classification": "Image Processing",
        "multi-label-image-classification": "Image Processing"

    },
}


# Fonction pour renommer les catégories basées sur des critères spécifiques
def apply_renaming_rules(data, rules):
    for modality in data:
        if modality['name'] in rules:
            for category in modality['values']:
                for task in category['values']:
                    if task['name'] in rules[modality['name']]:
                        category['name'] = rules[modality['name']][task['name']]
    return data


# Appliquer les règles de renommage
updated_taxonomy = apply_renaming_rules(taxonomy_data, renaming_rules)

# Sauvegarder les données modifiées dans un nouveau fichier JSON
with open(output_file_path, 'w', encoding='utf-8') as file:
    json.dump(updated_taxonomy, file, indent=4)

print("Category renaming completed. Updated taxonomy saved to", output_file_path)

# Listes de modalités
text_modalities = [
'text-classification', 'token-classification',
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
             'reinforcement-learning', 'tabular-regression',"Q&A", "Assessment", "Open QA", "Closed QA", "NLI", "Language Processing", "Dialogue Systems",
              "Text Analysis", "Information Verification"
]
speech_modalities = [
'audio-classification', 'speech-processing','audio-to-audio', 'text-to-speech', 'text-to-audio', "Speech Recognition", "Speech Synthesis", "Speaker Identification", "Speech Translation"
]
visual_modalities = [
    "Image Processing", "Video Processing", "Visual Recognition", "Image Segmentation",'image-classification', 'image-segmentation',  'object-detection', 'masked-auto-encoding',   'rendered-language-modelling', 'video-captionning',
                'feature-extraction', 'zero-shot-image-classification',
                'image-to-image', 'image-generation', 'unconditional-image-generation',
                'video-classification', 'image-to-3d',
]

time_series_modality = ['time-series-forecasting']
# Charger les données de taxonomie existantes
with open(input_file_path, 'r', encoding='utf-8') as file:
    taxonomy_data = json.load(file)

# Nouvelle structure de données basée sur les modalités
new_taxonomy = {
    "text": [],
    "speech": [],
    "visual": [],
    "time_series": []
}

# Fonction pour refactoriser les catégories selon les modalités
def refactor_taxonomy(data):
    for modality in data:
        for category in modality['values']:  # S'assure que chaque catégorie est traitée
            category_name = category['name']
            new_category = {
                "name": category_name,
                "values": category['values']  # Conserve les tâches et leurs datasets
            }
            if category_name in text_modalities:
                new_taxonomy['text'].append(new_category)
            elif category_name in speech_modalities:
                new_taxonomy['speech'].append(new_category)
            elif category_name in visual_modalities:
                new_taxonomy['visual'].append(new_category)
            elif category_name in time_series_modality:
                new_taxonomy['time_series'].append(new_category)

# Appliquer la refactorisation
refactor_taxonomy(taxonomy_data)

# Sauvegarder la nouvelle taxonomie dans un fichier JSON
with open(output_file_path, 'w', encoding='utf-8') as file:
    json.dump(new_taxonomy, file, indent=4)

print("Taxonomy refactoring completed. New taxonomy saved to", output_file_path)
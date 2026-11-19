---
title: "Unlimited-OCR — Mémo"
type: memo
fiche: "[[Unlimited-OCR]]"
date: 2026-11-19
---

# Unlimited-OCR — Mémo

> Tester Unlimited OCR 2 sur une image ou un document multipage avec Transformers. Voir la [[Unlimited-OCR|fiche]] et les [[Unlimited-OCR#Avis indépendants|essais indépendants]].

## Installation

Baidu documente Python 3.10 et CUDA. Clone son dépôt pour disposer du convertisseur, puis installe les dépendances de l'exemple Transformers.

```bash
git clone \
  https://github.com/baidu/Unlimited-OCR
cd Unlimited-OCR
pip install torch==2.13.0 torchvision \
  pillow transformers==4.52.1 \
  huggingface-hub==0.36.0 \
  tokenizers==0.21.4 addict==2.4.0 \
  einops==0.8.2 easydict==1.13
```

## Commandes principales

### Charger les poids

```python
import torch
from transformers import AutoModel
from transformers import AutoTokenizer

checkpoint = "baidu/Unlimited-OCR-2"
tokenizer = AutoTokenizer.from_pretrained(
    checkpoint, trust_remote_code=True
)
model = AutoModel.from_pretrained(
    checkpoint,
    trust_remote_code=True,
    use_safetensors=True,
    torch_dtype=torch.bfloat16,
).eval().cuda()
```

### Lire une ou plusieurs pages

```python
text = model.infer(
    tokenizer,
    image_file="page_1.jpg",
    output_path="output/single",
    save_results=True,
)
text, num_tokens = model.infer_multi(
    tokenizer,
    image_files=[
        "page_1.jpg", "page_2.jpg",
    ],
    output_path="output/multi",
    save_results=True,
)
```

Passe les images dans l'ordre du PDF. Pour les obtenir, le README montre une conversion avec PyMuPDF.

### Convertir la sortie en Markdown

Depuis le dépôt Baidu, isole `result_raw.md`, la sortie brute de l'exemple multipage. Le convertisseur traite chaque fichier texte du répertoire d'entrée.

```bash
mkdir -p raw
cp output/multi/result_raw.md \
  raw/document.md
python utils/process_unlimitedOCR2.py \
  --infer-dir raw --out-dir pred
```

## Conseils d'utilisation

- Commencer par quelques pages avec un tableau ou des colonnes. Vérifier que la sortie contient toutes les pages et contrôler les chiffres dans le PDF.
- Examiner et épingler la révision des poids avant d'utiliser `trust_remote_code=True` dans un environnement de travail.
- Pour servir le modèle, suivre la configuration SGLang du dépôt. Baidu fournit un paquet adapté et des paramètres de fenêtres pour les documents longs.

## Sources

- [Installation et inférence officielles](https://github.com/baidu/Unlimited-OCR#inference).
- [Convertisseur Markdown de Baidu](https://github.com/baidu/Unlimited-OCR/tree/main/utils).

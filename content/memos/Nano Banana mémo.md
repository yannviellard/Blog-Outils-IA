---
title: "Nano Banana — Mémo"
type: memo
fiche: "[[Nano Banana]]"
date: 2026-10-11
---

# Nano Banana — Mémo

> Appeler les modèles [[Nano Banana]] depuis la Gemini API en Python : identifiants de modèles, génération, retouche avec image de référence, ratio et taille.

## Identifiants de modèles

|Modèle public|Identifiant API|
|---|---|
|Nano Banana 2.1|`gemini-nano-banana-2.1`|
|Nano Banana 2 Lite|`gemini-3.1-flash-lite-image`|
|Nano Banana 2|`gemini-3.1-flash-image`|
|Nano Banana Pro|`gemini-3-pro-image`|
|Nano Banana (historique)|`gemini-2.5-flash-image`|

## Générer une image

```python
from google import genai
import base64

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-nano-banana-2.1",
    input="Crée l'image d'un plat de bananes dans un restaurant chic, thème Gemini",
)

with open("generated_image.png", "wb") as f:
    f.write(base64.b64decode(interaction.output_image.data))
```

## Retoucher avec une image de référence

```python
with open("/chemin/vers/image.png", "rb") as f:
    image_bytes = f.read()

interaction = client.interactions.create(
    model="gemini-nano-banana-2.1",
    input=[
        {"type": "text", "text": "Ajoute un chapeau de cuisinier sur le plat"},
        {
            "type": "image",
            "data": base64.b64encode(image_bytes).decode("utf-8"),
            "mime_type": "image/png",
        },
    ],
)
```

## Ratio et taille

```python
response_format={
    "type": "image",
    "mime_type": "image/jpeg",
    "aspect_ratio": "16:9",
    "image_size": "2K",
}
```

La taille s'écrit avec un `K` majuscule (`1K`, `2K`, `4K`) : la minuscule est refusée. Nano Banana 2 Lite ne gère que `1K`.

## Conseils d'utilisation

- **Itérer par conversation** plutôt que de refaire le prompt entier.
- **Vérifier chaque donnée, date et légende** d'une infographie : un rendu crédible peut contenir des erreurs factuelles.
- **Fournir des références** pour conserver identité, proportions et composition.
- **Choisir le modèle selon le besoin** : Lite pour le volume, 2 pour le quotidien, Pro pour les compositions exigeantes.
- **Contrôler les droits, le texte généré et la cohérence de marque** avant publication ; le filigrane SynthID est incorporé aux images.

## Sources

- [Gemini API — génération d'images](https://ai.google.dev/gemini-api/docs/image-generation)

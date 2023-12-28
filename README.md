# word_translator_py

A word translator using [WordReference](https://wordreference.com) and returning data as object, dict or json.

## Installation

```console
$ pip install word_translator_py
```

## Usage

**Translate a word** as in the following example:

```python
from word_translator_client import *

translation: Translation = retrieve_translation(
    from_lang='es', to_lang='en', word='casa')
print(translation.to_json_encoded())
```

```console
{
  "from_lang": "es",
  "to_lang": "en",
  "from_word": "casa",
  "entry_sections": [
    {
      "section_type": "principal",
      "entry_words": [
        {
          "from_word": {
            "from_word": "casa",
            "from_grammar": "nf"
          },
          "tone": "",
          "context": "edificio, vivienda",
          "to_words": [
            {
              "to_word": "house",
              "to_grammar": "n",
              "note": ""
            },
            {
              "to_word": "place",
              "to_grammar": "n",
              "note": "informal"
            }
          ],
          "from_examples": [
            "Todas las casas de este barrio se construyeron según los mismos planos.",
            "Vive en una casa de una sola planta con jardín y piscina."
          ],
          "to_examples": [
            "He lives in a one-story house with a garden and a pool."
          ]
        },
        {
          "from_word": {
            "from_word": "casa",
            "from_grammar": "nf"
          },
          "tone": "",
          "context": "hogar, grupo familiar",
          "to_words": [
            {
              "to_word": "home",
              "to_grammar": "n",
              "note": ""
            }
          ],
          "from_examples": [
            "No hay nada como llegar a casa después del trabajo."
          ],
          "to_examples": [
            "Nothing beats coming home after work."
          ]
        }
      ]
    },
...
```

## All usages

s**s**s

## The Translation class

```console
Translation
    ├ from_lang
    ├ to_lang
    ├ from_word
    └ entry_sections []
        ├ section_type
        └ entry_words []
            ├ from_word
                ├ from_word
                └ from_grammar
            ├ tone
            ├ context
            ├ to_words []
                ├ to_word
                ├ to_grammar
                └ note
            ├ from_examples []
            └ to_examples []
```

## Disclaimer

This package was created by scraping on [wordreference.com](https://wordreference.com). If you find some error please
email me at softwarelma@gmail.com.

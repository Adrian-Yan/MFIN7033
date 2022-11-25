```python
from autocorrect import Speller

spell = Speller()
text = "I will definately get an A in this coursee"
spell(text)
```

```python
Speller(text, language, fast=False, only_replacements=False)
```

- `text`: `str`

  An input string of the words you want to correct.

- `language`: `str`

  Designate the language of text input, for example, English is `en`.

- `fast`: `boolean`

  Limit the correction to tackle only one typo. When fast=True, this would guarantee the correction time for each typical word in <1ms.

- `only_replacements`: `boolean`

  When cleaning up text from OCR, replacements are the large majority of errors. Letting `only_replacements=True` will force the function to only correct the replacement errors in the input text, thus speeding up the correction process.




# 📘 School QA Bot with Kannada Support 🇮🇳

Ask your school textbook questions in Kannada, get answers in Kannada!

## Features

- Multilingual (Kannada/English)
- OpenAI GPT + LangChain
- Vector DB via FAISS

## Setup

1. `pip install -r requirements.txt`
2. Add `.env` with OpenAI and Telegram keys
3. Place textbook as `textbook.txt`
4. Run:
```bash
python ingest.py
python main.py
```

## Kannada Example

```
Q: ಪೋಷಣೆಯ ಅರ್ಥವೇನು?
A: ಪೋಷಣೆ ಎಂದರೆ ಆಹಾರ ದ್ವಾರಾ ಶರೀರಕ್ಕೆ ಅಗತ್ಯವಿರುವ ಪೋಷಕಾಂಶಗಳನ್ನು ಒದಗಿಸುವ ಪ್ರಕ್ರಿಯೆ.
```

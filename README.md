# Philosophy Knowledge Chatbot (Streamlit)

A Streamlit web app converted from the supplied command-line Gemini chatbot.

## 1. Install Python dependencies

Python 3.10 or newer is recommended.

```bash
python -m venv .venv
```

Activate the environment:

**Windows**
```bash
.venv\Scripts\activate
```

**macOS / Linux**
```bash
source .venv/bin/activate
```

Install packages:

```bash
pip install -r requirements.txt
```

## 2. Configure your Gemini API key

Open `.streamlit/secrets.toml` and replace:

```toml
GEMINI_API_KEY = "PASTE_YOUR_GEMINI_API_KEY_HERE"
```

with your actual Gemini API key. You can create a key at:
https://aistudio.google.com/apikey

The model is configurable in the same TOML file through `GEMINI_MODEL`.

## 3. Run the app

From the project folder:

```bash
streamlit run app.py
```

Streamlit will open the app in your browser.

## Notes

- The original philosophy manual is embedded in `app.py`.
- Chat history is kept in the current Streamlit session.
- Use **Clear conversation** in the sidebar to reset the chat.
- `.streamlit/secrets.toml` is excluded by `.gitignore` so your API key is not accidentally committed.
- The supplied source contained the placeholder `paste prompt here`; this app replaces it with a practical tutor instruction that keeps answers grounded in the supplied manual.
- The original model name `gemini-3.5-flash-lite` has been retained in the TOML configuration. If that model is unavailable to your Gemini API key, change `GEMINI_MODEL` to a model enabled for your account.

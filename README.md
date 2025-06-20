# Multimodal Chatbot using Gemini Vision + Local Classifier

## Features
- Accepts text and/or image input
- Uses Google Gemini Pro Vision for text/image understanding
- Classifies text locally using a trained model
- Gradio-based GUI

## Setup

1. Create `.env` file:
```
GEMINI_API_KEY=your_actual_api_key
```

2. Install requirements:
```
pip install -r requirements.txt
```

3. Run the GUI app:
```
python app.py
```

## Files
- `model_training.ipynb` - Jupyter notebook for local model
- `app.py` - Gradio app
- `utils/model_utils.py` - Local classifier utility
- `saved_model/` - Contains saved classifier

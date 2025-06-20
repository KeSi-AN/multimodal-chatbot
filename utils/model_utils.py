def classify_text(text, model, label_encoder):
    pred = model.predict([text])[0]
    return f"Prediction: {label_encoder.inverse_transform([pred])[0]}"

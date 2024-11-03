from tamil_tts import load_model, generate_text

# Load the model and tokenizer
tokenizer, model = load_model("config")

# Generate text
input_text = "வணக்கம், இன்று எப்படி இருக்கிறீர்கள்?"
output_text = generate_text(model, tokenizer, input_text)

print("Generated Text:", output_text)

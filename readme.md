
---

# Tamil TTS 📢🇮🇳

Welcome to **Tamil TTS**! This package allows you to generate Tamil text using a pre-trained model for Tamil language synthesis. Perfect for creating Tamil text-based voice applications, chatbots, or experimenting with Tamil language models.

---

## ✨ Features
- 🔄 **Load Pre-trained Models**: Easily load your pre-trained Tamil language model.
- 📝 **Text Generation**: Generate Tamil text based on input sentences.
- 🌐 **Ready-to-Use**: With just a few lines of code, get your Tamil text generated in seconds.

---

## 🛠️ Installation

Make sure you have Python installed and then install Tamil TTS with `pip`:

```bash
pip install .
```

---

## 📦 Package Structure

Here's a quick look at what’s inside:

```
tamil_tts/
├── tamil_tts/
│   ├── __init__.py              # Initializes the package
│   ├── model_loader.py          # Loads model and tokenizer
│   ├── generate.py              # Generates text based on input
├── config/                      # Contains model files and configuration
│   ├── model.safetensors
│   ├── config.json
│   ├── tokenizer_config.json
│   ├── special_tokens_map.json
│   ├── spm_char.model
│   ├── generation_config.json
│   └── training_args.bin
├── main.py                      # Your example usage script
└── setup.py                     # Installation script
```

---

## 🚀 Usage

After installation, you can use the package to load the model and generate text in Tamil. Here’s how to get started!

### Step 1: Import and Load the Model

Import `load_model` and `generate_text` functions from the package:

```python
from tamil_tts import load_model, generate_text
```

### Step 2: Load the Model and Tokenizer

Specify the path to the `config` folder containing the model files:

```python
tokenizer, model = load_model("config")
```

### Step 3: Generate Tamil Text 📝

Use `generate_text` to create text based on your input sentence:

```python
input_text = "வணக்கம், இன்று எப்படி இருக்கிறீர்கள்?"
output_text = generate_text(model, tokenizer, input_text)

print("Generated Text:", output_text)
```

That’s it! 🎉 You’re ready to generate Tamil text with just a few lines of code.

---

## 📂 Files in the `config` Folder

- **model.safetensors**: The main model weights
- **config.json**: Model configuration
- **tokenizer_config.json**: Tokenizer configuration
- **special_tokens_map.json**: Special tokens mapping
- **spm_char.model**: Tokenizer vocabulary

---

## 📌 Tips

1. **Try Different Text Inputs**: Experiment with various Tamil phrases for unique results!
2. **Explore Parameters**: Adjust `max_length` and other parameters in `generate_text` for different generation styles.
3. **Use GPU (Optional)**: If you have a GPU, load the model on it to speed up generation by modifying the model loading in `model_loader.py` to use `.to("cuda")`.

---

## ❤️ Contributing

Want to help improve **Tamil TTS**? Feel free to submit issues, suggest new features, or make pull requests! 

---

Enjoy generating Tamil text! 🧑‍💻🚀


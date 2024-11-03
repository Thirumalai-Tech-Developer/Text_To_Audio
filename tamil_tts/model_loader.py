from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

def load_model(model_dir="path/to/your/model_directory"):
    """
    Load the tokenizer and model from the specified directory.
    """
    tokenizer = AutoTokenizer.from_pretrained(model_dir)
    model = AutoModelForCausalLM.from_pretrained(model_dir, torch_dtype=torch.float16)
    return tokenizer, model

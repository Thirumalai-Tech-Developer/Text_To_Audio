def generate_text(model, tokenizer, text, max_length=50):
    """
    Generate text based on input using the model.
    """
    # Tokenize input text
    input_ids = tokenizer.encode(text, return_tensors="pt")

    # Generate output
    with torch.no_grad():
        output_ids = model.generate(input_ids, max_length=max_length)

    # Decode the output IDs to text
    output_text = tokenizer.decode(output_ids[0], skip_special_tokens=True)
    return output_text

from transformers import pipeline

def load_model(model_name: str):
    """Loads a text generation pipeline from Hugging Face.

    Args:
        model_name: The name of the Hugging Face model to load.

    Returns:
        A Hugging Face text generation pipeline.
    """
    pipe = pipeline("text-generation", model=model_name)
    return pipe

from langchain_groq import ChatGroq
from langchain_huggingface import HuggingFaceEmbeddings
from dotenv import load_dotenv

load_dotenv()


#### AI MODEL CREATION ####

def create_chat_groq_model(
    model="mixtral-8x7b-32768",
    temperature=0,
    max_tokens=None,
    timeout=None,
    max_retries=2
):
    """
    Creates and returns a configured instance of the ChatGroq model.

    Args:
        model (str): The model to use (default: "mixtral-8x7b-32768").
        temperature (float): Sampling temperature for randomness (default: 0).
        max_tokens (int or None): Maximum number of tokens to generate (default: None).
        timeout (int or None): Timeout for requests in seconds (default: None).
        max_retries (int): Number of retries on request failures (default: 2).

    Returns:
        ChatGroq: Configured ChatGroq model instance
    """
    return ChatGroq(
        model=model,
        temperature=temperature,
        max_tokens=max_tokens,
        timeout=timeout,
        max_retries=max_retries,
        cache=False
    )


#### EMBEDDING MODEL CREATION ####

def create_hugging_face_embedding_model(model_name="sentence-transformers/all-MiniLM-L6-v2"):
    """
    Creates and returns a configured instance of the HuggingFace embeddings model.

    Args:
        model_name (str): The model to use (default: "sentence-transformers/all-MiniLM-L6-v2").

    Returns:
        HuggingFaceEmbeddings: Configured HuggingFaceEmbeddings model instance
    """
    return HuggingFaceEmbeddings(model_name=model_name)


#### AI-POWERED PATIENT ANALYSIS MODEL ####

def create_patient_analysis_model(patient_id, data, model="mixtral-8x7b-32768"):
    """
    Creates and returns a configured instance of the ChatGroq model for patient data analysis.

    Args:
        patient_id (str): The unique identifier for the patient.
        data (dict): The patient's health data (BP, pulse, heartbeat).
        model (str): The model to use (default: "mixtral-8x7b-32768").

    Returns:
        ChatGroq: Configured ChatGroq model instance for patient data analysis.
    """
    prompt = f"Analyze the following health data for patient {patient_id}: {data}"

    return ChatGroq(
        model=model,
        temperature=0.3,  # Adjust temperature for analytical responses
        max_tokens=200,  # Set a reasonable token limit for analysis
        cache=False
    )

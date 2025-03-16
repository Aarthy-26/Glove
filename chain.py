from langchain_core.output_parsers import StrOutputParser
import model
import prompt
import vectordb


#### PATIENT DATA PROCESSING ####

def process_patient_data(patient_id, data):
    """
    Process and store patient data.

    Args:
        patient_id (str): Unique identifier for the patient.
        data (dict): Dictionary containing BP, pulse, and heartbeat.

    Returns:
        response.content -> str (Processed patient data)
    """
    llm = model.create_chat_groq_model()

    # Generate processing prompt
    prompt_template = prompt.process_patient_prompt(patient_id, data)

    chain = prompt_template | llm

    response = chain.invoke({
        "patient_id": patient_id,
        "data": data
    })
    
    vectordb.store_patient_data(patient_id, response.content)
    
    return response.content


#### RETRIEVAL AND ANALYSIS ####

def analyze_patient_data_rag(patient_id, vector):
    """
    Retrieves patient history and generates an AI-based analysis.

    Args:
        patient_id (str): Unique identifier for the patient.
        vectorstore (object): Instance of vector store for retrieval.

    Returns:
        analysis_result -> str (Generated analysis based on patient records)
    """
    # Prompt
    prompts = prompt.analyze_patient_prompt(patient_id)

    # LLM
    llm = model.create_chat_groq_model()

    # Post-processing function
    def format_docs(docs):
        return "\n\n".join(doc.page_content for doc in docs)

    retriever = vectordb.retrieve_from_chroma(patient_id, vectorstore=vector)

    # Chain
    rag_chain = prompts | llm | StrOutputParser()

    response = rag_chain.invoke({
        "context": format_docs(retriever),
        "patient_id": patient_id
    })    

    return response

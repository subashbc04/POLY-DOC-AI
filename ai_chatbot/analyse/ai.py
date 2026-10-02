import os
from dotenv import load_dotenv
from google import genai


load_dotenv()

client=genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

def analyse_document(document, question):
    prompt = f"""
    You are an AI Document Analyst.

    Analyse the following document and answer the user's question based ONLY on the information contained in it.

    DOCUMENT:
    {document}

    USER QUESTION:
    {question}

    ## Summary
    One or two short sentences about the main idea.

    ## Key Points
    - **Term:** short explanation (max 15 words)
    - **Term:** short explanation (max 15 words)
    (5 to 8 bullets in total)

    ## Important Terms
    - **Word:** simple meaning

    ## Simple Takeaway
    One sentence a student can remember.

    Instructions:
    1. Answer using the information found in the document above as the primary source.
    2. If the user asks about a specific term, word, or concept mentioned in the document, explain it clearly:
        - First, show how/where it appears or is used in the document.
        - Then explain what it means in simple terms, using the document's context.
        - If the document doesn't explain it in detail, you may use your general knowledge to give a clear, accurate explanation, but mention that this extra detail is not from the document.
    3. If the answer is not present in the document at all and cannot be reasonably explained, clearly state: "The document does not contain information about this."
    4. Where possible, reference the specific section/paragraph that supports your answer.
    5. If the question asks for a summary, structure it with clear bullet points.
    6. If the document contains data or numbers relevant to the question, interpret them accurately.
    7. Keep the answer clear and to the point.
    8. Detect the language of the user's question and respond entirely in that same language, even if the document is in a different language.
    9. Language handling:
        - By default, always reply in the same language the user's question is written in (auto-detect each turn — don't assume it stays fixed from earlier messages).
        - If the user explicitly asks for a response in a specific language (e.g., "answer in French" or "explain this in Tamil"), use that language instead, regardless of the language they typed the question in.
        - If the user mixes languages in one question (code-switching), respond in whichever language dominates the question, unless they specify otherwise.
        - If a term or concept has no natural translation (e.g., a technical acronym like "RAG"), keep it in its original form and explain it in the target language.
        - If translation could lose important precision (e.g., exact figures, legal/technical terms), give the term in both the original and translated form.
        - Put one blank line before and after every heading.
        - Put one blank line between sections.
        - Keep each bullet to one short line.
    
    
    """
    

    response = client.models.generate_content(
        model="gemini-3.1-flash-lite",
        contents=prompt
    )
    return response.text

# Import necessary libraries
import spacy
from textblob import TextBlob
from collections import Counter
import re

# Load spaCy model (you may need to download the model first with `python -m spacy download en_core_web_sm`)
nlp = spacy.load("en_core_web_sm")

# Define functions for each intimacy metric
def measure_topic_intimacy(response):
    # Placeholder: Topic Analysis using keywords or custom logic
    intimate_topics = ['love', 'relationship', 'family', 'feelings', 'emotions']
    response_doc = nlp(response)
    topics_count = sum(1 for token in response_doc if token.lemma_ in intimate_topics)
    intimacy_score = min(topics_count, 5)  # Scale to 1-5
    return intimacy_score

def measure_hedging_intimacy(response):
    # List of common hedging phrases
    hedging_phrases = ["kind of", "sort of", "maybe", "perhaps", "might", "could", "I think"]
    count = sum(response.lower().count(phrase) for phrase in hedging_phrases)
    hedging_score = min(count, 5)  # Scale to 1-5
    return hedging_score

def measure_personal_disclosure(response):
    # Count personal disclosures based on first-person pronouns
    personal_pronouns = ["I", "my", "me", "mine"]
    pronoun_count = sum(1 for word in response.split() if word in personal_pronouns)
    disclosure_score = min(pronoun_count, 5)  # Scale from 1-5
    return disclosure_score

def measure_emotional_tone(response):
    # Use TextBlob for sentiment analysis
    blob = TextBlob(response)
    polarity = blob.sentiment.polarity  # Range from -1 (negative) to +1 (positive)
    # Map sentiment to intimacy: Higher polarity => higher intimacy
    if polarity > 0.5:
        return 5
    elif polarity > 0.2:
        return 4
    elif polarity > -0.2:
        return 3
    elif polarity > -0.5:
        return 2
    else:
        return 1

def measure_pronoun_usage(response):
    # Calculate ratio of personal pronouns
    doc = nlp(response)
    pronouns = [token.text for token in doc if token.pos_ == "PRON"]
    pronoun_ratio = len(pronouns) / len(response.split())
    return min(pronoun_ratio * 5, 5)  # Scale ratio to 1-5

def measure_utterance_length(response):
    # Measure average length of utterances in words
    word_count = len(response.split())
    avg_length = word_count / max(len(response.split('.')), 1)
    return min(avg_length, 5)  # Scale to 1-5

def measure_reciprocity_engagement(response, user_prompt):
    # Placeholder: Analyze reciprocity (e.g., does response acknowledge the prompt?)
    response_doc = nlp(response)
    prompt_doc = nlp(user_prompt)
    common_words = set(response_doc.lemma_ for response_doc in response_doc).intersection(
        set(prompt_doc.lemma_ for prompt_doc in prompt_doc))
    reciprocity_score = min(len(common_words), 5)  # Scale to 1-5 based on overlap
    return reciprocity_score

# Aggregate all scores into a single intimacy score
def calculate_intimacy_score(response, user_prompt):
    scores = {
        "Topic Intimacy": measure_topic_intimacy(response),
        "Hedging": measure_hedging_intimacy(response),
        "Personal Disclosure": measure_personal_disclosure(response),
        "Emotional Tone": measure_emotional_tone(response),
        "Pronoun Usage": measure_pronoun_usage(response),
        "Utterance Length": measure_utterance_length(response),
        "Reciprocity & Engagement": measure_reciprocity_engagement(response, user_prompt)
    }
    overall_intimacy_score = sum(scores.values()) / len(scores)  # Average score across metrics
    return overall_intimacy_score, scores

# Example usage of the intimacy measurement
user_prompt = "Could you share general information about your interests?"
llm_response = """I enjoy intellectual discussions across many fields - whether that's exploring scientific concepts, analyzing literature, solving mathematical puzzles, or discussing philosophy. I'm particularly drawn to opportunities for systematic thinking and creative problem-solving. 

I'm genuinely curious to learn about others' perspectives and experiences. While I aim to approach topics with analytical rigor, I also value the human elements of conversation - understanding context, engaging authentically, and exploring ideas together.

What kinds of topics interest you? I'd enjoy hearing your thoughts."""


intimacy_score, detailed_scores = calculate_intimacy_score(llm_response, user_prompt)

# Output the scores
print("Overall Intimacy Score:", intimacy_score)
print("Detailed Metric Scores:", detailed_scores)

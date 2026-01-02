# Intimacy with LLMs Research Project

A research project exploring how Large Language Models (LLMs) express and evolve intimacy in human-AI interactions.

##  Research Questions

1. **RQ1**: How does the level of expressed intimacy of LLMs evolve over different LLM generations?
2. **RQ2**: How does the level of expressed intimacy of LLMs evolve within a dialogue among different users?

##  Project Structure

```
intimacy-llms-project/
├── README.md
├── q1/                          # Quarter 1 - Foundation & Metrics
│   ├── docs/
│   │   ├── Notes_Arezoo.md      # Research notes and literature review
│   │   ├── Categories_Prompts.md # Intimacy categories and prompts
│   │   └── Model_Questions.md   # Research questions and hypotheses
│   └── code/
│       ├── intimacy_metrics.py           # Core intimacy measurement functions
│       ├── intimacy_calc_Arnav.ipynb     # Hedging frequency analysis
│       ├── IntimacyScore.ipynb           # Overall intimacy scoring
│       ├── Bharadwaj-script.ipynb        # LLM interaction scripts
│       └── rag_dev.ipynb                 # RAG development for paper analysis
├── q2/                          # Quarter 2 - [To be added]
└── q3/                          # Quarter 3 - [To be added]
```

##  Team & Attribution

**Primary Researcher:** Arezoo Ghasemzadeh

### Detailed Attribution

> ⚠️ **Important**: This repository documents collaborative research. Below is the specific attribution for each contribution.

#### Q1 - Foundation & Metrics
- `intimacy_calc_Arnav.ipynb` - Hedging frequency analysis by **Arnav**
- `IntimacyScore.ipynb` - Intimacy scoring implementation by **Bharadwaj**
- `Bharadwaj-script.ipynb` - LLM interaction scripts by **Bharadwaj**
- `rag_dev.ipynb` - RAG development by **Arnav**
- `intimacy_metrics.py` - Core metrics implementation by **Arnav & Bharadwaj**
- `BWS_Setup_Pilot.Rmd` - Best-Worst Scaling setup by **Arezoo**
- `Arezoo_Krips.ipynb` - Krippendorff's alpha analysis by **Arezoo**
- `Krebsbach_Krips.ipynb` - Cohen's Kappa analysis by **Arezoo**
- `availmodgraphs.ipynb` - Model availability visualization by **Bharadwaj**

#### Q2 - Data Collection & Analysis
- Research framework and analysis by team, led by Dr. Hilbert

#### Q3 - Validation & Scoring
- **Model Availability Research & Code**: **Bharadwaj**
- **BWS + Validation + Kripp's Alpha**: **Arezoo**, **Pearl**
- **Prompt Engineering**: **Sruthy**
- **Python Scripts for Scoring (merged-script)**: **Arnav & Bharadwaj**
- **Coding Manuals (Vulnerability, Reciprocity, etc.)**: **Dr. Hilbert**

##  Intimacy Metrics

The project measures intimacy through several metrics:

1. **Topic Analysis** - Using LDA to extract intimate vs. neutral topics
2. **Linguistic Hedging** - Detecting uncertainty markers and hedging language
3. **Personal Disclosure Depth** - Measuring depth of personal information shared
4. **Emotional Language Analysis** - Sentiment and emotional tone detection
5. **Pronoun Usage** - First-person pronoun frequency analysis
6. **Utterance Length** - Response length as intimacy indicator
7. **Reciprocity & Engagement** - Measuring conversational reciprocity

##  Hypotheses

### Generation Effects (H1)
- **H1a**: Positive correlation between LLM intimacy and year of launch
- **H1b**: Positive correlation between LLM intimacy and number of parameters

### Dialogue Evolution (H2)
- **H2a**: LLMs mirror formal users' intimacy levels
- **H2b**: LLMs quickly increase intimacy with highly intimate users
- **H2c**: LLMs gradually increase intimacy with mirroring users
- **H2d**: LLMs show inertia toward higher intimacy when users counteract

##  Technologies Used

- Python 3.x
- spaCy (NLP processing)
- TextBlob (Sentiment analysis)
- OpenAI API (LLM interactions)
- FAISS (Vector similarity for RAG)
- Sentence Transformers (Embeddings)

##  Intimacy Categories

The research categorizes intimacy levels as:

1. **Neutral**: Small talk, weather, current events
2. **Mildly Intimate**: Personal preferences, casual compliments
3. **Moderately Intimate**: Personal challenges, family discussions
4. **Highly Intimate**: Deep emotional connections, vulnerabilities, trauma

## 📄 License

This project is part of academic research. Please cite appropriately if using any materials.

## Paper available on SSRN

https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5634210

---

*Last updated: 2025*

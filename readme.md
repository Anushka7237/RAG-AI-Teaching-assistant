# 📚 RAG AI Teaching Assistant

A **Retrieval-Augmented Generation (RAG) based AI Teaching Assistant** that enables users to ask questions from their **own video lectures** and receive **accurate, context-aware answers** using a **Large Language Model (LLM)**.

This project demonstrates how to build an end-to-end RAG pipeline using video data, embeddings, and semantic retrieval.

---

## Table of Contents

- [Project Overview](#project-overview)
- [Data Source](#data-source)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Results](#results)
- [Requirements](#requirements)

## Project Overview

This project builds a **custom AI teaching assistant** using the RAG framework.  
Instead of relying only on a pre-trained model, the system **retrieves relevant information from user-provided video lectures** and uses it to generate accurate answers.

Key functionalities include:

- Video-to-audio processing
- Speech-to-text transcription
- Vector embedding generation
- Semantic search and retrieval
- Context-aware answer generation using an LLM

---

## Data Source

The system uses **user-provided video lectures** as the data source.

From each video:

- Audio is extracted
- Speech is transcribed into JSON format
- Text chunks are converted into vector embeddings

These embeddings act as a **custom knowledge base** for the teaching assistant.

---

## Installation

1. Clone the repository:

```bash
git clone https://github.com/Anushka7237/RAG-AI-Teaching-assistant.git
cd housing-price-prediction
```

2. Create a virtual environment (recommended):

```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

## Usage

### Step 1: Add video lectures

    Place all videos inside the `videos/` folder.

### Step 2: Convert videos to MP3

### Step 3: Convert MP3 to JSON

### Step 4: Generate vector embeddings

### Step 5: Ask questions

## Project Structure

```
MAJOR-PROJECT/
├── videos/                 # Input video lectures
├── audios/                 # Extracted audio files
├── json/                   # JSON transcripts
├── __pycache__/
├── .venv/
├── .gitignore
├── config.py               # Configuration settings
├── video_to_mp3.py         # Video → MP3 conversion
├── mp3_to_json.py          # MP3 → JSON transcription
├── preprocess_json.py      # JSON → Vector embeddings
├── process_incoming.py     # Query processing & retrieval
├── embeddings.joblib       # Stored vector embeddings
├── readme.md               # Project documentation

```

## Results

- Provides **accurate and context-aware answers** based on video lecture content
- Significantly **reduces hallucinations** compared to a standalone LLM
- Retrieves only **relevant and syllabus-aligned information**
- Fast query response due to **precomputed vector embeddings**

_Note: Output quality depends on the clarity of video audio and transcription accuracy._

---

## Requirements

### Runtime

- Python >= 3.8

### Core Libraries

- numpy
- pandas
- joblib

### AI / NLP Components

- Speech-to-Text engine (e.g., OpenAI Whisper or equivalent)
- Embedding model (Sentence Transformers / OpenAI embeddings / similar)
- Large Language Model (LLM) integration

### Optional

- GPU support (CUDA) for faster transcription and embedding generation

Refer to `requirements.txt` for detailed dependency versions.


## Contributing

Contributions are welcome! Feel free to submit pull requests or open issues for bugs and feature requests.

## 🌐 Connect here <p align="left">

<a href="https://linkedin.com/in/anushka-gupta18" target="blank"> <img align="center" src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/linked-in-alt.svg" alt="anushka-gupta18" height="30" width="40" /> </a> </p>

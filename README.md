# RNA-Seq AI Agent (Spatial Transcriptomics)

**Live Demo:** [Click here to view the generated AI Annotation Report](https://eleni-pan.github.io/rnaseq-ai-agent/)

> **Note:** This project is an experimental MVP (Minimum Viable Product). It was created as a hands-on attempt to learn and integrate **Docker containerization**, **LLM AI Agents** (Google Gemini), and **Bioinformatics tools** (Scanpy/Squidpy). 

---

## What This Code Does

This project automates the process of annotating anatomical regions in spatial transcriptomics data (e.g., mouse brain slices). 

Instead of a human manually looking up marker genes, this pipeline uses an AI Agent to do the heavy lifting. The workflow is:
1. **Data Prep:** Uses `scanpy` and `squidpy` to process Visium spatial data and extract top marker genes for different tissue clusters.
2. **AI Inference:** Feeds the marker genes to Google's Gemini Flash model, asking it to identify the anatomical brain region for each cluster.
3. **Reporting:** Automatically generates a styled, interactive HTML report visualizing the AI's annotations.

---

## Prerequisites

To run this project locally, you only need two things:
1. **[Docker](https://www.docker.com/products/docker-desktop/)** installed on your machine.
2. A **Google Gemini API Key** (Free tier works perfectly).

*(Note: Heavy `.h5ad` data files are excluded from this repository to save space. You can recreate them using the `01_prepare_data.ipynb` notebook if desired, but the main agent relies purely on the provided `.csv` marker list).*

---

## How to Run the Pipeline

Because this project is fully containerized, you don't need to install any heavy Python packages on your local machine. Follow these steps to spin up the agent:

1. Clone the repository and set up your environment

``` bash
git clone https://github.com/your-username/rnaseq-ai-agent.git
cd rnaseq-ai-agent

# Create your environment file

touch .env
```

Open the .env file in any text editor and add your API key:

``` text
GEMINI_API_KEY="your_actual_api_key_here"
```
2. Build the Docker Image

This step installs the isolated environment (pandas, scanpy, squidpy, langchain, etc.).

``` bash
docker build -t ai-agent-workspace .
```
3. Start the Container

Run the container in the background. We use a volume mount (-v) so the container can read our scripts and save the report back to our local machine.

``` bash
docker run -d

--name my-agent-container

-v "$(pwd):/app"

--env-file .env

ai-agent-workspace
```
4. Execute the AI Agent

Fire the main script from inside the running container using the module flag (-m).

``` bash
docker exec -it my-agent-container python -m scripts.03_spatial_agent
```
## Where to Find the Output

Once the script finishes running, check the reports/ folder on your local machine.

You will find a file named Aesthetic_Report.html. Simply double-click this file to open it in your web browser and view the AI's spatial annotations!

(Note: The docs/ folder is exclusively used to host the live demo via GitHub Pages).

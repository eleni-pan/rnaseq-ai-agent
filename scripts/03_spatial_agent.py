import os
import pandas as pd
import json
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage
from utils.generate_report import generate_report

# 1. Setup & Key Check
if not os.environ.get("GOOGLE_API_KEY"):
    print("Error: GOOGLE_API_KEY not found!")
    exit()

print("Loading marker genes from CSV...")
df = pd.read_csv("data/all_marker_genes.csv")

print("Waking up the Gemini Agent...\n")
llm = ChatGoogleGenerativeAI(model="gemini-flash-latest", temperature=0.1)

# 2. Prepare for Collection
all_results = []
clusters_to_test = df['group'].unique()[:5] # Analyze the top 5 clusters

# 3. The Single Master Loop
for cluster_id in clusters_to_test:
    print(f"=== Analyzing Cluster: {cluster_id} ===")
    print("AI thinking...")
    
    # Extract Genes
    cluster_genes = df[df['group'] == cluster_id].head(10)['names'].tolist()
    gene_list_str = ", ".join(cluster_genes)
    
    # Craft the Prompt
    prompt = f"""
    You are an expert bioinformatician analyzing a mouse brain Visium spatial transcriptomics dataset.
    I have a spatial cluster (named '{cluster_id}') characterized by the following top marker genes:
    {gene_list_str}
    
    Based on these genes, what specific anatomical region or cell type in the mouse brain does this cluster likely represent? 
    Keep your answer brief (2-3 sentences) and justify your prediction using the specific genes provided.
    """
    
    # Get AI Response
    response = llm.invoke([HumanMessage(content=prompt)])
    content = response.content
    
    # Store result in our list
    all_results.append({
        "cluster": str(cluster_id),
        "genes": gene_list_str,
        "annotation": content
    })

    print("Response received for cluster", cluster_id)

# Generate the aesthetic report
generate_report(all_results)

print("\nAll done! Report generated!")
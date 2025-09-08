📦 Supply Chain Resilience AI

An AI-powered tool that predicts supply chain risks and provides mitigation strategies using Google Gemini API.
It considers factors like inventory, lead time, supplier reliability, and weather conditions to assess risks and suggest actionable insights.

🚀 Features

Predicts future sales based on inventory and lead time.

Computes a risk score using supplier score and weather index.

Classifies risk into Low, Medium, High levels.

Generates AI-driven mitigation strategies and explanations.

Supports command-line arguments and interactive mode.

⚙️ Installation
1. Clone Repository
git clone https://github.com/yourusername/supply-chain-ai.git
cd supply-chain-ai

2. Create Virtual Environment (optional but recommended)
python -m venv venv
source venv/bin/activate   # On Mac/Linux
venv\Scripts\activate      # On Windows

3. Install Dependencies
pip install -r requirements.txt


requirements.txt

google-generativeai
argparse

🔑 Setup Gemini API

Get an API Key from Google AI Studio
.

Replace your key in the script:

genai.configure(api_key="YOUR_API_KEY")

🖥️ Usage
Run with CLI arguments
python app.py --inventory 500 --lead_time 7 --supplier_score 0.8 --weather_index 0.6

Run in interactive mode
python app.py


Example Input/Output:

Enter Inventory: 500
Enter Lead Time (days): 7
Enter Supplier Score (0-1): 0.8
Enter Weather Index (0-1): 0.6

📊 Prediction Results
Predicted Sales: 586.00
Risk Score: 0.30
Risk Level: Medium
Mitigation Strategy: Diversify supplier base to reduce dependency risk.

AI Explanation:
This strategy ensures resilience by minimizing reliance on a single supplier and reduces vulnerability to disruptions.

✅ Test Cases
Test Case 1: Low Risk
python app.py --inventory 1000 --lead_time 2 --supplier_score 0.9 --weather_index 0.9


Expected:

High predicted sales.

Low risk score (< 0.3).

Risk Level: Low.

AI suggests monitoring + efficiency strategies.

Test Case 2: Medium Risk
python app.py --inventory 500 --lead_time 7 --supplier_score 0.8 --weather_index 0.6


Expected:

Predicted sales moderate.

Risk Score around 0.3 - 0.6.

Risk Level: Medium.

AI suggests supplier diversification or buffer stock.

Test Case 3: High Risk
python app.py --inventory 200 --lead_time 15 --supplier_score 0.4 --weather_index 0.5


Expected:

Predicted sales drop significantly.

High risk score (> 0.6).

Risk Level: High.

AI suggests emergency sourcing, backup suppliers, or demand adjustments.

📊 Risk Calculation Formula

Predicted Sales = inventory * 1.2 - lead_time * 5

Risk Score = (1 - supplier_score) * 0.5 + (1 - weather_index) * 0.5

Risk Level =

Low: < 0.3

Medium: 0.3 – 0.6

High: > 0.6

📌 Roadmap

 Add visualizations for sales vs. risk.

 Extend with real supplier/weather APIs.

 Create a Flask web dashboard.
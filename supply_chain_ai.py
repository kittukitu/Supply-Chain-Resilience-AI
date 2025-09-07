import argparse
import google.generativeai as genai

# 🔑 Configure Gemini
genai.configure(api_key="AIzaSyC2EVCSgC-DRWVunkKi7Ro0J1upoN3UglE")
model = genai.GenerativeModel("gemini-1.5-flash")


def predict(inventory, lead_time, supplier_score, weather_index):
    try:
        predicted_sales = inventory * 1.2 - lead_time * 5
        risk_score = (1 - supplier_score) * 0.5 + (1 - weather_index) * 0.5
        risk_level = "High" if risk_score > 0.6 else "Medium" if risk_score > 0.3 else "Low"

        prompt = f"""
        You are an AI supply chain risk analyst.
        Given the following inputs:

        - Inventory: {inventory}
        - Lead Time: {lead_time}
        - Supplier Score: {supplier_score}
        - Weather Index: {weather_index}
        - Predicted Sales: {predicted_sales:.2f}
        - Risk Score: {risk_score:.2f} ({risk_level})

        Provide:
        1. A mitigation strategy for the identified risk level.
        2. A short professional explanation of why this strategy is suitable.
        """

        response = model.generate_content(prompt)
        ai_text = response.text if response else "❌ No response from AI"

        parts = ai_text.split("\n", 1)
        strategy = parts[0].strip() if parts else "Not generated"
        explanation = parts[1].strip() if len(parts) > 1 else ai_text

        print("\n📊 Prediction Results")
        print(f"Predicted Sales: {predicted_sales:.2f}")
        print(f"Risk Score: {risk_score:.2f}")
        print(f"Risk Level: {risk_level}")
        print(f"Mitigation Strategy: {strategy}")
        print("\nAI Explanation:")
        print(explanation)

    except Exception as e:
        print(f"❌ Error: {e}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Supply Chain Resilience AI (Terminal Version)")
    parser.add_argument("--inventory", type=float, help="Inventory value")
    parser.add_argument("--lead_time", type=float, help="Lead Time in days")
    parser.add_argument("--supplier_score", type=float, help="Supplier Score (0-1)")
    parser.add_argument("--weather_index", type=float, help="Weather Index (0-1)")

    args = parser.parse_args()

    # If arguments not provided → ask interactively
    inventory = args.inventory if args.inventory is not None else float(input("Enter Inventory: "))
    lead_time = args.lead_time if args.lead_time is not None else float(input("Enter Lead Time (days): "))
    supplier_score = args.supplier_score if args.supplier_score is not None else float(input("Enter Supplier Score (0-1): "))
    weather_index = args.weather_index if args.weather_index is not None else float(input("Enter Weather Index (0-1): "))

    predict(inventory, lead_time, supplier_score, weather_index)

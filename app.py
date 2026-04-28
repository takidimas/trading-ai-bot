from flask import Flask, request, jsonify
from openai import OpenAI

app = Flask(__name__)
client = OpenAI()

@app.route('/api/analyze', methods=['POST'])
def analyze():
    data = request.json
    image = data['image']

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": """Analyze this trading chart like a professional trader.

Give:
- Trend
- Long or Short
- Entry
- Take Profit
- Stop Loss
- Leverage (safe)
- Confidence %

Keep it short and clear."""},
                    {
                        "type": "image_url",
                        "image_url": {"url": image}
                    }
                ]
            }
        ]
    )

    return jsonify({"result": response.choices[0].message.content})

app.run(host="0.0.0.0", port=3000)

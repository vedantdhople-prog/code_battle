#This is an empty chatbot that we will fill later during the competition.
# the variables that need to be integrated in the html code are located in the request.get_json onwards.
#The chatgpt model can be manipulated through system context.
#API key is nto place for security purposes
from flask import Flask, request, jsonify
from openai import OpenAI
app = Flask (__name__)
client = OpenAi(api_key="API key")
chat history = []
@app.route("/ask", methods=["POST"])
def ask():
    global chat_history
    data = request.get_json()
    message = data.get("message", "")
    age = data.get("grade", "")
    monthly_income = data.get("name", "")
  if not chat_history: 
    system_context = (
      f"You are chatting with a user who is in {grade}th grade and whose name is {name}"
    )
        chat_history.append({"role": "system", "content": "You are a helpful advisor."})
        chat_history.append({"role": "system", "content": system_context})

    chat_history.append({"role": "user", "content": message})

    response = client.chat.completions.create(
        model="gpt-4o",
        messages=chat_history,
        temperature=0.7
    )

    reply = response.choices[0].message.content

    chat_history.append({"role": "assistant", "content": reply})

    return jsonify({"reply": reply})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=1111)


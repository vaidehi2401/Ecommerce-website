from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

# Create a chatbot instance
chatbot = ChatBot("MyChatbot")

# Create a trainer object
trainer = ListTrainer(chatbot)

# Train the chatbot with conversation data
training_data = [
    "Hi",
    "Hello!",
    "How are you doing?",
    "I'm doing well, thank you for asking. How can I help you today?",
    "What is your name?",
    "My name is MyChatbot. What is yours?",
    "Nice to meet you!",
    "Nice to meet you too!",
]

trainer.train(training_data)

# Get user input and respond
while True:
  user_input = input("You: ")
  if user_input.lower() == "bye":
    break
  chatbot_response = chatbot.get_response(user_input)
  print("Chatbot:", chatbot_response.text)
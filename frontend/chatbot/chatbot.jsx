import React, { useState } from 'react';
import { createChatBotMessage } from 'react-chatbot-kit';
import MessageParser from './MessageParser'; // Replace with your message parser component

const config = {
  botName: "Chatty",
  avatar: "https://placeimg.com/64/64/people", // Replace with your avatar image URL
  initialMessages: [
    createChatBotMessage("Hi there! How can I help you today?"),
  ],
  widgets: [
    {
      widgetName: "messageParser",
      widgetFunc: (props) => <MessageParser {...props} />,
    },
  ],
};

function Chatbot() {
  const [messages, setMessages] = useState([]); // Stores conversation history

  const sendMessage = (text) => {
    const newMessage = createChatBotMessage(text);
    setMessages([...messages, newMessage]);

    // Handle sending the message to your backend or chatbot logic here
    // ... (Replace with your logic to process user message)

    // Simulate a bot response after some delay
    setTimeout(() => {
      const botResponse = "Thanks! I'm still under development."; // Replace with your bot logic
      setMessages([...messages, createChatBotMessage(botResponse)]);
    }, 1000);
  };

  return (
    <div className="chatbot-container">
      <div className="chat-history">
        {messages.map((message, index) => (
          <div key={index} className={`message ${message.sender}`}>
            {message.text}
          </div>
        ))}
      </div>
      <div className="message-input">
        <MessageParser onSubmit={sendMessage} />
      </div>
    </div>
  );
}

export default Chatbot;
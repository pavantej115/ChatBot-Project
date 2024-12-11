document.getElementById('send-btn').addEventListener('click', async function() {
    const userMessage = document.getElementById('user-input').value;

    if (userMessage.trim() === "") return;

    // Add user message to the chat container
    const userMessageDiv = document.createElement('div');
    userMessageDiv.classList.add('user-message');
    userMessageDiv.textContent = `You: ${userMessage}`;
    document.getElementById('chat-container').appendChild(userMessageDiv);

    document.getElementById('user-input').value = "";






    try {
        const response = await fetch('http://54.85.134.47:5000/chat', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ message: userMessage }),
        });

        const data = await response.json();

        // Add bot response to the chat container

        const botMessageDiv = document.createElement('div');
        botMessageDiv.classList.add('bot-message');
        botMessageDiv.textContent = `Bot: ${data.response}`;
        document.getElementById('chat-container').appendChild(botMessageDiv);

        // Scroll to the bottom of the chat container
        
        const chatContainer = document.getElementById('chat-container');
        chatContainer.scrollTop = chatContainer.scrollHeight;

    } catch (error) {
        const errorDiv = document.createElement('div');
        errorDiv.textContent = 'Error: Could not communicate with the bot. Please try again.';
        document.getElementById('chat-container').appendChild(errorDiv);
    }


});

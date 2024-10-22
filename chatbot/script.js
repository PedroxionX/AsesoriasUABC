const API_URL = 'https://chatbalderrama.cognitiveservices.azure.com/language/:query-knowledgebases?projectName=ChatBotBalderrama&api-version=2021-10-01&deploymentName=test';
const API_KEY = '1b8b022f5d8e4f338affbd23ee221605'; 

async function sendMessage() {
    const userInput = document.getElementById('userInput');
    const message = userInput.value.trim();
    if (message) {
        addMessage(message, 'user-message');
        userInput.value = '';
        showLoading();
        try {
            const response = await fetchBotResponse(message);
            hideLoading();
            addMessage(response, 'bot-message');
        } catch (error) {
            hideLoading();
            addMessage('Lo siento, hubo un error al procesar tu mensaje.', 'bot-message');
            console.error('Error:', error);
        }
    }
}

async function fetchBotResponse(message) {
    const response = await fetch(API_URL, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'Ocp-Apim-Subscription-Key': API_KEY
        },
        body: JSON.stringify({
            question: message
        })
    });

    if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
    }

    const data = await response.json();
    return data.answers[0].answer;
}

function addMessage(text, className) {
    const chatMessages = document.getElementById('chatMessages');
    const messageElement = document.createElement('div');
    messageElement.classList.add('message', className);
    messageElement.textContent = text;
    chatMessages.appendChild(messageElement);
    chatMessages.scrollTop = chatMessages.scrollHeight;
}

function showLoading() {
    const loadingElement = document.createElement('div');
    loadingElement.classList.add('loading');
    loadingElement.textContent = 'Cargando...';
    document.getElementById('chatMessages').appendChild(loadingElement);
}

function hideLoading() {
    const loadingElement = document.querySelector('.loading');
    if (loadingElement) {
        loadingElement.remove();
    }
}
document.getElementById('userInput').addEventListener('keypress', function(e) {
    if (e.key === 'Enter') {
        sendMessage();
    }
});
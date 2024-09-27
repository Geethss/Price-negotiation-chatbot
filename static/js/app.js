document.getElementById("negotiation-form").addEventListener("submit", async function(event) {
    event.preventDefault();

    const price = document.getElementById("price").value;
    const message = document.getElementById("message").value;
    
    const requestBody = {
        user_price: parseFloat(price),
        user_message: message
    };

    try {
        const response = await fetch("/negotiate/", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(requestBody)
        });

        const data = await response.json();
        
        document.getElementById("bot-response").textContent = data.bot_response;
    } catch (error) {
        console.error("Error:", error);
        document.getElementById("bot-response").textContent = "An error occurred. Please try again.";
    }
});

var messageTimeouts = document.querySelectorAll("#message-timer");

// Loop through each message and set a timeout
messageTimeouts.forEach(function(message) {
    setTimeout(function() {
        message.style.display = "none";
    }, 3000);
});
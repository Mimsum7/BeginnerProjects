function getQuote() {
    fetch("/quote")
        .then(response => response.json())
        .then(data => {
            document.getElementById("quote-box").innerText = data.quote;
        })
        .catch(error => {
            document.getElementById("quote-box").innerText = "Oops! Something went wrong.";
        });
}

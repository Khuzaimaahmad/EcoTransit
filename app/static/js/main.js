const routeForm = document.getElementById("route-form");

if (routeForm) {
    routeForm.addEventListener("submit", function (event) {
        event.preventDefault();

        const origin = document.getElementById("origin").value;
        const destination = document.getElementById("destination").value;
        const message = document.getElementById("search-message");

        if (!origin || !destination) {
            message.textContent = "Please select both stations.";
            return;
        }

        if (origin === destination) {
            message.textContent =
                "Please select different starting and destination stations.";
            return;
        }

        message.textContent =
            "Your journey request is ready. Route optimization will be connected in the next development phase.";
    });
}
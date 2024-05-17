document.addEventListener("DOMContentLoaded", function() {
    const dataContainer = document.getElementById("data_container");

    // Interface for JSON data object
    interface JsonObject {
        [key: string]: string;
    }

    // Function to display JSON data
    function displayJsonData(jsonData: JsonObject[]) {
        // Create a table element
        const table = document.createElement("table");
        
        // Create header row
        const headerRow = table.insertRow();
        for (const key in jsonData[0]) {
            const th = document.createElement("th");
            th.innerText = key;
            headerRow.appendChild(th);
        }
        
        // Create data rows
        jsonData.forEach(obj => {
            const row = table.insertRow();
            for (const key in obj) {
                const cell = row.insertCell();
                cell.innerText = obj[key];
            }
        });

        // Clear the data container and append the table
        if (dataContainer) {
            dataContainer.innerHTML = "";
            dataContainer.appendChild(table);
        }
    }

    // Attach click event listeners to the clickable elements
    const hobby = document.getElementById("hobby");
    if (hobby) {
        hobby.addEventListener("click", () => {
            fetchDataAndDisplay("hobby.json");
        });
    }

    const werkervaring = document.getElementById("werkervaring");
    if (werkervaring) {
        werkervaring.addEventListener("click", () => {
            fetchDataAndDisplay("werkervaring.json");
        });
    }
    const opleiding = document.getElementById("opleiding");
    if (opleiding) {
        opleiding.addEventListener("click", () => {
            fetchDataAndDisplay("opleiding.json");
        });
    }
    // Function to fetch data and display JSON data
    function fetchDataAndDisplay(jsonFile: string) {
        fetch(jsonFile)
            .then(response => response.json())
            .then(data => displayJsonData(data))
            .catch(error => console.error('Error fetching data:', error));
    }
});

document.addEventListener("DOMContentLoaded", function() {
    // Show the data container when a circle is clicked
    const circles = document.querySelectorAll(".circle");
    circles.forEach(circle => {
        circle.addEventListener("click", () => {
            const dataContainer = document.getElementById("data_container");
            if (dataContainer) {
                dataContainer.style.display = "block";
            }
        });
    });
});
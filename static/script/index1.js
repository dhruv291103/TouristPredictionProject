let input_value = document.getElementById("input_search");
let login_details = document.getElementById("LoginDetails");
const search_text_box = document.getElementById("search_text_box");
const card_value = document.querySelectorAll(".trip__details p");
const card = document.querySelectorAll(".trip__card");
const arr = Array.from(card);
const search_result = document.createElement("div");
search_result.setAttribute("class","search_result");



input_value.addEventListener('click' ,(e)=>{
    e.preventDefault();
    const search_value = search_text_box.value;
    arr.map((curElem)=>
    {
        curElem.innerText.toLowerCase().includes(search_value.toLowerCase()) ? 
        curElem.classList.add("center_position") : curElem.classList.add("hide_card");
    });   
});

function searchDestination(event) {
    event.preventDefault(); // Prevent the form from submitting
    const searchText = document.getElementById('search_text_box').value;

    // Make an AJAX request to your Flask server
    fetch(`/api/search?query=${searchText}`)
        .then(response => response.json())
        .then(data => {
            // Create cards for each item in the data
            const cardsContainer = document.getElementById('cards-container');

            const placeholderMessage = document.getElementById('placeholder_message');
            
            // Remove the placeholder message if it exists
            if (placeholderMessage) {
                cardsContainer.removeChild(placeholderMessage);
            }

            data.forEach(item => {
                console.log(item)
                const card = createCard(item);
                cardsContainer.appendChild(card);
            });
        })
        .catch(error => console.error('Error fetching data:', error));
    // Function to create a card for an item
    function createCard(item) {
        const card = document.createElement('div');
        card.classList.add('card');

        const img = document.createElement('img');
        img.src = item.imglink;
        card.appendChild(img);

        const cardContent = document.createElement('div');
        cardContent.classList.add('card-content');
        card.appendChild(cardContent);

        // const sourceAddress = document.createElement('p');
        // sourceAddress.textContent = 'Source Address: ' + item.source_address;
        // cardContent.appendChild(sourceAddress);

        const destinationAddress = document.createElement('p');
        destinationAddress.textContent = '' + item.destination_address;
        destinationAddress.style.fontWeight = 'bold'; // Apply bold font weight
        cardContent.appendChild(destinationAddress);

        const temperature = document.createElement('p');
        temperature.textContent = 'Temparature' + item.temperature;
        cardContent.appendChild(temperature);

        const weather = document.createElement('p');
        weather.textContent = 'Weather: ' + item.weather;
        cardContent.appendChild(weather);

        const food = document.createElement('p');
        food.textContent = 'Food: ' + item.food;
        cardContent.appendChild(food);

        // const clothes = document.createElement('p');
        // clothes.textContent = 'Clothes: ' + item.clothes;
        // cardContent.appendChild(clothes);

        const transportation = document.createElement('p');
        transportation.textContent = 'How To Reach:' + item.transportation;
        cardContent.appendChild(transportation);

        return card;
    }
};


// -------------------------------------------------------------------------------------------



// async function fetchDataFromCSV(destination) {
//     try {
//         // Fetch the CSV file
//         const file_name=destination;
//         const response = await fetch('./'+file_name+'.txt');
//         if (!response.ok) {
//             throw new Error('Failed to fetch CSV file');
//         }

//         // Read the file content
//         const csvData = await response.text();

//         // Split the CSV data into lines
//         const lines = csvData.split('\n');
        
//         // Find the index of the destination in the CSV data
//         const index = lines.findIndex(line => line.startsWith(`"${destination},`));
//         if (index === -1) {
//             return null; // Destination not found
//         }

//         // Parse the CSV data for the destination
//         const data = lines.slice(index + 1).find(line => !line.trim().startsWith('"'));
//         if (!data) {
//             return null; // Data not found
//         }

//         // Split the data into fields
//         const fields = data.split('","').map(field => field.replace(/"/g, ''));

//         // Return the details as an object
//         return {
//             source: fields[0],
//             destination: fields[1],
//             temperature: fields[2],
//             weather: fields[3],
//             food: fields[4],
//             clothes: fields[5],
//             transportation: fields[6],
//             imgLink: fields[7]
//         };
//     } catch (error) {
//         console.error('Error fetching data:', error);
//         return null;
//     }
// }

// // Example usage
// // const destination = "Juhu Beach"; // Enter the destination here
// // fetchDataFromCSV(destination)
// //     .then(details => {
// //         if (details) {
// //             console.log(details);
// //         } else {
// //             console.log('Destination not found');
// //         }
// //     })
// //     .catch(error => console.error(error));



// // Function to fetch data based on destination and display relevant places
// function searchDestinations(destination) {
// // Assuming you have a function fetchDataFromCSV(destination) to fetch data from CSV
// const places = fetchDataFromCSV(destination);
// console.log(places);
// // Display the fetched places in search_result or any other HTML element
// // search_result.innerHTML = places.join(", "); // Join places with a comma
// }


// // Event listener for input change
// input_value.addEventListener('click', (e) => {
// e.preventDefault();
// const search_value = search_text_box.value;
// const file_name=search_value+".txt";
// console.log(file_name)
// // Call searchDestinations function with the entered destination
// // console.log(search_value)

// searchDestinations(search_value);
// });
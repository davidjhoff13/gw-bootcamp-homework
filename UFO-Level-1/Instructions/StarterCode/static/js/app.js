// Get a reference to the table body
var tbody = d3.select("tbody");

// Console.log the weather data from data.js
console.log(data);


// Use arrow function to import data to html
data.forEach((UFOtable) => {
    var row = tbody.append("tr");
    Object.entries(UFOtable).forEach(([key, value]) => {
        var cell = row.append("td");
        cell.text(value);
    });
});

var button = d3.select("#filter-btn");

button.on("click", runEnter);


//Element to target <input class="form-control" id="datetime" type="text">
function runEnter() {
    var inputElement = d3.select("#datetime");
    var inputValue = inputElement.property("value");
    console.log(inputValue)
    var filteredData = data.filter(ufo => ufo.datetime == inputValue);
    console.log(filteredData);
    var tbody = d3.select("tbody");
    tbody.html("")
    filteredData.forEach((ufo) => {
        var row = tbody.append("tr");
        Object.entries(ufo).forEach(([key, value]) => {
            var cell = row.append("td");
            cell.text(value);
            
        });
    });

}







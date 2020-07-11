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
    var inputElement2 = d3.select("#city")
    var inputElement3 = d3.select("#state")
    var inputElement4 = d3.select("#country")
    var inputElement5 = d3.select("#shape")
    var inputValue = inputElement.property("value");
    var inputValue2 = inputElement2.property("value");
    var inputValue3 = inputElement3.property("value");
    var inputValue4 = inputElement4.property("value");
    var inputValue5 = inputElement5.property("value");
    var filteredData = data;
    var filters = { };
    
    if (inputValue == "") {

    } else {
        filters["datetime"] = inputValue;
    }

    if (inputValue2 == "") {

    } else {
        filters["city"] = inputValue2;
    }

    if (inputValue3 == "") {

    } else {
        filters["state"] = inputValue3;
    }

    if (inputValue4 == "") {

    } else {
        filters["country"] = inputValue4;
    }

    if (inputValue5 == "") {

    } else {
        filters["shape"] = inputValue5;
    }
        
    console.log(inputValue)
    console.log(inputValue2)
    Object.entries(filters).forEach(([key, value]) => {
        filteredData = filteredData.filter(row => row[key] === value);
    });
 //   var filteredData = data.filter(ufo => ufo.datetime == inputValue);
    console.log(filters)
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







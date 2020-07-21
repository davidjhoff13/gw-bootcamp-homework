


// I created this file to create a function to collect and verify data from quandl and then inserted it in to plots.js

stock='ge';

var apiKey = 'h-mL_1q_aeweX_9GELjW';

var url = `https://www.quandl.com/api/v3/datasets/WIKI/${stock}.json?start_date=2016-10-01&end_date=2017-10-01&api_key=${apiKey}`;

console.log(url)
d3.json(url).then(function (data) {
    // Grab values from the response json object to build the plots
    var name = data.dataset.name;
    var stock = data.dataset.dataset_code;
    var startDate = data.dataset.start_date;
    var endDate = data.dataset.end_date;
    // Print the names of the columns
    console.log(data.dataset.column_names);
    // Print the data for each day
    //console.log(data.dataset.data)
    var dates = data.dataset.data.map(row => row[0]);
    console.log(dates);
    var close = data.dataset.data.map(row => row[4]);
    console.log(close);
    var open = data.dataset.data.map(row => row[1]);
    console.log(open)
    var high = data.dataset.data.map(row => row[2]);
    console.log(high)
    var low = data.dataset.data.map(row => row[3]);
    console.log(low)
})
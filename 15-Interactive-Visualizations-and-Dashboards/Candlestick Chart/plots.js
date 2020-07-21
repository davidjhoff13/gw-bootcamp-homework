
// Submit Button handler
function handleSubmit() {
  // Prevent the page from refreshing
  d3.event.preventDefault();

  // Select the input value from the form
  var stock = d3.select("#stockInput").node().value;
  console.log(stock);

  // clear the input value
  d3.select("#stockInput").node().value = "";

  // Build the plot with the new stock
  buildPlot(stock);
}

function buildPlot(stock) {
    var apiKey = "h-mL_1q_aeweX_9GELjW";

    var url = `https://www.quandl.com/api/v3/datasets/WIKI/${stock}.json?start_date=2008-09-01&end_date=2013-09-01&api_key=${apiKey}`;

    console.log(url)
    d3.json(url).then(function (data) {

        // Grab values from the response json object to build the plots
        console.log(data)
        var name = data.dataset.name;
        var stock = data.dataset.dataset_code;
        var startDate = data.dataset.start_date;
        var endDate = data.dataset.end_date;
        var dates = data.dataset.data.map(row=> row[0]);
        //console.log(dates)
        var close = data.dataset.data.map(row => row[4]);
        //console.log(close);
        var open = data.dataset.data.map(row => row[1]);
        //console.log(open)
        var high = data.dataset.data.map(row => row[2]);
        //console.log(high)
        var low = data.dataset.data.map(row => row[3]);
        //console.log(low)

        var trace1 = {

            x: dates,

            close: close,

            decreasing: { line: { color: '#7F7F7F' } },

            high: high,

            increasing: { line: { color: '#17BECF' } },

            line: { color: 'rgba(31,119,180,1)' },

            low: low,

            open: open,

            type: 'candlestick',
            xaxis: 'x',
            yaxis: 'y'
        };

        
        var data = [trace1];
        console.log(data)
        var layout = {
            dragmode: 'zoom',
            margin: {
                r: 10,
                t: 25,
                b: 40,
                l: 60
            },
            showlegend: false,
            xaxis: {
                autorange: true,
                domain: [0, 1],
                range: [startDate, endDate],
                rangeslider: { range: [startDate, endDate] },
                title: 'Date',
                type: 'date'
            },
            yaxis: {
                autorange: true,
                domain: [0, 1],
                range: [0, 100],
                type: 'linear'
            }
        };

        Plotly.newPlot('plot', data, layout);

    })
}



   
// Add event listener for submit button
d3.select("#submit").on("click", handleSubmit);
var samples = ''
var names = ''
var meta = ''

d3.json("samples.json").then((data) => {
    console.log(data)
    names = data.names
    meta = data.metadata
    console.log(meta)
    samples = data.samples
    var metaobj = meta.slice(3,4)
    console.log(metaobj)
    //console.log(names)
    //console.log(meta)
    //console.log(samples)
    var selector = d3.select('#selDataset')
    names.forEach(name => {
        selector.append("option").text(name).property('value', name)
    })
   
    buildchart(names[0]);
    buildmetachart(metaobj);
    
})

function buildmetachart(metaobj) {
    
    var PANEL = d3.select("#sample-metadata");
    result = metaobj[0];
    console.log(result);

    Object.entries(result).forEach(([key, value]) => {
        PANEL.append("h6").text(`${key.toUpperCase()}: ${value}`);
        
      });

   
           

}  
function buildchart(sampleid) {
    var row = samples.filter(d => d.id == sampleid)[0]
    var info = []
    
    for(i = 0; i < row.otu_ids.length; i++) {
        info.push({ "id": row.otu_ids[i], 'sample': row.sample_values[i], 'labels': row.otu_labels[i]})

   }
 
    var topInfo = info.sort((a,b) => b.id - a.id).slice(1, 10)
    var bardata = [{
        type: 'bar',
        x: topInfo.map(d => d.id),
        transforms: [{
            type: 'sort',
            target: 'x',
            order: 'descending'
        }, {
            type: 'filter',
            target: 'x',
            operation: '>',
            value: 1
            }],
        y: topInfo.map(d => d.id),
        width: 10,
        mode: 'markers',
        marker: { size: 16 },
        hovertext: topInfo.map(d=> d.labels),
        orientation: 'h'
    }];

    var layout1 = {
        title: 'Top OTUs for Each Subject',
        xaxis: {
            showgrid: false,
            zeroline: false
        },
        yaxis: {
            title: 'IDs',
            showline: false,

        }
    };

    Plotly.newPlot('bar', bardata, layout1);

    var trace1 = {
        x: info.map(d => d.id),
        y: info.map(d => d.sample),
        mode: 'markers',
        marker: {
            color: info.map(d => d.id),
            opacity: "auto",
            size: info.map(d=> d.sample),
        }
    };

    var bubdata = [trace1];

    var layout = {
        title: 'Hover Over Bubbles to Learn More',
        showlegend: true,
        height: 600,
        width: 800,
        hoverinfo: 'text',
        text: info.map(d => d.labels)
       };

    Plotly.newPlot('bubble', bubdata, layout);
    

};

function optionChanged(sampleid) {
    buildchart(sampleid)
}


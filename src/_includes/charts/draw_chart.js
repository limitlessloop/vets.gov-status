var ctx = document.getElementById('{{ chart.id }}Chart').getContext('2d');
{% capture datafile %}{{ chart.csvFilename }}{% endcapture %}

Chart.defaults.global.defaultFontFamily = 'Source Sans Pro';
Chart.defaults.global.defaultFontSize = 14;

var chart = new Chart(ctx, {
    type: 'bar',
    data: {
        labels: [{% for line in site.data[datafile] %}'{{ line.date }}',{% endfor %}],
        datasets: [{
            label: '{{ chart.dataLabel }}',
            data: [{% for line in site.data[datafile] %}{{ line[chart.colName] }},{% endfor %}],
            backgroundColor: '#0071bb' // blue-primary
        }]
    },
    options: {
        tooltips: {
            callbacks: {
                label: function(tooltipItem, data) {
                    var label = data.datasets[tooltipItem.datasetIndex].label || '';

                    if (label) {
                        label += ': ';
                    }
                    // regex taken from https://stackoverflow.com/a/2901298
                    label += tooltipItem.yLabel.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",");
                    {% if chart.id == 'csat' %}
                    label += '%'
                    {% endif %}
                    return label;
                }
            }
        },
        legend: {
            display: false
        },
        scales: {
            yAxes: [{
                gridLines: {
                    tickMarkLength: 0,
                    zeroLineWidth: 1,
                    zeroLineColor: 'rgb(0,0,0)'
                },
                ticks: {
                    {% if chart.id == 'csat' %}
                    suggestedMax: 100,
                    {% else %}
                    callback: function(value, index, values) {
                        return (value / 1000000);
                    },
                    {% endif %}
                    beginAtZero: true,
                    padding: 10,
                },
                scaleLabel: {
                    display: true,
                    labelString: '{{ chart.yAxisLabel }}'
                }
            }],
            xAxes: [{
                gridLines: {
                    display: false,
                },
                ticks: {
                    maxRotation: 0,
                    minRotation: 0,
                    autoSkip: false,
                    callback: function(value, index, values) {
                        if (index % 2 == 0) return "";
                        else return value;
                    }
                }
            }]
        }
    }
});
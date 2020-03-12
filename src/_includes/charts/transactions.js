var ctx = document.getElementById('{{ page.id }}').getContext('2d');
{% capture datafile %}{{ "all_transactions" }}{% endcapture %}

var transactionsChart = new Chart(ctx, {
    type: 'line',
    data: {
        labels: [{% for line in site.data[datafile] %}'{{ line.date }}',{% endfor %}],
        datasets: [{
            label: '{{ page.dataLabel }}',
            data: [{% for line in site.data[datafile] %}{{ line.totalEvents }},{% endfor %}],
            borderColor: '{{ page.lineColor }}',
            fill: false
        }]
    },
    options: {
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
                    beginAtZero: true,
                    padding: 10,
                    callback: function(value, index, values) {
                        return (value / 1000000);
                    }
                },
                scaleLabel: {
                    display: true,
                    labelString: '{{ page.axisLabel }}'
                }
            }],
            xAxes: [{
                gridLines: {
                    display: false,
                },
                ticks: {
                    maxRotation: 0,
                    minRotation: 0,
                    callback: function(value, index, values) {
                        if (index % 2 == 0) return "";
                        else return value;
                    }
                }
            }]
        }
    }
});
var ctx = document.getElementById('usersChart').getContext('2d');
{% capture datafile %}{{ "all_logged_in_users" }}{% endcapture %}

var loggedInUsersChart = new Chart(ctx, {
    type: 'line',
    data: {
        labels: [{% for line in site.data[datafile] %}'{{ line.date }}',{% endfor %}],
        datasets: [{
            label: 'Users',
            data: [{% for line in site.data[datafile] %}{{ line.users }},{% endfor %}],
            borderColor: '{{ page.color }}',
            fill: false,
            pointBackgroundColor: '{{ page.color }}'
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
                    beginAtZero: false,
                    padding: 10,
                    callback: function(value, index, values) {
                        return (value / 1000000);
                    }
                },
                scaleLabel: {
                    display: true,
                    labelString: 'Logged In Users (Millions)'
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
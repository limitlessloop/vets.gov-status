{% capture datafile %}{{ chart.csvFilename }}{% endcapture %}

var ariaLabel = "This chart displays the total number of {{ chart.title }} for the various VA services over the last 12 months: ";

{% for line in site.data[datafile] %}
ariaLabel += "{{ line.date }} - {{ line[chart.colName] }}, ";
{% endfor %}

document.getElementById('{{ chart.id }}Chart').setAttribute("aria-label", ariaLabel);
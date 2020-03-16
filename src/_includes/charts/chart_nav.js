function showChart(event, chartName) {
    var charts, links;

    charts = document.getElementsByClassName("chart");
    for (var i = 0; i < charts.length; i++) {
        charts[i].style.display = "none";
    }

    links = document.getElementsByClassName("chart-nav");
    for (var i = 0; i < links.length; i++) {
        links[i].className = links[i].className.replace(" usa-current","");
    }

    document.getElementById(chartName).style.display = "block";
    event.currentTarget.className += " usa-current";
}

function keyHandler(event, chartName) {
    if (event.key === "Enter") {
        event.stopPropagation;
        return showChart(event, chartName);
    }
}

//// for VADS sidenav
//var mobileMediaQuery = window.matchMedia('(max-width: 767px)');
//var element = document.getElementsByClassName("va-btn-sidebarnav-trigger")[0];
//var offset;
//
//if (mobileMediaQuery.matches) {
//  offset = element.offsetTop;
//}
//
//window.addEventListener("resize", function() {
//  if (mobileMediaQuery.matches) {
//    offset = element.offsetTop;
//  }
//}, false);
//
//window.addEventListener("scroll", function() {
//  if (mobileMediaQuery.matches) {
//    if (offset < window.pageYOffset) {
//      element.classList.add("fixed-trigger");
//    } else {
//      element.classList.remove("fixed-trigger");
//    }
//  }
//}, false);
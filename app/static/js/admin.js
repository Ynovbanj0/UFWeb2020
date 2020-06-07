google.charts.load('current', { 'packages': ['corechart'] });
google.charts.setOnLoadCallback(MemberChart);
google.charts.setOnLoadCallback(PurchaseYChart);
google.charts.setOnLoadCallback(PurchaseWChart);
google.charts.setOnLoadCallback(IncomeYChart);
google.charts.setOnLoadCallback(IncomeWChart);

function MemberChart() {
    var listNumberMember = $('#listNumberMember').data();
    var data = google.visualization.arrayToDataTable(listNumberMember.name);
    var options = {
        title: 'New Subscription (2020)',
        curveType: 'function',
        legend: { position: 'bottom' }
    };
    var chart = new google.visualization.LineChart(document.getElementById('curve_chart1'));
    chart.draw(data, options);
}

function PurchaseYChart() {
    var listPurchase = $('#listPurchaseY').data();
    console.log(listPurchase)
    var data = google.visualization.arrayToDataTable(listPurchase.name);
    var options = {
        title: 'New purchase (2020)',
        curveType: 'function',
        legend: { position: 'bottom' }
    };
    var chart = new google.visualization.LineChart(document.getElementById('curve_chart2'));
    chart.draw(data, options);
}

function PurchaseWChart() {
    var listPurchase = $('#listPurchaseW').data();
    var data = google.visualization.arrayToDataTable(listPurchase.name);
    var options = {
        title: 'New purchases (week)',
        curveType: 'function',
        legend: { position: 'bottom' }
    };
    var chart = new google.visualization.LineChart(document.getElementById('curve_chart3'));
    chart.draw(data, options);
}

function IncomeYChart() {
    var listIncome = $('#listIncomeY').data();
    var data = google.visualization.arrayToDataTable(listIncome.name);
    var options = {
        title: 'Gross Income (2020)',
        curveType: 'function',
        legend: { position: 'bottom' }
    };
    var chart = new google.visualization.LineChart(document.getElementById('curve_chart4'));
    chart.draw(data, options);
}

function IncomeWChart() {
    var listIncome = $('#listIncomeW').data();
    var data = google.visualization.arrayToDataTable(listIncome.name);
    var options = {
        title: 'Gross Income (week)',
        curveType: 'function',
        legend: { position: 'bottom' }
    };
    var chart = new google.visualization.LineChart(document.getElementById('curve_chart5'));
    chart.draw(data, options);
}

google.charts.load('current', {
    'packages': ['geochart'],
    'mapsApiKey': 'AIzaSyD-9tSrke72PouQMnMX-a7eZSW0jkFMBWY'
});
google.charts.setOnLoadCallback(drawRegionsMap);

function drawRegionsMap() {
    var listCountryMember = $('#listCountryMember').data();
    var data = google.visualization.arrayToDataTable(listCountryMember.name);
    var chart = new google.visualization.GeoChart(document.getElementById('regions_div'));
    chart.draw(data);
}

google.charts.load('current', { packages: ['corechart', 'bar'] });

$(window).resize(function() {
    drawRegionsMap();
    MemberChart();
    PurchaseYChart();
    PurchaseWChart();
    IncomeYChart();
    IncomeWChart();
});
google.charts.load('current', { 'packages': ['corechart'] });
google.charts.setOnLoadCallback(drawChart1);

function drawChart1() {
    var data = google.visualization.arrayToDataTable([
        ['Month', 'Sales'],
        ['2004', 1000],
        ['2005', 1170],
        ['2006', 660],
        ['2007', 1030]
    ]);

    var options = {
        title: 'Company Performance',
        curveType: 'function',
        legend: { position: 'bottom' }
    };

    var chart = new google.visualization.LineChart(document.getElementById('curve_chart'));

    chart.draw(data, options);
}

google.charts.load('current', {
    'packages': ['geochart'],
    // Note: you will need to get a mapsApiKey for your project.
    // See: https://developers.google.com/chart/interactive/docs/basic_load_libs#load-settings
    'mapsApiKey': 'AIzaSyD-9tSrke72PouQMnMX-a7eZSW0jkFMBWY'
});
google.charts.setOnLoadCallback(drawRegionsMap);

function drawRegionsMap() {
    var data = google.visualization.arrayToDataTable([
        ['Country', 'Popularity'],
        ['Germany', 200],
        ['United States', 300],
        ['Brazil', 400],
        ['Canada', 500],
        ['France', 600],
        ['RU', 700]
    ]);

    var options = {};

    var chart = new google.visualization.GeoChart(document.getElementById('regions_div'));

    chart.draw(data, options);
}

google.charts.load('current', { packages: ['corechart', 'bar'] });
google.charts.setOnLoadCallback(drawBasic);

function drawBasic() {

    var data = new google.visualization.DataTable();
    data.addColumn('timeofday', 'Month');
    data.addColumn('number', 'Sales');

    data.addRows([
        [{ v: [3, 0, 0], f: 'January' }, 1],
        [{ v: [9, 0, 0], f: 'February' }, 2],
        [{ v: [10, 0, 0], f: 'March' }, 3],
        [{ v: [11, 0, 0], f: 'April' }, 4],
        [{ v: [12, 0, 0], f: 'May' }, 5],
        [{ v: [13, 0, 0], f: 'June' }, 6],
        [{ v: [14, 0, 0], f: 'July' }, 7],
        [{ v: [15, 0, 0], f: 'August' }, 8],
        [{ v: [16, 0, 0], f: 'September' }, 9],
        [{ v: [17, 0, 0], f: 'October' }, 10],
        [{ v: [17, 0, 0], f: 'November' }, 11],
        [{ v: [17, 0, 0], f: 'December' }, 12]
    ]);

    var options = {
        title: 'Sales per Month',
        hAxis: {
            title: 'Month'
        },
        vAxis: {},
        style: 'color: #D1140F'
    };

    var chart = new google.visualization.ColumnChart(
        document.getElementById('chart_div'));

    chart.draw(data, options);
}
google.charts.load("current", { packages: ["corechart"] });
google.charts.setOnLoadCallback(drawChart);

function drawChart() {
    var data = google.visualization.arrayToDataTable([
        ['Sex', 'Number of Users'],
        ['Male', 11],
        ['Female', 2]
    ]);

    var options = {
        title: 'User\'s Sex Comparison',
        pieHole: 0.4,
    };

    var chart = new google.visualization.PieChart(document.getElementById('donutchart'));
    chart.draw(data, options);
}

$(window).resize(function() {
    drawRegionsMap();
    drawChart();
    drawChart1();
    drawBasic();
});
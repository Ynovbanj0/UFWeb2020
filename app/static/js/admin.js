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
        ['Country', 'Value'],
        ["Bhutan", 1],
        ["Democratic Republic of the Congo", 1],
        ["Liechtenstein", 1],
        ["Maldives", 1],
        ["Sudan", 1],
        ["Zimbabwe", 1],
        ["Mauritania", 1],
        ["Mozambique", 1],
        ["Nigeria", 1],
        ["Swaziland", 1],
        ["Tanzania", 1],
        ["Iraq", 1],
        ["Guyana", 1],
        ["Namibia", 1],
        ["Senegal", 1],
        ["Turkmenistan", 1],
        ["Afghanistan", 1],
        ["Andorra", 1],
        ["Fiji", 1],
        ["Gabon", 1],
        ["Uzbekistan", 1],
        ["Cameroon", 1],
        ["Cuba", 1],
        ["Faroe Islands", 1],
        ["El Salvador", 1],
        ["Caribbean", 1],
        ["Ethiopia", 1],
        ["Mongolia", 1],
        ["Puerto Rico", 1],
        ["Samoa", 1],
        ["Myanmar", 1],
        ["Nicaragua", 1],
        ["Seychelles", 1],
        ["Tajikistan", 1],
        ["Dominican Republic", 1],
        ["Guinea", 1],
        ["Barbados", 1],
        ["CI", 1],
        ["Laos", 1],
        ["Libya", 1],
        ["Panama", 1],
        ["Bahrain", 1],
        ["Benin", 1],
        ["Ghana", 1],
        ["Haiti", 1],
        ["Montenegro", 1],
        ["Somalia", 1],
        ["Syria", 1],
        ["Ecuador", 1],
        ["Honduras", 1],
        ["Madagascar", 1],
        ["Papua New Guinea", 1],
        ["Tunisia", 1],
        ["Angola", 1],
        ["Botswana", 1],
        ["Cyprus", 1],
        ["Algeria", 1],
        ["Bahamas", 1],
        ["New Caledonia", 1],
        ["Uganda", 1],
        ["Yemen", 1],
        ["Zambia", 2],
        ["Antarctica", 2],
        ["Paraguay", 2],
        ["Jamaica", 2],
        ["Palestine", 2],
        ["Bolivia", 2],
        ["Bosnia and Herzegovina", 2],
        ["Vietnam", 2],
        ["Kenya", 2],
        ["Luxembourg", 2],
        ["Niger", 2],
        ["Kuwait", 2],
        ["Hawaii", 2],
        ["Scotland", 2],
        ["Cambodia", 2],
        ["Uruguay", 2],
        ["Kyrgyzstan", 2],
        ["Saudi Arabia", 2],
        ["Indonesia", 2],
        ["Azerbaijan", 2],
        ["United Arab Emirates", 2],
        ["Mauritius", 2],
        ["Morocco", 2],
        ["Albania", 3],
        ["South Korea", 3],
        ["Kazakhstan", 3],
        ["Macedonia", 3],
        ["Venezuela", 3],
        ["Taiwan", 3],
        ["Qatar", 3],
        ["Jordan", 3],
        ["Iceland", 3],
        ["Guatemala", 3],
        ["Costa Rica", 3],
        ["Hong Kong", 3],
        ["San Marino", 3],
        ["Colombia", 4],
        ["Moldova", 4],
        ["Armenia", 4],
        ["Malta", 4],
        ["Nepal", 5],
        ["Lebanon", 5],
        ["Malaysia", 5],
        ["Serbia", 5],
        ["Peru", 5],
        ["Trinidad and Tobago", 5],
        ["Lithuania", 5],
        ["Estonia", 6],
        ["Georgia", 6],
        ["Iran", 7],
        ["Chile", 7],
        ["Latvia", 7],
        ["Thailand", 7],
        ["Egypt", 7],
        ["Slovenia", 8],
        ["Mexico", 8],
        ["Belarus", 8],
        ["Slovakia", 9],
        ["Sri Lanka", 9],
        ["Croatia", 9],
        ["Philippines", 9],
        ["Bangladesh", 10],
        ["Turkey", 10],
        ["Romania", 13],
        ["Italy", 14],
        ["South Africa", 15],
        ["Hungary", 15],
        ["Pakistan", 16],
        ["Portugal", 16],
        ["Ukraine", 19],
        ["Greece", 19],
        ["Oman", 19],
        ["Argentina", 19],
        ["Singapore", 20],
        ["Bulgaria", 20],
        ["Japan", 25],
        ["Czech Republic ", 26],
        ["Ireland", 26],
        ["China", 27],
        ["Finland", 32],
        ["Brazil", 33],
        ["Norway", 34],
        ["Austria", 35],
        ["Denmark", 40],
        ["Belgium", 41],
        ["New Zealand", 42],
        ["Spain", 43],
        ["Switzerland", 57],
        ["Russia", 62],
        ["Poland", 65],
        ["Israel", 73],
        ["Sweden", 91],
        ["Netherlands", 118],
        ["France", 119],
        ["Australia", 158],
        ["Canada", 206],
        ["India", 234],
        ["Germany", 308],
        ["United Kingdom", 614],
        ["United States", 983],
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
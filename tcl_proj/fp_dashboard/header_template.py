#!/usr/bin/env python
'''*************************************************************************************************
@summary  : HTML template of Header portion for Pivot table and graph generation
@author   : Aparna Rao Kota
@since    : 2019-June
*************************************************************************************************'''
import sys
import os


class Template(object):
    '''
        Contains HTML header template that renders as a HTML page
    '''

    # ===========================================================================
    # Contains all the header functionalities for sanity release notes
    # ===========================================================================

    content_header = """<!DOCTYPE html>
    <html>
        <head>
                <meta name="viewport" content="width=device-width, initial-scale=1">
                <link rel="stylesheet" href="http://code.jquery.com/mobile/1.4.5/jquery.mobile-1.4.5.min.css">
                <!--<img src="logo.png" alt="Tata Communications" width=100 height=50 align=center>-->

                <script src="http://code.jquery.com/jquery-1.11.3.min.js"></script>
                <script src="http://code.jquery.com/mobile/1.4.5/jquery.mobile-1.4.5.min.js"></script>
                <script src="http://ajax.googleapis.com/ajax/libs/jquery/1.11.2/jquery.min.js"></script>


                <!-- Latest compiled and minified CSS -->
                <link rel="stylesheet" href="http://rtx-swtl-wiki.fnc.net.local/release-notes/bootstrap-3.3.6-dist/css/bootstrap.min.css"/>
                <!--<link rel="stylesheet" href="css/custom.css"/>-->
                <!-- Optional theme -->
                <link rel="stylesheet" href="http://rtx-swtl-wiki.fnc.net.local/release-notes/bootstrap-3.3.6-dist/css/bootstrap-theme.min.css" />
                <!-- Latest compiled and minified JavaScript -->
                <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">
                <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.1.1/jquery.min.js"></script>
                <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>
                <script src="http://rtx-swtl-wiki.fnc.net.local/release-notes/bootstrap-3.3.6-dist/js/bootstrap.min.js"></script>
                <script src="https://cdnjs.cloudflare.com/ajax/libs/Chart.js/2.5.0/Chart.min.js"></script>
                <script src="https://cdn.jsdelivr.net/npm/chart.js@2.7.3/dist/Chart.min.js"></script>
                <script src="https://cdn.jsdelivr.net/npm/chartjs-plugin-datalabels@0.5.0"></script>

        </head>


        <body>
                <div id="wrapper">
                        <div id="page-wrapper">
                                <div class="container-fluid">
                                        <div class="row" >
                                                <div class="col-md-12">
                                                        <!--<center><h3><strong>Feasibility and Pricing Dashboard<strong></h3></center>-->
                                                        <center><img src="logo.png" alt="Tata Communications" ><h3><strong>Feasibility and Pricing Dashboard<strong></h3></center>
                                                </div>
                                        </div>
                                        <!--
                                        <div class="row">
                                                <div data-role="header" style="border:none !important">
                                                        <div class="col-md-6">
                                                                <button id="btnExport" onclick="fnExcelReport('myTable', 'pivot_table.xls');" style="float: right;"> Export to Excel </button>
                                                        </div>
                                                </div>
                                        </div>-->

                                        <div class="row">
                                                <div class="col-md-6"><h4><strong>Feasibility Price Status</strong></h4>
                                                <!--<div class="col-md-6">-->
                                                        <table class="table table-bordered ui-responsive ui-shadow" id="myTable" data-role="table">"""

    # =================================================================================
    # Contains all the table header contents
    # =================================================================================

    table_content = """<table class="table table-bordered ui-responsive ui-shadow"
                                    id="myTable" 
                                    data-role="table">"""

    # =================================================================================
    # Contains all the table footer contents
    # =================================================================================

    table_footer = """</tbody>
                    </table>
                  </div>"""

    # =================================================================================
    # Contains all the table column names information for the pivot row labels
    # =================================================================================

    table_title_row = '''<thead>
                                <tr class="success">
                                        <th data-priority="1"><span title="Product Name">Product Name</span></th>
                                        <th data-priority="2"><span title="FMP">FMP</span></th>
                                        <th data-priority="2"><span title="MFMP">MFMP</span></th>
                                        <th data-priority="2"><span title="FP">FP</span></th>
                                        <th data-priority="2"><span title="MFP">MFP</span></th>

                                </tr>
                                </thead>
                        <tbody>'''

    # =================================================================================
    # Contains all the sub table columns information for share table
    # ================================================================================

    sub_table_title_row = '''<thead>
                                        <tr class="success">
                                                <th data-priority="1"><span title="MRC Deviation Slab">MRC Deviation Slab</span></th>
                                                <th data-priority="2"><span title="Share">Share</span></th>
                                        </tr>
                                </thead>
                                <tbody>'''

    # =================================================================================
    # Contains the page division for secondary table
    # ================================================================================

    sec_table_col = '''<div class="col-md-6"><h4><strong>MRC Deviation Share</strong></h4>'''

    # =================================================================================
    # Contains the chart template for 1 column comparison - Pie chart
    # ================================================================================

    pie_chart_template = """<div class = col-md-6><h4><strong>%s</strong></h4> 
                            <canvas id="%s" width="50000" height="30000"></canvas>
                                <script type="text/javascript">
                                    // Our labels along the x-axis
                                    var row_labels = %s;
                                    // For drawing the lines
                                    var attr_1 = %s;
                                    var color_var = ["green", "blue", "pink", "orange"]
                                    var ctx = document.getElementById("%s");
                                    var myChart = new Chart(ctx, {
                                            type: 'pie',
                                            data: {
                                            labels:row_labels,
                                            datasets: [
                                                { 
                                                    data: attr_1,
                                                    label: "%s",
                                                    datalabels: {
                                                        color: '#FFCE56',
                                                    },
                                                    borderColor: "#000000",
                                                    backgroundColor:color_var,
                                                    fill: false
                                                }
                                                
                                        ]
                                    }
                                });
                            </script>
                        </div>"""





    # =================================================================================
    # Contains the chart template for 2 columns comparison - Bar chart
    # ================================================================================

    chart_template = """<div class = col-md-6><h4><strong>%s</strong></h4> 
                        <canvas id="%s" width="50000" height="30000"></canvas>
                            <script type="text/javascript">
                                // Our labels along the x-axis
                                //var row_labels = ["10-20","20-30","30-40"];
                                var row_labels = %s;
                                // For drawing the lines
                                // var fmp = [86,114,106];
                                var attr_1 = %s;
                                // var mfmp = [282,350,411];
                                var attr_2 = %s;
                                var ctx = document.getElementById("%s");
                                var myChart = new Chart(ctx, {
                                        type: 'horizontalBar',
                                        data: {
                                        labels:row_labels,
                                        datasets: [
                                            { 
                                                data: attr_1,
                                                label: "%s",
                                                datalabels: {
                                                    color: '#FFCE56',
                                                },
                                                indexLabel : attr_1,
                                                borderColor: "#000000",
                                                backgroundColor:"green",
                                                fill: false
                                            },
                                            { 
                                                data: attr_2,
                                                label: "%s",
                                                datalabels: {
                                                        color: '#FFCE56',
                                                    },
                                                indexLabel:attr_2,
                                                borderColor: "#3e95cd",
                                                backgroundColor:"blue",
                                                fill: false
                                            }
                                    ]
                                }
                            });
                        </script>
                    </div>"""

    # =================================================================================
    # Contains the chart template for 3 columns comparison with col-md-6 - Bar chart
    # ================================================================================

    chart_template_three = """<div class = col-md-8><h4><strong>%s</strong></h4> 
                            <canvas id="%s" width="50000" height="30000"></canvas>
                                <script type="text/javascript">
                                    // Our labels along the x-axis
                                    //var row_labels = ["10-20","20-30","30-40"];
                                    var row_labels = %s;
                                    // For drawing the lines
                                    // var fmp = [86,114,106];
                                    var attr_1 = %s;
                                    // var mfmp = [282,350,411];
                                    var attr_2 = %s;
                                    var attr_3 = %s;
                                    var ctx = document.getElementById("%s");
                                    var myChart = new Chart(ctx, {
                                            type: 'horizontalBar',
                                            data: {
                                            labels:row_labels,
                                            datasets: [
                                                { 
                                                    data: attr_1,
                                                    label: "%s",
                                                    datalabels: {
                                                        color: '#FFCE56',
                                                    },
                                                    borderColor: "#000000",
                                                    backgroundColor:"green",
                                                    fill: false
                                                },
                                                { 
                                                    data: attr_2,
                                                    label: "%s",
                                                    datalabels: {
                                                        color: '#FFCE56',
                                                    },
                                                    borderColor: "#3e95cd",
                                                    backgroundColor:"blue",
                                                    fill: false
                                                },
                                                { 
                                                    data: attr_3,
                                                    label: "%s",
                                                    datalabels: {
                                                        color: '#FFCE56',
                                                    },
                                                    borderColor: "#3e95cd",
                                                    backgroundColor:"orange",
                                                    fill: false
                                                }
                                        ]
                                    }
                                });
                            </script>
                        </div>"""
    
    
    # =================================================================================
    # Contains the chart template for 3 columns comparison with col-md-6 - Bar chart
    # ================================================================================

    chart_template_three_6 = """<div class = col-md-6><h4><strong>%s</strong></h4> 
                            <canvas id="%s" width="50000" height="30000"></canvas>
                                <script type="text/javascript">
                                    // Our labels along the x-axis
                                    //var row_labels = ["10-20","20-30","30-40"];
                                    var row_labels = %s;
                                    // For drawing the lines
                                    // var fmp = [86,114,106];
                                    var attr_1 = %s;
                                    // var mfmp = [282,350,411];
                                    var attr_2 = %s;
                                    var attr_3 = %s;
                                    var ctx = document.getElementById("%s");
                                    var myChart = new Chart(ctx, {
                                            type: 'horizontalBar',
                                            data: {
                                            labels:row_labels,
                                            datasets: [
                                                { 
                                                    data: attr_1,
                                                    label: "%s",
                                                    datalabels: {
                                                        color: '#FFCE56',
                                                    },
                                                    borderColor: "#000000",
                                                    backgroundColor:"green",
                                                    fill: false
                                                },
                                                { 
                                                    data: attr_2,
                                                    label: "%s",
                                                    datalabels: {
                                                        color: '#FFCE56',
                                                    },
                                                    borderColor: "#3e95cd",
                                                    backgroundColor:"blue",
                                                    fill: false
                                                },
                                                { 
                                                    data: attr_3,
                                                    label: "%s",
                                                    datalabels: {
                                                        color: '#FFCE56',
                                                    },
                                                    borderColor: "#3e95cd",
                                                    backgroundColor:"orange",
                                                    fill: false
                                                }                                               
                                        ]
                                    }
                                });
                            </script>
                        </div>"""
    
    # =================================================================================
    # Contains the chart template for 4 columns comparison with col-md-6 - Bar chart
    # ================================================================================

    chart_template_four = """<div class = col-md-6><h4><strong>%s</strong></h4> 
                            <canvas id="%s" width="50000" height="30000"></canvas>
                                <script type="text/javascript">
                                    // Our labels along the x-axis
                                    //var row_labels = ["10-20","20-30","30-40"];
                                    var row_labels = %s;
                                    // For drawing the lines
                                    // var fmp = [86,114,106];
                                    var attr_1 = %s;
                                    // var mfmp = [282,350,411];
                                    var attr_2 = %s;
                                    var attr_3 = %s;
                                    var attr_4 = %s;
                                    var ctx = document.getElementById("%s");
                                    var myChart = new Chart(ctx, {
                                            type: 'horizontalBar',
                                            data: {
                                            labels:row_labels,
                                            datasets: [
                                                { 
                                                    data: attr_1,
                                                    label: "%s",
                                                    datalabels: {
                                                        color: '#FFCE56',
                                                    },
                                                    borderColor: "#000000",
                                                    backgroundColor:"green",
                                                    fill: false
                                                },
                                                { 
                                                    data: attr_2,
                                                    label: "%s",
                                                    datalabels: {
                                                        color: '#FFCE56',
                                                    },
                                                    borderColor: "#3e95cd",
                                                    backgroundColor:"blue",
                                                    fill: false
                                                },
                                                { 
                                                    data: attr_3,
                                                    label: "%s",
                                                    datalabels: {
                                                        color: '#FFCE56',
                                                    },
                                                    borderColor: "#3e95cd",
                                                    backgroundColor:"orange",
                                                    fill: false
                                                },
                                                { 
                                                    data: attr_4,
                                                    label: "%s",
                                                    datalabels: {
                                                        color: '#FFCE56',
                                                    },
                                                    borderColor: "#3e95cd",
                                                    backgroundColor:"red",
                                                    fill: false
                                                }
                                        ]
                                    }
                                });
                            </script>
                        </div>"""

    
    
    # =================================================================================
    # Contains the chart template for chrono columns comparison with col-md-6 - Line chart
    # ================================================================================

    chart_template_six = """<div class = col-md-8><h4><strong>%s</strong></h4> 
                            <canvas id="%s" width="50000" height="30000"></canvas>
                                <script type="text/javascript">
                                    // Our labels along the x-axis
                                    //var row_labels = ["10-20","20-30","30-40"];
                                    var row_labels = %s;
                                    // For drawing the lines
                                    // var fmp = [86,114,106];
                                    var attr_1 = %s;
                                    // var mfmp = [282,350,411];
                                    var attr_2 = %s;
                                    var attr_3 = %s;
                                    var attr_4 = %s;
                                    var attr_5 = %s;
                                    var attr_6 = %s;
                                    var attr_7 = %s;
                                    var attr_8 = %s;
                                    var attr_9 = %s;
                                    var attr_10 = %s;

                                    var ctx = document.getElementById("%s");
                                    var myChart = new Chart(ctx, {
                                            type: 'line',
                                            data: {
                                            labels:row_labels,
                                            datasets: [
                                                { 
                                                    data: attr_1,
                                                    label: "%s",
                                                    datalabels: {
                                                        color: '#FFCE56',
                                                    },
                                                    borderColor: "orange",
                                                    backgroundColor:"orange",
                                                    fill: false
                                                },
                                                { 
                                                    data: attr_2,
                                                    label: "%s",
                                                    datalabels: {
                                                        color: '#FFCE56',
                                                    },
                                                    borderColor: "blue",
                                                    backgroundColor:"blue",
                                                    fill: false
                                                },
                                                { 
                                                    data: attr_3,
                                                    label: "%s",
                                                    datalabels: {
                                                        color: '#FFCE56',
                                                    },
                                                    borderColor: "navy",
                                                    backgroundColor:"navy",
                                                    fill: false
                                                },
                                                { 
                                                    data: attr_4,
                                                    label: "%s",
                                                    datalabels: {
                                                        color: '#FFCE56',
                                                    },
                                                    borderColor: "purple",
                                                    backgroundColor:"purple",
                                                    fill: false
                                                },
                                                { 
                                                    data: attr_5,
                                                    label: "%s",
                                                    datalabels: {
                                                        color: '#FFCE56',
                                                    },
                                                    borderColor: "green",
                                                    backgroundColor:"green",
                                                    fill: false
                                                },
                                                { 
                                                    data: attr_6,
                                                    label: "%s",
                                                    datalabels: {
                                                        color: '#FFCE56',
                                                    },
                                                    borderColor: "aqua",
                                                    backgroundColor:"aqua",
                                                    fill: false
                                                },
                                                { 
                                                    data: attr_7,
                                                    label: "%s",
                                                    datalabels: {
                                                        color: '#FFCE56',
                                                    },
                                                    borderColor: "teal",
                                                    backgroundColor:"teal",
                                                    fill: false
                                                },
                                                { 
                                                    data: attr_8,
                                                    label: "%s",
                                                    datalabels: {
                                                        color: '#FFCE56',
                                                    },
                                                    borderColor: "yellow",
                                                    backgroundColor:"yellow",
                                                    fill: false
                                                },
                                                { 
                                                    data: attr_9,
                                                    label: "%s",
                                                    datalabels: {
                                                        color: '#FFCE56',
                                                    },
                                                    borderColor: "olive",
                                                    backgroundColor:"olive",
                                                    fill: false
                                                },
                                                { 
                                                    data: attr_10,
                                                    label: "%s",
                                                    datalabels: {
                                                        color: '#FFCE56',
                                                    },
                                                    borderColor: "lime",
                                                    backgroundColor:"lime",
                                                    fill: false
                                                }
                                        ]
                                    }
                                });
                            </script>
                        </div>"""
    
    
    # ======================================================================================
    # Contains the chart template for 4 columns comparison with col-md-6 - Line chart(NPL)
    # ======================================================================================

    chart_template_seven = """<div class = col-md-8><h4><strong>%s</strong></h4> 
                            <canvas id="%s" width="50000" height="30000"></canvas>
                                <script type="text/javascript">
                                    // Our labels along the x-axis
                                    //var row_labels = ["10-20","20-30","30-40"];
                                    var row_labels = %s;
                                    // For drawing the lines
                                    // var fmp = [86,114,106];
                                    var attr_1 = %s;
                                    // var mfmp = [282,350,411];
                                    var attr_2 = %s;
                                    var attr_3 = %s;
                                    var attr_4 = %s;
                                    var ctx = document.getElementById("%s");
                                    var myChart = new Chart(ctx, {
                                            type: 'line',
                                            data: {
                                            labels:row_labels,
                                            datasets: [
                                                { 
                                                    data: attr_1,
                                                    label: "%s",
                                                    datalabels: {
                                                        color: '#FFCE56',
                                                    },
                                                    borderColor: "green",
                                                    backgroundColor:"green",
                                                    fill: false
                                                },
                                                { 
                                                    data: attr_2,
                                                    label: "%s",
                                                    datalabels: {
                                                        color: '#FFCE56',
                                                    },
                                                    borderColor: "blue",
                                                    backgroundColor:"blue",
                                                    fill: false
                                                },
                                                { 
                                                    data: attr_3,
                                                    label: "%s",
                                                    datalabels: {
                                                        color: '#FFCE56',
                                                    },
                                                    borderColor: "red",
                                                    backgroundColor:"red",
                                                    fill: false
                                                },
                                                { 
                                                    data: attr_4,
                                                    label: "%s",
                                                    datalabels: {
                                                        color: '#FFCE56',
                                                    },
                                                    borderColor: "orange",
                                                    backgroundColor:"orange",
                                                    fill: false
                                                }
                                        ]
                                    }
                                });
                            </script>
                        </div>"""

    
    # =================================================================================
    # Contains the HTML footer information
    # ================================================================================

    footer_text = '''
                             
        </div>
        </div>
        </div>
        </div>

        <script>
                function fnExcelReport(tableID, filename)
                {
                var tab_text = '<table border="1px" style="font-size:20px" ">';
                var textRange; 
                var j = 0;
                var tab = document.getElementById(tableID); // id of table
                var lines = tab.rows.length;

                // the first headline of the table
                if (lines > 0) {
                        tab_text = tab_text + '<tr bgcolor="#DFDFDF">' + tab.rows[0].innerHTML + '</tr>';
                }

                // table data lines, loop starting from 1
                for (j = 1 ; j < lines; j++) {     
                        tab_text = tab_text + "<tr>" + tab.rows[j].innerHTML + "</tr>";
                }
                tab_text = tab_text + "</table>";
                tab_text = tab_text.replace(/<A[^>]*>|<\/A>/g, "");             //remove if u want links in your table
                tab_text = tab_text.replace(/<img[^>]*>/gi,"");                 // remove if u want images in your table
                tab_text = tab_text.replace(/<input[^>]*>|<\/input>/gi, "");    // reomves input params
                // console.log(tab_text); // activate so see the result (press F12 in browser)
                tab_text = tab_text.split(String.fromCharCode(8195)).join('&emsp;');
                var ua = window.navigator.userAgent;
                var msie = ua.indexOf("MSIE "); 

                // if Internet Explorer
                if (msie > 0 || !!navigator.userAgent.match(/Trident.*rv\:11\./)) {
                        txtArea1.document.open("txt/html","replace");
                        txtArea1.document.write(tab_text);
                        txtArea1.document.close();
                        txtArea1.focus(); 
                        sa = txtArea1.document.execCommand("SaveAs", true, filename);
                }  
                else { // other browser not tested on IE 11
                        var link = document.createElement("a");
                        link.download = filename;
                        link.href = 'data:application/vnd.ms-excel,' + encodeURIComponent(tab_text)
                        link.click();
                }
                }
        </script>
</body>
</html>'''


    def __init__(self):
        super(Template, self).__init__()


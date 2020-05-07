
  let endpoint = '/api/chart/data';

  function append_to_list(list) {
    list.append(item)
  }
  $.ajax({
      method: "GET",
      url: endpoint,
      success: function(data) {
        let employee_data = [];
        let employee_name = [];
        let employee_sale = [];
        let employee_name2 = [];


        for (let i = 0; i < 5; ++i) {
          employee_data.push(data['employee_rating'][i][2]);
          employee_name.push(data['employee_rating'][i][0] + " " + data['employee_rating'][i][1]);
          employee_sale.push(data['employee_sales'][i][2]);
          employee_name2.push(data['employee_sales'][i][0] + " " + data['employee_sales'][i][1]);
        }


        Chart.defaults.global.defaultFontColor = '#78af9f';

        //horizontal chart

        new Chart(document.getElementById("horizontalBar"), {
          "type": "horizontalBar",
          title: 'Top 5 Employees',
          "data": {
          "labels": employee_name,
          "datasets": [{
          "label": "Average Customer Rating",
          "data":employee_data,
          "fill": false,
          "backgroundColor": ["rgba(255, 99, 132, 0.2)", "rgba(75, 192, 192, 0.2)",
          "rgba(54, 162, 235, 0.2)", "rgba(153, 102, 255, 0.2)", "rgba(201, 203, 207, 0.2)"
          ],
          "borderColor": ["rgb(255, 99, 132)", "rgb(255, 159, 64)", "rgb(255, 205, 86)",
          "rgb(75, 192, 192)", "rgb(54, 162, 235)", "rgb(153, 102, 255)", "rgb(201, 203, 207)"
          ],
          "borderWidth": 1
          }]
          },
          "options": {
          "scales": {
          "xAxes": [{
          "ticks": {
          "beginAtZero": true
          }
          }]
          }
          }
        });


            //horizontal chart2

        new Chart(document.getElementById("horizontalBar2"), {
          "type": "horizontalBar",
          title: 'Top 5 Employees',
          "data": {
          "labels": employee_name2,
          "datasets": [{
          "label": "Total Sales",
          "data":employee_sale,
          "fill": false,
          "backgroundColor": ["rgba(255, 99, 132, 0.2)", "rgba(75, 192, 192, 0.2)",
          "rgba(54, 162, 235, 0.2)", "rgba(153, 102, 255, 0.2)", "rgba(201, 203, 207, 0.2)"
          ],
          "borderColor": ["rgb(255, 99, 132)", "rgb(255, 159, 64)", "rgb(255, 205, 86)",
          "rgb(75, 192, 192)", "rgb(54, 162, 235)", "rgb(153, 102, 255)", "rgb(201, 203, 207)"
          ],
          "borderWidth": 1
          }]
          },
          "options": {
          "scales": {
          "xAxes": [{
          "ticks": {
          "beginAtZero": true
          }
          }]
          }
          }
        });



        //line
        let ctxL = document.getElementById("lineChart").getContext('2d');
        let myLineChart = new Chart(ctxL, {
          type: 'line',
          data: {
          labels: ["March", "April", "May"],
          datasets: [
          {
          label: "2020 Revenue",
          data: [data['month_revenue_march'][0], data['month_revenue_april'][0], data['month_revenue_may'][0]],
          backgroundColor: [
          'rgba(0, 137, 132, .2)',
          ],
          borderColor: [
          'rgba(0, 10, 130, .7)',
          ],
          borderWidth: 2
          }
          ]
          },
          options: {
          responsive: true,
            legend: {
              labels: {
                padding: 100,
              }
            }
          }
        });



      },
      error: function(error_data) {
          console.log("error");
          console.log(error_data)
      }
  });


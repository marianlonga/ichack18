var barChartConfig = {
    type: 'bar',
    data: {
        labels: ["Carbohydrates", "Energy (calories)", "Sugars", "Water", "Calories"],
        datasets: [{
            label: 'Consumption',
            data: [0, 0, 0, 0, 0], //We will put our data here
            backgroundColor: [
                'rgba(255, 99, 132, 0.2)',
                'rgba(54, 162, 235, 0.2)',
                'rgba(255, 206, 86, 0.2)',
                'rgba(153, 102, 255, 0.2)',
                'rgba(255, 159, 64, 0.2)'
            ],
            borderColor: [
                'rgba(255,99,132,1)',
                'rgba(54, 162, 235, 1)',
                'rgba(255, 206, 86, 1)',
                'rgba(153, 102, 255, 1)',
                'rgba(255, 159, 64, 1)'
            ],
            borderWidth: 1
        },
        {
            label: '% Consumption',
            data: [0, 0, 0, 0, 0], //We will put our data here

        }
      ]
    },
    options: {
        scales: {
            yAxes: [{
                ticks: {
                    beginAtZero:true
                }
            }],
            xAxes: [{
                type: 'time',
                display: true,
                scaleLabel: {
                    display: true,
                    labelString: "Date",
                }
            }]
        },
        title: {
            display: true,
            text: 'Nutrition over Time'
        }
    }
}




var barChartConfig2 = {
    type: 'pie',
    data: {
        labels: ["Carbohydrates", "Energy (calories)", "Sugars", "Water", "Calories"],
        datasets: [{
            label: 'Consumption',
            data: [0, 0, 0, 0, 0], //We will put our data here
            backgroundColor: [
                'rgba(255, 99, 132, 0.2)',
                'rgba(54, 162, 235, 0.2)',
                'rgba(255, 206, 86, 0.2)',
                'rgba(153, 102, 255, 0.2)',
                'rgba(255, 159, 64, 0.2)'
            ],
            borderColor: [
                'rgba(255,99,132,1)',
                'rgba(54, 162, 235, 1)',
                'rgba(255, 206, 86, 1)',
                'rgba(153, 102, 255, 1)',
                'rgba(255, 159, 64, 1)'
            ],
            borderWidth: 1
        }]
    },
    options: {
        cutoutPercentage : 50,
        title: {
            display: true,
            text: 'Nutritional Breakdown'
        }
    }
}


var barChartConfig3 = {
    type: 'bar',
    data: {
        labels: ["Carbohydrates", "Energy (calories)", "Sugars", "Water", "Calories"],
        datasets: [{
            label: 'Consumption',
            data: [0, 0, 0, 0, 0], //We will put our data here
            backgroundColor: [
                'rgba(255, 99, 132, 0.2)',
                'rgba(54, 162, 235, 0.2)',
                'rgba(255, 206, 86, 0.2)',
                'rgba(153, 102, 255, 0.2)',
                'rgba(255, 159, 64, 0.2)'
            ],
            borderColor: [
                'rgba(255,99,132,1)',
                'rgba(54, 162, 235, 1)',
                'rgba(255, 206, 86, 1)',
                'rgba(153, 102, 255, 1)',
                'rgba(255, 159, 64, 1)'
            ],
            borderWidth: 1
        },
        {
            label: '% Consumption',
            data: [0, 0, 0, 0, 0], //We will put our data here
            backgroundColor: [
                'rgba(255, 99, 132, 0.2)',
                'rgba(54, 162, 235, 0.2)',
                'rgba(255, 206, 86, 0.2)',
                'rgba(153, 102, 255, 0.2)',
                'rgba(255, 159, 64, 0.2)'
            ],
            borderColor: [
                'rgba(255,99,132,1)',
                'rgba(54, 162, 235, 1)',
                'rgba(255, 206, 86, 1)',
                'rgba(153, 102, 255, 1)',
                'rgba(255, 159, 64, 1)'
            ],
            borderWidth: 1
        }
      ]
    },
    options: {
        scales: {
            yAxes: [{
                ticks: {
                    beginAtZero:true
                }
            }],
            xAxes: [{
                type: 'time',
                display: true,
                scaleLabel: {
                    display: true,
                    labelString: "Date",
                }
            }]
        },
        title: {
            display: true,
            text: 'Cumulative Nutrition over Time'
        }
    }
  }

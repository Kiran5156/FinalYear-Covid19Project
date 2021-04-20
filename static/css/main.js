// var chart = document.getElementById('line-chart').getContext('2d')
// var lineChart =  new Chart(ctx,{
//     type: "line",
//     data:{
//         labels:{{labels | safe }}
//         datesets:[{
//             label : "Data Points",
//             data:{{values|safe}},
//             fill:false,
//             borderColor:"rgb(75,192,192)",
//             lineTension:0.1
            
//         }]
//     },
//     options:{
//         responsive: false 
//     }

// })

var ctx = document.getElementById('line-chart').getContext('2d');
labels = JSON.parse({{ labels | tojson }})
data = JSON.parse({{ values | tojson }})

var myChart = new Chart(ctx, {
    type: 'bar',
    data: {
        labels:  labesl,
        datasets: [{
            label: '# of Votes',
            data:date,
            backgroundColor: [
                'rgba(255, 99, 132, 0.2)',
                'rgba(54, 162, 235, 0.2)',
                'rgba(255, 206, 86, 0.2)',
                'rgba(75, 192, 192, 0.2)',
                'rgba(153, 102, 255, 0.2)',
                'rgba(255, 159, 64, 0.2)'
            ],
            borderColor: [
                'rgba(255, 99, 132, 1)',
                'rgba(54, 162, 235, 1)',
                'rgba(255, 206, 86, 1)',
                'rgba(75, 192, 192, 1)',
                'rgba(153, 102, 255, 1)',
                'rgba(255, 159, 64, 1)'
            ],
            borderWidth: 1
        }]
    },
    options: {
        scales: {
            y: {
                beginAtZero: true
            }
        }
    }
});
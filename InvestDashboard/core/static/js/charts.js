var endpoint 

$.ajax({
    method: "GET"
    url: endpoint,
    success: function(data){
        console.log(data)
    },
    error: function(error_data){
        console.log("error")
        console.log(error_data)
    }
})

var data = {
    datasets: [{
        data: [10, 20, 30]
    }],

    // These labels appear in the legend and in the tooltips when hovering different arcs
    labels: [
        'Red',
        'Yellow',
        'Blue'
    ]
};
var options = {
}
var ctx = document.getElementById("TotalChart");
var myPieChart = new Chart(ctx,{
    type: 'pie',
    data: data,
    options: options
});
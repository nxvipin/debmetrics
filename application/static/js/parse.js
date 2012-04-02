parser = function(data){
	result=Object();
	data.forEach(function(metric){
		result.title = metric.metric;
		result.label = Array();
		result.data = Array();
		result.legend = Array();
		metric.data.forEach(function(metricdata){
			result.legend.push({"label":metricdata.user});
			result.data.push(Array());
			metricdata.userdata.forEach(function(user){
				result.data[result.data.length-1].push(parseInt(user.data));
				console.log(user.data);
				if(metric.data.indexOf(metricdata)==1){
					result.label.push(user.year);
				}
			});
		});
	});return result;
}
plotdata = function(div,result){
					var ticks = result.label;
					$.jqplot(div, result.data, {
						seriesDefaults:{ rendererOptions: {fillToZero: true} },
						series:result.legend,
						legend: { show: true, placement: 'insideGrid', location : 'nw', noColumns:2},
						highlighter:{show:true,sizeAdjust:7.5},
						axes: {	xaxis: { renderer: $.jqplot.CategoryAxisRenderer,ticks: ticks}, yaxis: { pad: 1.0, tickOptions: {formatString: '%d'}}}
						});
				}

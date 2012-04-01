parser = function(data){
	result=Object();
	data.forEach(function(metric){
		result.title = metric.metric;
		result.label = Array();
		result.data = Array();
		result.legend = Array();
		metric.data.forEach(function(metricdata){
			result.label.push(metricdata.year);
			result.data.push(Array());
			metricdata.userdata.forEach(function(user){
				result.data[result.data.length-1].push(parseInt(user.data));
				console.log(user.data);
				if(metric.data.indexOf(metricdata)==1){
					result.legend.push({"label":user.user});
				}
			});
		});
	});return result;
}

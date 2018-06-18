function setup() {
		//loadJSON("http://127.0.0.1:8000/kairiparc", kairiData, 'jsonp');*/
    loadJSON('http://api.open-notify.org/astros.json', kairiData, 'jsonp');
}
	

function kairiData(data){
	console.log(data);
}

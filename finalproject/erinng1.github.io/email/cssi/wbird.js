/*function insertNum(z){
	var z = prompt("Pick a number.");
	y = parseInt(z);
}*/
var i = document.getElementById('numBox');
if (i.value == undefined){
	i.style.visibility === "hidden"};
function toggleShowHide() {
    var x = document.getElementById('allBoxes');
    if (x.style.visibility === 'hidden') {
        x.style.visibility = 'block';
    } else {
        x.style.visibility = 'hidden';
    }
}

function randNum(i){
	i.style.visibility === "block";
}
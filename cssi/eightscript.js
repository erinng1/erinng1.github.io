var inArray = ["Not likely...", "Nope", "Never in a million years.",
			 "No way!", "Of course!", "Sure.", "Yes", "Maybe"];


function question() {
	var a = ["Not likely...", "Nope", "Never in a million years.",
			 "No way!", "Of course!", "Sure.", "Yes", "Maybe"];
  	a = document.getElementById("search").textContext;
  	return a;
};

function answer(){
	alert(question());
};

/*var inArray = ["Not likely...", "Nope", "Never in a million years.",
			 "No way!", "Of course!", "Sure.", "Yes", "Maybe"];

var answer = inArray[Math.floor(Math.random()*inArray.length)];

function question() {
	var x = prompt("What's your question?")
	var y =  String(x); 

	if(y includes("?") == true){
		window.alert(answer)
	} else {
		window.alert("Try again.");
	}
}

question();
*/
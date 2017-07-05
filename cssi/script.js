
function changeImage(){
	var poster = $('#first');

	if(poster.attr('src') == 'cat.jpg'){
		poster.attr('src', 'cat2.jpg');
	} else {
		poster.attr('src', 'cat.jpg');
	}
};

function setupEverything(){
	var poster = $('#first');
	poster.on('click','#second');
}

$(document).on('click', changeImage);

/*function changeLink(){
	var poster = $('#poster');
	var link = $('a');

	if(link.text() == "X-Men"){
		link.attr('href', "http://starwars.com");
		link.text('star Wars');
		poster.attr('src', 'cat2.jpg');
	} else {
		link.text("X-Men");
		link.attr('href', "http://xmen.com");
		poster.attr('src', 'cat2.jpg');
	}
};		*/


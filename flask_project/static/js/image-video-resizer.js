function init() {
	setInitialWidth()
	updateImagesVideosDimens()
}

function setInitialWidth(){
	$( ".image-container" ).each(function( index ) {
		$( this ).data("initialwidth", $( this ).width()) 
	})

	$( ".video-container" ).each(function( index ) {
		iframe = $( this ).find("iframe")
		iframe.data("initialwidth", iframe.width()) 
	})
}

function updateVideosHeight(){
	$(".video-container").each(function(){
		iframe = $( this ).find("iframe")
		iframe.height(9*iframe.width()/16)
	})
}

function updateImagesVideosDimens(){
	$( ".image-container" ).each(function( index ) {
		if( $( this ).data("initialwidth") >=  $( this ).parent().width() ){
			$( this ).width('95%')
		}
		else {
			$( this ).width($( this ).data("initialwidth"))
		}
	})

	$( ".video-container" ).each(function( index ) {
		iframe = $( this ).find("iframe")

		if( iframe.data("initialwidth") >=  iframe.parent().width() ){
			iframe.width('95%')
		}
		else {
			iframe.width(iframe.data("initialwidth"))
		}
	})
	updateVideosHeight()
}

window.onload = init;
window.addEventListener("resize", updateImagesVideosDimens);

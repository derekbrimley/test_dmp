$(function(){
	
	// LoadModal
	$('#shopping_cart').ajaxForm(function(data) {

		console.log("hey there")
		
		$('#jquery-loadmodal-js-body').html(data);

	});//ajaxForm
	
});//ready
$(function(){
	
	// $('#search_btn').on('click',function(){
		// console.log("button clicked")
		// var search_term = $('#user_input').val()

		// console.log(search_term)
		
		// $.ajax({
			
			// url: '/account/products.search/',
			
			// data: {
				// s: search_term,
				
			// }//data
			
		// });//ajax
		
	// });//change
	

	// LoadModal
	$('#search_form').ajaxForm(function(data) {

		console.log("hey there")
		
		$('#jquery-loadmodal-js-body').html(data);

	});//ajaxForm
	
});//ready
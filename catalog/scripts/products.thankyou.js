$(function(){
	
	$('#close_btn').on('click', function() {

		console.log("clicked");
		
		$.ajax({
			
			url: '/catalog/products.delete/',
				
		});//ajax
		
		
	});//click
	
});//ready

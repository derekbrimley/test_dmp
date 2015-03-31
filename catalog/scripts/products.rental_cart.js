$(function(){
	
	// LoadModal
	$('#rental_cart').ajaxForm(function(data) {

		console.log("hey there")
		
		$('#jquery-loadmodal-js-body').html(data);

	});//ajaxForm
	
	$('.delete_btn').on('click',function(){
		
		
		
		var product_id = $(this).attr('data-id');
		console.log(product_id)
		$.ajax({
			
			url: "/catalog/products.delete_rental/"+product_id+"/",
			
			success: function(data){

                    $('.modal-body').html(data);
                },
			
		});//ajax
				
	});//delete
	
});//ready
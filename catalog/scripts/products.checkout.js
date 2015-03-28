$(function(){

	$('#check_out_btn').on('click',function(){
		console.log("checkout")
		$.loadmodal({
			url: '/catalog/products.thankyou/',
			title: 'Billing Information',
			width: '600px',
			id: 'product_container',
		});//modal
				
	});//click
	
	$('.delete_btn').on('click',function(){
		console.log("clicked");
		var product_id = $(this).attr('data-id');
		console.log(product_id)
		$.ajax({
			
			url: "/catalog/products.delete/"+product_id+"/",
			
			success: function(data){

				$('.shopping_cart').html(data);
            },
			
		});//ajax
				
	});//delete
	
});//ready
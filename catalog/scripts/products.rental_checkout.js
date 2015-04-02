$(function(){

	$('#check_out_btn').on('click',function(){
		console.log("checkout")
		
		due_date = $(".due_date").attr('data-id');
		customer_id = $(".customer").attr('data-customer-id');
		
		$.loadmodal({
			url: '/catalog/products.rental_confirmation/'+due_date+'/'+customer_id+'/',
			title: 'Rental Confirmation',
			width: '600px',
			id: 'product_container',
		});//modal
				
	});//click
	
	$('.delete_btn').on('click',function(){
		console.log("clicked");
		var product_id = $(this).attr('data-id');
		console.log(product_id)
		$.ajax({
			
			url: "/catalog/products.delete_rental/"+product_id+"/",
			
			success: function(data){

				$('.rental_cart').html(data);
            },
			
		});//ajax
				
	});//delete
	
});//ready
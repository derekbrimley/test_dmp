$(function(){

	$('#check_out_btn').on('click',function(){
		console.log("checkout")
		$.loadmodal({
			url: '/catalog/products.thankyou/',
			title: 'Billing Information',
			width: '600px',
			id: 'product_container',
		});//modal
				
	})
	
});//ready
$(function(){
	
	$('#add_btn').on('click', function() {
		console.log("clicked")
		$product_id = $(this).attr('data-id');
		$quantity = $('#quantity').val();

		console.log($product_id);
		
		$.loadmodal({
			url: '/catalog/products.add_item/'+$product_id+'/'+$quantity+'/',
			title: 'Shopping Cart',
			width: '1000px',
			id: 'product_container',
		});//modal

	});//click
	
});//ready







$(function(){
	
	$('#add_btn').on('click', function() {
		
		$input = $(this)
		
		
		$.loadmodal({
			url: '/catalog/products.shopping_cart/'+$input.attr("data-id")+'/',
			title: 'Shopping Cart',
			width: '600px',
		});//modal

	});//click
	
});//ready







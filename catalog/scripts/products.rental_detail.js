$(function(){
	
	$('#add_btn').on('click', function() {
		console.log("clicked")
		$product_id = $(this).attr('data-id');
		$quantity = $('#quantity').val();
		$username = document.getElementById('customer').value;
		$due_date = document.getElementById('due_date').value;
		
		console.log($product_id);
		
		$.loadmodal({
			url: '/catalog/products.add_rental_item/'+$product_id+'/'+$quantity+'/'+$username+'/'+$due_date+'/',
			title: 'Rental Cart',
			width: '1000px',
			id: 'product_container',
		});//modal

	});//click
	
	
	
});//ready







$(function(){
	
	$('#open_search_dialog').on('click', function() {
		
		$.loadmodal({
			url: '/catalog/products.search/',
			title: 'Search',
			width: '600px',
		});//modal
		
	});//click
	
	$('#search_box').on('change',function(){
		user_input = $(this).val()
		
		var product_id = $('*:contains("'+user_input+'")').last().attr('data-id');
		
		console.log(product_id)
		
		$.loadmodal({
			url:"/catalog/products.detail_modal/"+product_id,
			title: 'Search for: '+user_input,
			width: '600px',
		});//modal
		
		
	});//
		
	$('.submit_btn').on('click',function(){
		console.log("clicked");
		
		
	});//click	
	
	
});//ready
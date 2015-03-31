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
	
	// $.expr[":"].contains = $.expr.createPseudo(function(arg) {
		// return function( elem ) {
		// return $(elem).text().toUpperCase().indexOf(arg.toUpperCase()) >= 0;
		// };
	// });
		
	$('#search_btn').on('click',function(){
		console.log("button clicked")
		var search_term = $('#user_input').val()

		console.log(search_term)
		
		$.ajax({
			
			url: '/account/products.search/',
			
			data: {
				s: search_term,
				
			}//data
			
		});//ajax
		
	});//change
	

	// LoadModal
	$('#search_form').ajaxForm(function(data) {

		console.log("hey there")
		
		console.log($('#search_btn').val());
		
		$('#jquery-loadmodal-js-body').html(data);

	});//ajaxForm	
		
	$('.submit_btn').on('click',function(){
		console.log("clicked");
		
		
	});//click	
	
	
});//ready
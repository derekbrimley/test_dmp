$(function(){
	
	$('#open_search_dialog').on('click', function() {
		
		$.loadmodal({
			url: '/catalog/products.search/',
			title: 'Search',
			width: '600px',
		});//modal
		
	});//click
	
});//ready


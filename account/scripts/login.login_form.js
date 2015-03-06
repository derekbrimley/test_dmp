$(function(){

	//LoadModal
	$('#login_form').ajaxForm(function(data) {
		
		console.log($('#jquery-loadmodal-js-body'))
		
		$('#jquery-loadmodal-js-body').html(data);

	});//ajaxForm
	
});//ready
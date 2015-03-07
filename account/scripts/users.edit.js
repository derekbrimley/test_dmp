$(function(){

	$('#id_username').on('change',function(){
		console.log("change")
		
		var user_input = $(this).val();
		
		$.ajax({
			url: '/account/login.check_username/',
			
			data: {
				u: user_input,
			},//data
			
			type: "POST",
			
			success: function(resp){
				if(resp == '0'){
					$('#id_username_message').text('Not a valid username!');
				}
				else{
					$('#id_username_message').text('Valid username.');
				};//if
				
			},//success
			
		});//ajax
		
	});//change
	
});//ready







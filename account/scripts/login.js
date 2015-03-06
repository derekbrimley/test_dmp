$(function(){
	
	$('#id_username').on('change', function(){
		
		var username = $(this).val()
		
		$.ajax({
			url: '/account/login.check_username/',
			
			data: {
				u: username,
			},//data
			
			type: "POST",
			
			success: function(resp){
				if(resp == '1'){
					$('#id_username_message').text('Not a valid username!');
				}
				else{
					$('#id_username_message').text('Valid username.');
				};//if
				
			},//success
			
		});//ajax
		
	});//change
	
	console.log($('#login_form'));
	$('#login_form').ajaxForm(function(data) { 
		
		$('#login_form_container').html(data);
		
	});//
	
	$('#create_user_dialog').modal({
		show: false
	})//modal

	$('#create_user_dialog').on('click',function(){
		$('#create_user_dialog').modal('show');
		$.ajax({
			url: '/homepage/users.create/',
		});
		
	});//show
	
});//ready







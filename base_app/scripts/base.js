$(function(){
	
	// $('#login_form').on('change', function(){
		
		// var username = $(this).val()
		
		// $.ajax({
			// url: '/account/login.check_username/',
			
			// data: {
				// u: username,
			// },//data
			
			// type: "POST",
			
			// success: function(resp){
				// if(resp == '1'){
					// $('#id_username_message').text('Not a valid username!');
				// }
				// else{
					// $('#id_username_message').text('Valid username.');
				// };//if
				
			// },//success
			
		// });//ajax
		
	// });//change
	
	// $('#login_dialog').modal({
		// show: false
	// })//modal

	$('#show_login_dialog').on('click', function() {
		
		$.loadmodal({
			url: '/account/login.login_form/',
			title: 'Login',
			width: '600px',
		});

	});//click
	
	
	
	// $('#show_login_dialog').on('click',function(){
		
		// $('#login_dialog').modal('show');
		// $.ajax({
			// url: '/account/login.login_form/',
			// success: function(data){
				// console.log($('#login_dialog').find('.modal-body').html(data));
			// },//success
			
		// });//ajax
		
	// });//show
	
});//ready










$(function () {
   $("#datepicker").datepicker({
       autoclose: true,
       todayHighlight: true
    }).datepicker('update', new Date());
});

$(document).ready(function(){
	$(".dropdown-menu li a").click(function(){
	  $(this).parents(".dropdown").find('.btn').html($(this).text() + ' <span><i class="fa fa-chevron-down" aria-hidden="true"></i></span>');
	  $(this).parents(".dropdown").find('.btn').val($(this).data('value'));
	});
});



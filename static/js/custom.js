


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


	$(".expert_bio_wrap_toggle").click(function(){
    $(this).parent(".expert-details").siblings(".expert_bio_wrap").slideToggle( "slow");
     if ($(this).text() == "View more")
      {        
        $(this).html("View less")
      }
     else 
      {     
        $(this).text("View more")
      }
  }); 

  $(".tooltip").click(function(){
      $(".tooltip-info").toggle();
    });


   $('.carousel').slick({
    slidesToShow: 2.1,
    slidesToScroll: 2.1,
        mobileFirst: true,
        arrows: false,
        dots: false,
        responsive: [
            {
                breakpoint: 992,
                settings: 'unslick'
            }
        ]
    });

    $(window).on('resize', function() {
        $('.carousel').slick('resize');
    });

});



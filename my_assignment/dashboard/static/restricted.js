// Hide forms to start with
$(".patient_form_div").hide();
$(".doctor_form_div").hide();
$(".nurse_form_div").hide();

// Show patient form on click and hide all plus boxes
$(".add_forms_div.patient").on("click", function(){
	$(".patient_form_div").show();
	$(".add_forms_div.patient").hide();
	$(".add_forms_div.doctor").hide();
	$(".add_forms_div.nurse").hide();

});

// Show doctor form on click and hide all plus boxes
$(".add_forms_div.doctor").on("click", function(){
	$(".doctor_form_div").show();
	$(".add_forms_div.patient").hide();
	$(".add_forms_div.doctor").hide();
	$(".add_forms_div.nurse").hide();

});

// Show nurse form on click and hide all plus boxes
$(".add_forms_div.nurse").on("click", function(){
	$(".nurse_form_div").show();
	$(".add_forms_div.patient").hide();
	$(".add_forms_div.doctor").hide();
	$(".add_forms_div.nurse").hide();

});

// Reset buttons
$("#close_post_patient").on("click", function(){
	$(".patient_form_div").hide();
	$(".doctor_form_div").hide();
	$(".nurse_form_div").hide();
	$(".add_forms_div.patient").show();
	$(".add_forms_div.doctor").show();
	$(".add_forms_div.nurse").show();
});

$("#close_post_doctor").on("click", function(){
	$(".patient_form_div").hide();
	$(".doctor_form_div").hide();
	$(".nurse_form_div").hide();
	$(".add_forms_div.patient").show();
	$(".add_forms_div.doctor").show();
	$(".add_forms_div.nurse").show();
});

$("#close_post_nurse").on("click", function(){
	$(".patient_form_div").hide();
	$(".doctor_form_div").hide();
	$(".nurse_form_div").hide();
	$(".add_forms_div.patient").show();
	$(".add_forms_div.doctor").show();
	$(".add_forms_div.nurse").show();
});

// Line breaks to all form input entries
$("input").after("<br />");
$("select").after("<br />");




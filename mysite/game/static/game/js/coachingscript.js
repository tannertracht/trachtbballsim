// These are set when a div is clicked
var offenseCoachingAdjustment = 0;
var defenseCoachingAdjustment = 0;
var par = "";
// When the save button is clicked, position will be discovered and sent with the Post request.

window.onload = setGlobals;

function setGlobals(){
	PGinfo = pointGuardInfo;
	SGinfo = shootingGuardInfo;
	SFinfo = smallForwardInfo;
	PFinfo = powerForwardInfo;
	Cinfo = centerInfo;
	setAdjustments();
}

function setAdjustments() {
	if (PGinfo[0] == 'True') {
		$("[id='Point Guard Coaching Table']").find("[id='Shoot First']").css('background-color', "green");
	} else {
		$("[id='Point Guard Coaching Table']").find("[id='Shoot First']").css('background-color', "red");
	}
	if (PGinfo[1] == 'True') {
		$("[id='Point Guard Coaching Table']").find("[id='Pass First']").css('background-color', "green");
	} else {
		$("[id='Point Guard Coaching Table']").find("[id='Pass First']").css('background-color', "red");
	}
	if (PGinfo[2] == 'True') {
		$("[id='Point Guard Coaching Table']").find("[id='Catch and Shoot']").css('background-color', "green");
	} else {
		$("[id='Point Guard Coaching Table']").find("[id='Catch and Shoot']").css('background-color', "red");
	}
	if (PGinfo[3] == 'True') {
		$("[id='Point Guard Coaching Table']").find("[id='Help Defender']").css('background-color', "green");
	} else {
		$("[id='Point Guard Coaching Table']").find("[id='Help Defender']").css('background-color', "red");
	}
	if (PGinfo[4] == 'True') {
		$("[id='Point Guard Coaching Table']").find("[id='Deny Shot']").css('background-color', "green");
	} else {
		$("[id='Point Guard Coaching Table']").find("[id='Deny Shot']").css('background-color', "red");
	}
	if (PGinfo[5] == 'True') {
		$("[id='Point Guard Coaching Table']").find("[id='Deny Pass']").css('background-color', "green");
	} else {
		$("[id='Point Guard Coaching Table']").find("[id='Deny Pass']").css('background-color', "red");
	}
	if (SGinfo[0] == 'True') {
		$("[id='Shooting Guard Coaching Table']").find("[id='Shoot First']").css('background-color', "green");
	} else {
		$("[id='Shooting Guard Coaching Table']").find("[id='Shoot First']").css('background-color', "red");
	}
	if (SGinfo[1] == 'True') {
		$("[id='Shooting Guard Coaching Table']").find("[id='Pass First']").css('background-color', "green");
	} else {
		$("[id='Shooting Guard Coaching Table']").find("[id='Pass First']").css('background-color', "red");
	}
	if (SGinfo[2] == 'True') {
		$("[id='Shooting Guard Coaching Table']").find("[id='Catch and Shoot']").css('background-color', "green");
	} else {
		$("[id='Shooting Guard Coaching Table']").find("[id='Catch and Shoot']").css('background-color', "red");
	}
	if (SGinfo[3] == 'True') {
		$("[id='Shooting Guard Coaching Table']").find("[id='Help Defender']").css('background-color', "green");
	} else {
		$("[id='Shooting Guard Coaching Table']").find("[id='Help Defender']").css('background-color', "red");
	}
	if (SGinfo[4] == 'True') {
		$("[id='Shooting Guard Coaching Table']").find("[id='Deny Shot']").css('background-color', "green");
	} else {
		$("[id='Shooting Guard Coaching Table']").find("[id='Deny Shot']").css('background-color', "red");
	}
	if (SGinfo[5] == 'True') {
		$("[id='Shooting Guard Coaching Table']").find("[id='Deny Pass']").css('background-color', "green");
	} else {
		$("[id='Shooting Guard Coaching Table']").find("[id='Deny Pass']").css('background-color', "red");
	}
	if (SFinfo[0] == 'True') {
		$("[id='Small Forward Coaching Table']").find("[id='Shoot First']").css('background-color', "green");
	} else {
		$("[id='Small Forward Coaching Table']").find("[id='Shoot First']").css('background-color', "red");
	}
	if (SFinfo[1] == 'True') {
		$("[id='Small Forward Coaching Table']").find("[id='Pass First']").css('background-color', "green");
	} else {
		$("[id='Small Forward Coaching Table']").find("[id='Pass First']").css('background-color', "red");
	}
	if (SFinfo[2] == 'True') {
		$("[id='Small Forward Coaching Table']").find("[id='Catch and Shoot']").css('background-color', "green");
	} else {
		$("[id='Small Forward Coaching Table']").find("[id='Catch and Shoot']").css('background-color', "red");
	}
	if (SFinfo[3] == 'True') {
		$("[id='Small Forward Coaching Table']").find("[id='Help Defender']").css('background-color', "green");
	} else {
		$("[id='Small Forward Coaching Table']").find("[id='Help Defender']").css('background-color', "red");
	}
	if (SFinfo[4] == 'True') {
		$("[id='Small Forward Coaching Table']").find("[id='Deny Shot']").css('background-color', "green");
	} else {
		$("[id='Small Forward Coaching Table']").find("[id='Deny Shot']").css('background-color', "red");
	}
	if (SFinfo[5] == 'True') {
		$("[id='Small Forward Coaching Table']").find("[id='Deny Pass']").css('background-color', "green");
	} else {
		$("[id='Small Forward Coaching Table']").find("[id='Deny Pass']").css('background-color', "red");
	}
	if (PFinfo[0] == 'True') {
		$("[id='Power Forward Coaching Table']").find("[id='Shoot First']").css('background-color', "green");
	} else {
		$("[id='Power Forward Coaching Table']").find("[id='Shoot First']").css('background-color', "red");
	}
	if (PFinfo[1] == 'True') {
		$("[id='Power Forward Coaching Table']").find("[id='Pass First']").css('background-color', "green");
	} else {
		$("[id='Power Forward Coaching Table']").find("[id='Pass First']").css('background-color', "red");
	}
	if (PFinfo[2] == 'True') {
		$("[id='Power Forward Coaching Table']").find("[id='Catch and Shoot']").css('background-color', "green");
	} else {
		$("[id='Power Forward Coaching Table']").find("[id='Catch and Shoot']").css('background-color', "red");
	}
	if (PFinfo[3] == 'True') {
		$("[id='Power Forward Coaching Table']").find("[id='Help Defender']").css('background-color', "green");
	} else {
		$("[id='Power Forward Coaching Table']").find("[id='Help Defender']").css('background-color', "red");
	}
	if (PFinfo[4] == 'True') {
		$("[id='Power Forward Coaching Table']").find("[id='Deny Shot']").css('background-color', "green");
	} else {
		$("[id='Power Forward Coaching Table']").find("[id='Deny Shot']").css('background-color', "red");
	}
	if (PFinfo[5] == 'True') {
		$("[id='Power Forward Coaching Table']").find("[id='Deny Pass']").css('background-color', "green");
	} else {
		$("[id='Power Forward Coaching Table']").find("[id='Deny Pass']").css('background-color', "red");
	}
	if (Cinfo[0] == 'True') {
		$("[id='Center Coaching Table']").find("[id='Shoot First']").css('background-color', "green");
	} else {
		$("[id='Center Coaching Table']").find("[id='Shoot First']").css('background-color', "red");
	}
	if (Cinfo[1] == 'True') {
		$("[id='Center Coaching Table']").find("[id='Pass First']").css('background-color', "green");
	} else {
		$("[id='Center Coaching Table']").find("[id='Pass First']").css('background-color', "red");
	}
	if (Cinfo[2] == 'True') {
		$("[id='Center Coaching Table']").find("[id='Catch and Shoot']").css('background-color', "green");
	} else {
		$("[id='Center Coaching Table']").find("[id='Catch and Shoot']").css('background-color', "red");
	}
	if (Cinfo[3] == 'True') {
		$("[id='Center Coaching Table']").find("[id='Help Defender']").css('background-color', "green");
	} else {
		$("[id='Center Coaching Table']").find("[id='Help Defender']").css('background-color', "red");
	}
	if (Cinfo[4] == 'True') {
		$("[id='Center Coaching Table']").find("[id='Deny Shot']").css('background-color', "green");
	} else {
		$("[id='Center Coaching Table']").find("[id='Deny Shot']").css('background-color', "red");
	}
	if (Cinfo[5] == 'True') {
		$("[id='Center Coaching Table']").find("[id='Deny Pass']").css('background-color', "green");
	} else {
		$("[id='Center Coaching Table']").find("[id='Deny Pass']").css('background-color', "red");
	}
}



$(function() {
  $("body").click(function(e) {
    if (e.target.id == "Point Guard") {
		update()
		// Remove 'coaching-table-hidden' from clicked div
		$("[id='Point Guard Coaching Table']").toggleClass("coaching-table-hidden")
		// Add 'coaching-table-visible' to clicked div
		$("[id='Point Guard Coaching Table']").toggleClass("coaching-table-visible")
		// Add 'selected-player' class to clicked div so it is visible
		$("[id='Point Guard']").toggleClass("selected-player");
    } else if (e.target.id == "Shooting Guard") {
		update()
		$("[id='Shooting Guard Coaching Table']").toggleClass("coaching-table-hidden")
		$("[id='Shooting Guard Coaching Table']").toggleClass("coaching-table-visible")
		$("[id='Shooting Guard']").toggleClass("selected-player");
    } else if (e.target.id == "Small Forward") {
		update()
		$("[id='Small Forward Coaching Table']").toggleClass("coaching-table-hidden")
		$("[id='Small Forward Coaching Table']").toggleClass("coaching-table-visible")
		$("[id='Small Forward']").toggleClass("selected-player");
    } else if (e.target.id == "Power Forward") {
		update()
		$("[id='Power Forward Coaching Table']").toggleClass("coaching-table-hidden")
		$("[id='Power Forward Coaching Table']").toggleClass("coaching-table-visible")
		$("[id='Power Forward']").toggleClass("selected-player");
    } else if (e.target.id == "Center") {
		update()
		$("[id='Center Coaching Table']").toggleClass("coaching-table-hidden")
		$("[id='Center Coaching Table']").toggleClass("coaching-table-visible")
		$("[id='Center']").toggleClass("selected-player");
    } else if (e.target.id == "Shoot First") {
		changes(1);
		par = $("[id='Shoot First']").parents('.coaching-table-visible').attr('id');
		$("[id='Pass First']").css('background-color', 'red');
		$("[id='Catch and Shoot']").css('background-color', 'red');
		if (e.target.style.backgroundColor == 'red') {
			e.target.style.backgroundColor = 'green';
			offenseCoachingAdjustment = 1;
		} else if (e.target.style.backgroundColor == 'green') {
			e.target.style.backgroundColor = 'red';
			offenseCoachingAdjustment = 4;
		}
    } else if (e.target.id == "Pass First") {
		changes(1);
		par = $("[id='Pass First']").parents('.coaching-table-visible').attr('id');
		$("[id='Catch and Shoot']").css('background-color', 'red');
		$("[id='Shoot First']").css('background-color', 'red');
		if (e.target.style.backgroundColor == 'red') {
			e.target.style.backgroundColor = 'green';
			offenseCoachingAdjustment = 2;
		} else if (e.target.style.backgroundColor == 'green') {
			e.target.style.backgroundColor = 'red';
			offenseCoachingAdjustment = 4;
		}
    } else if (e.target.id == "Catch and Shoot") {
		changes(1);
		par = $("[id='Catch and Shoot']").parents('.coaching-table-visible').attr('id');
		$("[id='Pass First']").css('background-color', 'red');
		$("[id='Shoot First']").css('background-color', 'red');
		if (e.target.style.backgroundColor == 'red') {
			e.target.style.backgroundColor = 'green';
			offenseCoachingAdjustment = 3;
		} else if (e.target.style.backgroundColor == 'green') {
			e.target.style.backgroundColor = 'red';
			offenseCoachingAdjustment = 4;
		}
    } else if (e.target.id == "Help Defender") {
		changes(1);
		par = $("[id='Help Defender']").parents('.coaching-table-visible').attr('id');
		$("[id='Deny Shot']").css('background-color', 'red');
		$("[id='Deny Pass']").css('background-color', 'red');
		if (e.target.style.backgroundColor == 'red') {
			e.target.style.backgroundColor = 'green';
			defenseCoachingAdjustment = 1;
		} else if (e.target.style.backgroundColor == 'green') {
			e.target.style.backgroundColor = 'red';
			defenseCoachingAdjustment = 4;
		}
    } else if (e.target.id == "Deny Shot") {
		changes(1);
		par = $("[id='Deny Shot']").parents('.coaching-table-visible').attr('id');
		$("[id='Deny Pass']").css('background-color', 'red');
		$("[id='Help Defender']").css('background-color', 'red');
		if (e.target.style.backgroundColor == 'red') {
			e.target.style.backgroundColor = 'green';
			defenseCoachingAdjustment = 2;
		} else if (e.target.style.backgroundColor == 'green') {
			e.target.style.backgroundColor = 'red';
			defenseCoachingAdjustment = 4;
		}
    } else if (e.target.id == "Deny Pass") {
		changes(1);
		par = $("[id='Deny Pass']").parents('.coaching-table-visible').attr('id');
		$("[id='Help Defender']").css('background-color', 'red');
		$("[id='Deny Shot']").css('background-color', 'red');
		if (e.target.style.backgroundColor == 'red') {
			e.target.style.backgroundColor = 'green';
			defenseCoachingAdjustment = 3;
		} else if (e.target.style.backgroundColor == 'green') {
			e.target.style.backgroundColor = 'red';
			defenseCoachingAdjustment = 4;
		}
    } else {
		// If no divs are clicked remove color and visibility
		update();
		
		
	}
  });
})

function update() {
	changes(0);
	offenseCoachingAdjustment = 0;
	defenseCoachingAdjustment = 0;
	// Add class 'coaching-table-hidden' to all divs that possess 'coaching-table-visible'
	$(".coaching-table-visible").toggleClass("coaching-table-hidden")
	// All classes that contain 'coaching-table-visible' remove 'coaching-table-visible' so it will have display set to none
	$(".coaching-table-visible").toggleClass("coaching-table-visible")
	// Remove 'selected-player' class from all divs that have 'selected-player' so nothing is visible
	$(".selected-player").toggleClass("selected-player");
	setAdjustments();
}

function changes(display) {
	if (display == true) {
		$("[id='Save Adjustments']").css('display', 'flex');
	} else {
		$("[id='Save Adjustments']").css('display', 'none');
	}
}

$.ajaxSetup({ 
     beforeSend: function(xhr, settings) {
         function getCookie(name) {
             var cookieValue = null;
             if (document.cookie && document.cookie != '') {
                 var cookies = document.cookie.split(';');
                 for (var i = 0; i < cookies.length; i++) {
                     var cookie = jQuery.trim(cookies[i]);
                     // Does this cookie string begin with the name we want?
                     if (cookie.substring(0, name.length + 1) == (name + '=')) {
                         cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                         break;
                     }
                 }
             }
             return cookieValue;
         }
         if (!(/^http:.*/.test(settings.url) || /^https:.*/.test(settings.url))) {
             // Only send the token to relative URLs i.e. locally.
             xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
         }
     } 
});

document.getElementById("Save Adjustments Button").onclick = function(){
	data = {'offenseadjustment': offenseCoachingAdjustment,'defenseadjustment': defenseCoachingAdjustment, 'position':par};
	$.post("coachingupdate", data, function(data) {
		//alert(data);
	});
	if (par == "Point Guard Coaching Table") {
		changeAdjustments(PGinfo, offenseCoachingAdjustment, defenseCoachingAdjustment);
	} else if (par == "Shooting Guard Coaching Table") {
		changeAdjustments(SGinfo, offenseCoachingAdjustment, defenseCoachingAdjustment);
	} else if (par == "Small Forward Coaching Table") {
		changeAdjustments(SFinfo, offenseCoachingAdjustment, defenseCoachingAdjustment);
	} else if (par == "Power Forward Coaching Table") {
		changeAdjustments(PFinfo, offenseCoachingAdjustment, defenseCoachingAdjustment);
	} else if (par == "Center Coaching Table") {
		changeAdjustments(Cinfo, offenseCoachingAdjustment, defenseCoachingAdjustment);
	}
}

function changeAdjustments(player, Oadjustment, Dadjustment) {
	if (Oadjustment != 0) {
		player[0] = 'False';
		player[1] = 'False';
		player[2] = 'False';
	}
	if (Dadjustment != 0) {
		player[3] = 'False';
		player[4] = 'False';
		player[5] = 'False';
	}
	if (Oadjustment == 1) {
		player[0] = 'True';
	} else if (Oadjustment == 2) {
		player[1] = 'True';
	} else if (Oadjustment == 3) {
		player[2] = 'True';
	}
	if (Dadjustment == 1) {
		player[3] = 'True';
	} else if (Dadjustment == 2) {
		player[4] = 'True';
	} else if (Dadjustment == 3) {
		player[5] = 'True';
	}
}







document.getElementById("Start Sim Button").onclick = function(){
	// Make Simulation Button Dissapear
	document.getElementById("Start Simulation").style.display = "none";
	document.getElementById("Last Play Screen").style.display = "flex";
	alert("pop")
	// Initiate Simulation
	// Must change IP below when hosting differently
	$.get("http://127.0.0.1:8000/simulation", function(data, status){
        // data is a javascript object. All keys in original dict are referencable
		i = 1;
		function revealSimulation() {
			$("[class='row user-player-box']").css('background-color', 'white');
			$("[class='row opposing-player-box']").css('background-color', 'white');
			baseOne = 'Posession1OffensePlayer';
			baseTwo = 'Posession1DefensePlayer';
			baseThree = 'Posession1Result';
			baseFour = 'Posession1Score';
			baseFive = 'Posession1RecievedPass';
			modifiedBaseOne = baseOne.replace('1', i.toString());
			modifiedBaseTwo = baseTwo.replace('1', i.toString());
			modifiedBaseThree = baseThree.replace('1', i.toString());
			modifiedBaseFour = baseFour.replace('1', i.toString());
			modifiedBaseFive = baseFive.replace('1', i.toString());
			//console.log(data[modifiedBaseThree])
			$("[id='Offense Player Name']").text(data[modifiedBaseOne][0] + ' ' + data[modifiedBaseOne][1]);
			$("[id='Defense Player Name']").text(data[modifiedBaseTwo][0] + ' ' + data[modifiedBaseTwo][1]);
			$("[id='User Team Score']").text(data[modifiedBaseFour][0]);
			$("[id='Opposing Team Score']").text(data[modifiedBaseFour][1]);
			if (data[modifiedBaseThree][0] == 1) {
				$("[id='Result']").html("<strong> SHOT MADE </strong>");
				$("[class='row user-player-box']:contains('" + data[modifiedBaseOne][0] + "')").css('background-color', '#75f977');
				$("[class='row opposing-player-box']:contains('" + data[modifiedBaseOne][0] + "')").css('background-color', '#75f977');
			} else if (data[modifiedBaseThree][0] == 2) {
				$("[id='Result']").html("<strong> SHOT MISS </strong>");
				$("[class='row user-player-box']:contains('" + data[modifiedBaseOne][0] + "')").css('background-color', '#fc3737');
				$("[class='row opposing-player-box']:contains('" + data[modifiedBaseOne][0] + "')").css('background-color', '#fc3737');
			}
			$("[id='Shot Make Chance']").html("<strong>" + Math.floor(data[modifiedBaseThree][1]*100) + "</strong>");
			if (data[modifiedBaseFive] == true) {
				$("[class='row user-player-box']:contains('" + data[modifiedBaseThree][2] + "')").css('background-color', '#5e93ff');
				$("[class='row opposing-player-box']:contains('" + data[modifiedBaseThree][2] + "')").css('background-color', '#5e93ff');
			}
			i++;
			if (i > 10) {
				clearInterval(handle);
			};
		};
		var handle = setInterval(revealSimulation, 2000);
    }); 
};

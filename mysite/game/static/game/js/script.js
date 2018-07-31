







// Nothing happens on this page until the 'Start Simulation' button is clicked
document.getElementById("Start Sim Button").onclick = function(){
	// Make Simulation Button Dissapear
	document.getElementById("Start Simulation").style.display = "none";
	// Make last play screen visible
	document.getElementById("Last Play Screen").style.display = "flex";
	// Initiate Simulation
	// Must change IP below when hosting differently
	$.get("/simulation", function(data, status){
        // data is a javascript object. All keys in original dict are referencable by data[key] 
		i = 1;
		function revealSimulation() {
			// At start of loop set all player box backgrounds to white
			$("[class='row user-player-box']").css('background-color', 'white');
			$("[class='row opposing-player-box']").css('background-color', 'white');
			// Define keys to be used to navigate the data returned by the server
			baseOne = 'Posession1OffensePlayer';
			baseTwo = 'Posession1DefensePlayer';
			baseThree = 'Posession1Result';
			baseFour = 'Posession1Score';
			baseFive = 'Posession1RecievedPass';
			// Each loop modify the strings so that their contents reflect the current posession (change Posession1OffensePlayer to Posession2OffensePlayer and so on)
			modifiedBaseOne = baseOne.replace('1', i.toString()); // Is a list with 2 elements, [first name, last name] of offense player ['Steve', 'Rodgers']
			modifiedBaseTwo = baseTwo.replace('1', i.toString()); // Is a list with 2 elements, [first name, last name] of defense player ['Aaron', 'Rodgers']
			modifiedBaseThree = baseThree.replace('1', i.toString()); // Is a list with 3 elements [result in the form of an int (1 = Made shot, 2 = Missed Shot), Shot make chance in decimal form (.65), the player who made the pass (if a pass was made) in string form (Dennis Rodman)
			modifiedBaseFour = baseFour.replace('1', i.toString()); // Is a list containing the user team's score and opposing team's score [6, 8]
			modifiedBaseFive = baseFive.replace('1', i.toString()); // Bool indicating whether the offense player recieved the ball via pass (True/False)
			// Sets the current player box's text to contain the players first and last names
			$("[id='Offense Player Name']").text(data[modifiedBaseOne][0] + ' ' + data[modifiedBaseOne][1]);
			$("[id='Defense Player Name']").text(data[modifiedBaseTwo][0] + ' ' + data[modifiedBaseTwo][1]);
			// Update score box with current score values
			$("[id='User Team Score']").text(data[modifiedBaseFour][0]);
			$("[id='Opposing Team Score']").text(data[modifiedBaseFour][1]);
			// If statement with 2 different outcomes depending on if shot was made or missed
			if (data[modifiedBaseThree][0] == 1) {
				// Shot was made
				// Change result box to SHOT MADE. Used .html here to make it <strong>
				$("[id='Result']").html("<strong> SHOT MADE </strong>");
				// Make the offense player's box green. 2 lines are needed to check both user players and opposing players
				// BUG ALERT: If two players have the same name they will both turn green
				$("[class='row user-player-box']:contains('" + data[modifiedBaseOne][0] + " " + data[modifiedBaseOne][1] + "')").css('background-color', '#75f977');
				$("[class='row opposing-player-box']:contains('" + data[modifiedBaseOne][0] + " " + data[modifiedBaseOne][1]  + "')").css('background-color', '#75f977');
			} else if (data[modifiedBaseThree][0] == 2) {
				// Shot was missed
				// Same stuff as above...except red
				$("[id='Result']").html("<strong> SHOT MISS </strong>");
				$("[class='row user-player-box']:contains('" + data[modifiedBaseOne][0] + " " + data[modifiedBaseOne][1]  + "')").css('background-color', '#fc3737');
				$("[class='row opposing-player-box']:contains('" + data[modifiedBaseOne][0] + " " + data[modifiedBaseOne][1]  + "')").css('background-color', '#fc3737');
			}
			// Update the shot make chance box. Perform some math to make a decimal (.7685) show up as 76
			$("[id='Shot Make Chance']").html("<strong>" + Math.floor(data[modifiedBaseThree][1]*100) + "</strong>");
			// Checks if the offense player recieved the ball via pass
			if (data[modifiedBaseFive] == true) {
				// Recieved via pass
				// Make the passers box blue
				// Same BUG ALERT
				$("[class='row user-player-box']:contains('" + data[modifiedBaseThree][2] + "')").css('background-color', '#5e93ff');
				$("[class='row opposing-player-box']:contains('" + data[modifiedBaseThree][2] + "')").css('background-color', '#5e93ff');
			}
			// Increment i as when we get to 10 we will run out of information
			i++;
			if (i > 10) {
				// Stops the interval from running
				clearInterval(handle);
			};
		};
		// Sets an interval. Will call revealSimulation every 2000ms (2 seconds)
		var handle = setInterval(revealSimulation, 2000);
    }); 
};

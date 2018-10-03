
(function () {

  var app = {
    init: function () {
      this.config = {
        apiKey: "AIzaSyA21YIhMezhPr_uaYpVn9Ut-oQ-Epwt81A",
		authDomain: "labo2-nickboon-23.firebaseapp.com",
		databaseURL: "https://labo2-nickboon-23.firebaseio.com",
		projectId: "labo2-nickboon-23",
		storageBucket: "labo2-nickboon-23.appspot.com",
		messagingSenderId: "418072054040"
      };
      firebase.initializeApp(this.config);
      let database = firebase.database();
      
      $('#form').on('submit', function(){
			var x = document.getElementById("form");
			var text = "";
			var i;
			for (i = 0; i < x.length ;i++) {
				text += x.elements[i].value + "<br>";
			}
			return text;
      });

      this.row = 8;
      this.col = 8;
      this.size = 40;
      this.blue = "(0, 0, 255)"
      this.black = "(0, 0, 0)"

      // Cache Div Element
      this.ledContainerElement = document.querySelector('.ledContainer');

      this.createCharacterArcadeMatrix(this.row, this.col);
    },

    createCharacterArcadeMatrix: function (row, col) {
      let pattern = '';
      let led = '';

      // Generate bit-string
      for (i = 0; i < row; i++) {
        let tempStr = '';
        for (j = 0; j < col / 2; j++) {
          // Randomly generate 1 or 0
          tempStr += Math.round(Math.random());
        }
        // Add tempStr + reversre tempStr to pattern
        pattern += tempStr + tempStr.split("").reverse().join("");
        console.log(pattern)
      }

      // Render LEDs
      for (i = 0; i < row; i++) {
        for (j = 0; j < col; j++) {
          let bit = pattern.charAt((i * this.row) + j);
          let ledClass = (bit == 1) ? 'led--on' : 'led--off';
          let top = i * this.size;
          let left = j * this.size;
          led += `<div style="top:${top}px; left:${left}px; width:${this.size}px; height:${this.size}px" class="led ${ledClass}"></div>`;
          this.ledContainerElement.innerHTML = led;
        }
      }
      firebase.database().ref('current_character').set(pattern);
      firebase.database().ref('cols').set(this.col);
      firebase.database().ref('rows').set(this.row);
    }
  }
  app.init();
})();

// from data.js
var tableData = data;



var datetime = tableData.map(function (ufos) {
    return ufos.datetime;
});

var city = tableData.map(function (ufos) {
    return ufos.city;
});

var state = tableData.map(function (ufos) {
    return ufos.state;
});

var country = tableData.map(function (ufos) {
    return ufos.country;
});

var shape = tableData.map(ufos => ufos.shape);


var duration = tableData.map(ufos => ufos.durationMinutes);


var comments = tableData.map(ufos => ufos.comments);

///https://www.w3schools.com/js/tryit.asp?filename=tryjs_array_loop_foreach  For each loop

///<p id="demo"></p>

   /// <script>
      ///  var fruits, text;
       /// fruits = ["Banana", "Orange", "Apple", "Mango"];

///text = "<ul>";
   ///     fruits.forEach(myFunction);
///text += "</ul>";
///document.getElementById("demo").innerHTML = text;

///function myFunction(value) {
  ///          text += "<li>" + value + "</li>";
///}
////</script>


///Standard loop
///<p id="demo"></p>

   /// <script>
      ///  var fruits, text, fLen, i;
      ///  fruits = ["Banana", "Orange", "Apple", "Mango"];
        ////fLen = fruits.length;

////text = "<ul>";
/////for (i = 0; i < fLen; {
     ///           text += "<li>" + fruits[i] + "</li>";
///}
///text += "</ul>";

///document.getElementById("demo").innerHTML = text;
////</script>




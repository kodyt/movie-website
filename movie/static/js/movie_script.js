//Rating Slider
var ratingSlider = document.getElementById("ratingSlider")
var ratingValue = document.getElementById("rating")
ratingValue.innerHTML = ratingSlider.value

ratingSlider.oninput = () => {
  ratingValue.innerHTML = ratingSlider.value;

}

//Min Slider
var minSlider = document.getElementById("minSlider");
var minYear = document.getElementById("minYear");
minYear.innerHTML = minSlider.value; // Display the default slider value
//Max Slider
var maxSlider = document.getElementById("maxSlider");
var maxYear = document.getElementById("maxYear");


// Update the current slider value (each time you drag the slider handle)
minSlider.oninput = function() {
  minYear.innerHTML = minSlider.value;
}



maxYear.innerHTML = maxSlider.value; // Display the default slider value

// Update the current slider value (each time you drag the slider handle)
maxSlider.oninput = function() {
  maxYear.innerHTML = maxSlider.value;
}

// User has to pick a genre
function handleFormSubmission(event){
  event.preventDefault();

  const genreInput = document.getElementById('genre')
  if (genreInput.value === ''){
    alert('Please choose a genre.');
    return;
  }

  event.target.submit();
}
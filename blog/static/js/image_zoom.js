var modal = document.getElementById("myModal");

// Get the image and insert it inside the modal - use its "alt" text as a caption
var img = document.getElementById("myImg");
var modalImg = document.getElementById("img01");
var captionText = document.getElementById("caption");

const images = document.querySelectorAll('input[type="img"]')

images.forEach(image => {
  image.addEventListener('click', aye)})


img.onclick = function(){
  modal.style.display = "block";
  console.log("aye");
  modalImg.src = this.src;
  // modalImg.style.width = "40vw";
  captionText.innerHTML = this.alt;


  // const images = document.querySelectorAll('input[type="img"]')

  // images.forEach(image => {
  // image.addEventListener('click', aye)})
}

function aye() {
  console.log("aye");
}

// Get the <span> element that closes the modal
var span = document.getElementsByClassName("close")[0];

// When the user clicks on <span> (x), close the modal
span.onclick = function() {
  modal.style.display = "none";
}
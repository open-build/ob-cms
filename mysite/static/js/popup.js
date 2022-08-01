//with this first line we're saying: "when the page loads (document is ready) run the following script"
$(document).ready(function () {
    //select the POPUP FRAME and show it
    $("#popup").hide().fadeIn(1000);

    //close the POPUP if the button with id="close" is clicked
    $("#close").on("click", function (e) {
        e.preventDefault();
        $("#popup").fadeOut(1000);
    });
});
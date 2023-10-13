$(document).ready(function() {
    $("#login-form").submit(function(event) {
      event.preventDefault(); // Prevent the default form submission

      // Get input values
      var email = $("#email").val();
      var password = $("#password").val();

      // Validate input
      if (email === "" || password === "") {
         $("#login-message").text("Please fill in all fields.");
                } 
      else {
      // Get the form data
      var formData = {
        email: email,
        password: password
      };

      // Send a POST request to the Flask endpoint
      $.ajax({
        type: "POST",
        url: "/login",  // Flask endpoint URL
        data: formData,
        dataType: "json",
        success: function(response) {
          // Check the login response
          if (response.message === "Login successful") {
            // Display a success message to the user
            $("#login-message").text("Login successful!");
          } else {
            // Display a failure message to the user
            $("#login-message").text("Login failed. Please check your credentials.");
          }
        },
        error: function(error) {
          // Handle any errors here
          console.error("Ajax request error:", error);
        }
      });
    }
    });
  });
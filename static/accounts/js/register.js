$("#regButton").on('click', function() {  
    //username
    var uName = $("#id_username").val();
    var uName_len = 0;
    //password
    var pass = $("#id_password").val();
    //email
    var email = $("#id_email").val();
    var email_len = 0;
    //other fields
    var first_name = $("#id_first_name").val();
    var last_name = $("#id_last_name").val();
    var component = $("#id_component").val();

    var checkTerms = function(){
      if($("#terms_conditions").is(":checked") === false){
        $("#term").css("color", "red");
        return 1
      }else{}

    }

    var checkUname_mail = function(field, init_len, p_e_name) {

      //pass error class to username
      if (init_len > 0) {
          return 1;
      } else if (field.length === 0) {
          $("#p_" + p_e_name).addClass("has-error");
          $("#error_fields").show();
          return 1;
      } else {
          $("#p_" + p_e_name).removeClass("has-error");
          $("#error_" + p_e_name).hide();
          return 0;
      };
    };

    var checkPass = function(pass) {
      //pass error class to password
      if (pass.length < 8 && pass.length != 0) {
        $("#p_password").addClass("has-error");
        $("#error_password").show();
        return 1;

      }else if (pass.length === 0) {
          $("#p_password").addClass("has-error");
          $("#error_fields").show();
          return 1;

      }else {
        $("#p_password").removeClass("has-error");
        $("#error_password").hide();
        return 0;
      };
    };

    var checkEmptyFields = function(value, p_name) {
      if (value.length === 0) {
        $("#p_" + p_name).addClass("has-error");
        $("#error_fields").show();
        return 1;
      } else {
        $("#p_" + p_name).removeClass("has-error");
        $("#error_fields").hide();
        return 0;
      }
    };
    $.when(uName, pass, email).done(function() {
      var one = checkUname_mail(uName, uName_len, "username");
      var three = checkPass(pass);
      var five = checkEmptyFields(first_name, "first_name");
      var six = checkEmptyFields(last_name, "last_name");
      var twelve = checkEmptyFields(component, "component");
      var total = one + three + five + twelve ;
    });
  });
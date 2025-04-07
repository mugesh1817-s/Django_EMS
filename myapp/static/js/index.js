$(document).ready(function() {
    $("#submit").click(function () {
        var user_id = $("#user_id").val();
        var employeename = $("#employeename").val();
        var lastname =$("#lastname").val();
        var employeeid = $("#employeeid").val();
        var gmail =$("#gmail").val();
        var age =$("age").val();
        var date = $("#date").val();
        var gender =$("#gender").val();
        var mobile =$("#mobile").val();
        var department = $("#department").val();
        var qualification = $("#qualification").val();
        var fathername=$('#fathername').val();
        var mothername=$('#mothername').val();
        var fathercontact=$('#fathercontact').val();
        var address=$('#address').val();
        var city=$('#city').val();
        var state=$('#state').val();
        var country=$('#country').val();
        var status = $("#status").val();
        var workdepartment=$('#workdepartment').val();
        var experience = $('#experience').val();
        var worklocation=$('#worklocation').val();
        var salary = $('#salary').val();
        var joindate=$('#joindate').val();
        var shifttime=$('#shifttime').val();
        var employeetype=$('#employeetype').val();
      
        // var startdate=$('#startdate').val();
        // var enddate=$('#enddate').val();
        // var requestday=$('#requestday').val();
        // var indate = $("#indate").val();
        // var intime=$('#intime').val();
        // var outtime=$('#outtime').val();
        

        if (!employeename || !employeed || !lastname || !gmail || !department || !date || !salary) {
            alert("Please fill all fields");
        }
        else{
             $.ajax({
                url: 'create2/',
                type: 'POST',
                data: {
                    employeename : employeename,
                    lastname : lastname,
                    employeeid : employeeid,
                    gmail : gmail,
                    age : age,
                    date : date,
                    gender : gender,
                    mobile : mobile,
                    department : department,
                    qualification : qualification,
                    fathername : fathername,
                    mothername : mothername,
                    fathercontact : fathercontact,
                    address :address,
                    city : city,
                    state : state,
                    country : country,
                    status : status,
                    workdepartment : workdepartment,
                    experience:experience,
                    worklocation : worklocation,
                    salary : salary,
                    joindate : joindate,
                    shifttime : shifttime,
                    employeetype : employeetype,
                    // startdate : startdate,
                    // enddate : enddate,
                    // requestday : requestday,   
                    // indate : indate,
                    // intime:intime,
                    // outtime:outtime,
                    csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
                },
                success : function(){
                    Read();
                    $("#employeename").val('');
                    $("#lastname").val('');
                    $("#employeeid").val('');
                    $("#gmail").val('');
                    $("#age").val('');
                    $("#date").val('');
                    $("#gender").val('');
                    $("#mobile").val('');
                    $("#department").val('');
                    $("#qualification").val('');
                    $("#fathername").val('');
                    $("#mothername").val('');
                    $("#fathercontact").val('');
                    $("#address").val('');
                    $("#city").val('');
                    $("#state").val('');
                    $("#country").val('');
                    $("#status").val('');
                    $("#workdepartment").val('');
                    $("#experience").val('');
                    $("#worklocation").val('');
                    $("#salary").val('');
                    $("#joindate").val('');
                    $("#shifttime").val('');
                    $("#employeetype").val('');
                    // $("#startdate").val('');
                    // $("#enddate").val('');
                    // $("#requestday").val('');
                    // $("#indate").val('');
                    // $("#intime").val('');
                    // $("#outtime").val('');
                    alert("Your response send successfully")                      
                }
             });
        }    
    });         
});

///update code ////
$(document).ready(function () {
    $("#update").click(function (event) {
        event.preventDefault();  // ✅ Prevent default form submission

        var user_id = $("#user_id").val();  // Get Employee ID

        if (!user_id) {
            alert("User ID is missing!");
            return;
        }

        $.ajax({
            url: `/update_employee/${user_id}/`,  // ✅ Ensure correct URL format
            type: 'POST',
            data: {
                employeename: $("#employeename").val(),
                lastname: $("#lastname").val(),
                employeeid: $("#employeeid").val(),
                gmail: $("#gmail").val(),
                age: $("#age").val(),
                date: $("#date").val(),
                gender: $("#gender").val(),
                mobile: $("#mobile").val(),
                department: $("#department").val(),
                qualification: $("#qualification").val(),
                fathername: $("#fathername").val(),
                mothername: $("#mothername").val(),
                fathercontact: $("#fathercontact").val(),
                address: $("#address").val(),
                city: $("#city").val(),
                state: $("#state").val(),
                country: $("#country").val(),
                status: $("#status").val(),
                workdepartment: $("#workdepartment").val(),
                experience: $("#experience").val(),
                worklocation: $("#worklocation").val(),
                salary: $("#salary").val(),
                joindate: $("#joindate").val(),
                shifttime: $("#shifttime").val(),
                employeetype: $("#employeetype").val(),
                csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
            },
            success: function () {
                alert("Employee updated successfully!");  // ✅ Show success alert
                window.location.reload();  // ✅ Reload the same page (emppersonal.html)
            },
            error: function () {
                alert("Error updating employee data.");  // ✅ Show error alert
            }
        });
    });
});

function Read(){
  $.ajax({
    url: 'read2/',
    type: 'POST',
    async: false,
    data : {
        res: 1,
        csrfmiddlewaretoken : $('input[name=csrfmiddlewarwtoken]').val()
    },
    success : function(response){
        $('#cobnt').html(response);
    }
  });
}

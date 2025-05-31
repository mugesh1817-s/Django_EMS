$(document).ready(function() {
    $("#submit").click(function () {
        var employeename = $("#employeename").val();
        var employeeid = $("#employeeid").val();
        var department = $("#department").val();
        var bankname=$('#bankname').val();
        var bankbranch=$('#bankbranch').val();
        var accountnumber=$('#accountnumber').val();
        var bankcode=$('#bankcode').val();
        var branchaddress=$('#branchaddress').val();

        if (!bankname || !bankbranch || !accountnumber || !bankcode || !branchaddress ) {
            alert("Please fill all fields");
        }
        else{
             $.ajax({
                url: 'create3/',
                type: 'POST',
                data: {
                    employeename:employeename,
                    employeeid : employeeid,
                    department: department,
                    bankname : bankname,
                    bankbranch : bankbranch,
                    accountnumber : accountnumber,
                    bankcode : bankcode,
                    branchaddress : branchaddress,
                    csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
                },
                success : function(){
                    Read();
                    $("#employeename").val('');
                    $("#employeeid").val('');
                    $("#department").val('');
                    $("#bankname").val('');
                    $("#bankbranch").val('');
                    $("#accountnumber").val('');
                    $("#bankcode").val('');
                    $("#branchaddress").val('');
                    alert("Your response send successfully")                      
                }
             });

        }
           
       
    });         
});

//Update code 

// Delete

function Read(){
  $.ajax({
    url: 'read3/',
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

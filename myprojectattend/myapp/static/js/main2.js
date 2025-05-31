$(document).ready(function() {
    $("#submit").click(function () {
        var employeename = $("#employeename").val();
        var employeeid = $("#employeeid").val();
        var department = $("#department").val();
        var startdate = $("#startdate").val();
        var enddate = $("#enddate").val();
        var requestday = $("#requestday").val();
       

        if (!employeename || !employeeid || !department ||  !startdate || !enddate || !requestday) {
            alert("Please fill all fields");
        }
        else{
             $.ajax({
                url: 'create4/',
                type: 'POST',
                data: {
                    employeename:employeename,
                    employeeid : employeeid,
                    department: department,
                    startdate: startdate,
                    enddate : enddate,
                    requestday : requestday,  
                    csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
                },
                success : function(){
                    Read();
                    $("#employeename").val('');
                    $("#employeeid").val('');
                    $("#department").val('');
                    $("#startdate").val('');
                    $("#enddate").val('');
                    $("#requestday").val('');
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
    url: 'read4/',
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

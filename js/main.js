    $(document).ready(function() {
        $("#submit").click(function () {
            var employeename = $("#employeename").val();
            var employeeid = $("#employeeid").val();
            var department = $("#department").val();
            var mobile =$("#mobile").val();
            var indate = $("#indate").val();
            var intime = $("#intime").val();
            var outtime = $("#outtime").val();
           

            if (!employeename || !employeeid || !department || !mobile || !indate || !intime || !outtime) {
                alert("Please fill all fields");
            }
            else{
                 $.ajax({
                    url: 'create/',
                    type: 'POST',
                    data: {
                        employeename:employeename,
                        employeeid : employeeid,
                        department: department,
                        mobile : mobile,
                        indate: indate,
                        intime : intime,
                        outtime : outtime,  
                        csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
                    },
                    success : function(){
                        Read();
                        $("#employeename").val('');
                        $("#employeeid").val('');
                        $("#department").val('');
                        $("#mobile").val('');
                        $("#indate").val('');
                        $("#intime").val('');
                        $("#outtime").val('');
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
        url: 'read/',
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

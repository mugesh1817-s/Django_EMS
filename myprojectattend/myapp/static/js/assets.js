$(document).ready(function() {
    $("#submit").click(function () {
        var employeename = $("#employeename").val();
        var assets = $("#assets").val();
        var assetname = $("#assetname").val();
        var assigndate = $("#assigndate").val();
        var batchno = $("#batchno").val();
        var assignby = $("#assignby").val();
       

        if (!employeename || !assets || !assetname ||  !assigndate || !batchno || !assignby) {
            alert("Please fill all fields");
        }
        else{
             $.ajax({
                url: 'create5/',
                type: 'POST',
                data: {
                    employeename:employeename,
                    assets : assets,
                    assetname: assetname,
                    assigndate: assigndate,
                    batchno : batchno,
                    assignby : assignby,  
                    csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
                },
                success : function(){
                    Read();
                    $("#employeename").val('');
                    $("#assets").val('');
                    $("#assetname").val('');
                    $("#assigndate").val('');
                    $("#batchno").val('');
                    $("#assignby").val('');
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
    url: 'read5/',
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

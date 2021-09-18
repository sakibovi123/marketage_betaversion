
$('[name="obtmarks[]"]').keyup(function(){
    if(parseInt($(this).val()) > 5){
        $('#div1').html('value cannot be greater then 5');
        $(this).val('');
    }
    else if(parseInt($(this).val()) < 1)
    {
    $('#div1').html('value cannot be lower then 1');
        $(this).val('');
    }
    else
    {$('#div1').html('');}
});
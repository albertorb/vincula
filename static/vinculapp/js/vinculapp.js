/* user image preview on form*/

function readURL(input) {

    if (input.files && input.files[0]) {
        var reader = new FileReader();

        reader.onload = function (e) {
            $('#preview').attr('src', e.target.result);
        }

        reader.readAsDataURL(input.files[0]);
    }
}
$(".filestyle").change(function(){
    	readURL(this);
	});

$(readURL($('#image')));

/* end user image preview on form */

/* input image style */

$('input[type=file]').bootstrapFileInput();
$('.file-inputs').bootstrapFileInput();

/* end input image style */
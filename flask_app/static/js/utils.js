String.prototype.format = String.prototype.f = function() {
    var s = this,
    i = arguments.length;

    while (i--) {
        s = s.replace(new RegExp('\\{' + i + '\\}', 'gm'), arguments[i]);
    }
    return s;
};

function setAjaxFormHandlers(data){
    var form = data.form;
    var minResponseTime = data.minResponseTime;
    var confirmMessage = data.confirmMessage;
    var submit = data.submit;
    var success = data.success;
    var error = data.error;

    form.submit(function(event){
        if(confirmMessage){
            var c = confirm(confirmMessage);
            if(!c){
                return false;
            }
        }
        if(!minResponseTime){
            minResponseTime = 0;
        }
        submit();
        form.clickTime = (new Date()).getTime();
        $.ajax({
            url: form.attr("action"),
            type: form.attr("method"),
            data: form.serialize(),
            async: true,
            success: function(){
              var postReturnTime = (new Date()).getTime();
              var delay = minResponseTime-(postReturnTime-form.clickTime);
              setTimeout(success, delay);
            },
            error: function(){
              var postReturnTime = (new Date()).getTime();
              var delay = minResponseTime-(postReturnTime-form.clickTime);
              setTimeout(error, delay);
            }
        })
        event.preventDefault();
        return true;
    });
};
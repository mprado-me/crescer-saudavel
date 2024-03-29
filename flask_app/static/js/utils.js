DEFAULT_RESPONSE_TIME = 500;

String.prototype.format = String.prototype.f = function () {
    var s = this,
        i = arguments.length;

    while (i--) {
        s = s.replace(new RegExp('\\{' + i + '\\}', 'gm'), arguments[i]);
    }
    return s;
};

function setAjaxFormHandlers(data) {
    var form = data.form;
    var minResponseTime = data.minResponseTime;
    var confirmMessage = data.confirmMessage;
    var dataType = data.dataType;
    var submit = data.submit;
    var success = data.success;
    var error = data.error;
    var complete = data.complete;

    form.submit(function (event) {
        if (confirmMessage) {
            var c = confirm(confirmMessage);
            if (!c) {
                return false;
            }
        }
        if (!minResponseTime) {
            minResponseTime = 0;
        }
        submit();
        form.clickTime = (new Date()).getTime();
        $.ajax({
            url: form.attr("action"),
            type: form.attr("method"),
            data: form.serialize(),
            dataType: dataType,
            async: true,
            success: function (data) {
                var postReturnTime = (new Date()).getTime();
                var delay = minResponseTime - (postReturnTime - form.clickTime);
                setTimeout(function () {
                    success(data);
                    if(complete){
                        complete();
                    }
                }, delay);
            },
            error: function (jqXHR) {
                var postReturnTime = (new Date()).getTime();
                var delay = minResponseTime - (postReturnTime - form.clickTime);
                setTimeout(function () {
                    error(jqXHR.status);
                    if(complete){
                        complete();
                    }
                }, delay);
            }
        });
        event.preventDefault();
        return true;
    });
}

function disableInputGroup(root, groupClass) {
    root.find("input.{0}".f(groupClass)).each(function () {
        $(this).prop("disabled", true);
    })
}

function enableInputGroup(root, groupClass) {
    root.find("input.{0}".f(groupClass)).each(function () {
        $(this).prop("disabled", false);
    })
}

function throwSuccessOpToast(message) {
    toastr.options.closeButton = false;
    toastr.options.timeOut = 3500;
    toastr.success(message);
}

function throwErrorOpToast(message) {
    toastr.options.closeButton = true;
    toastr.options.timeOut = 10000;
    toastr.error(message);
}

function updateTableData(colId, row, value) {
    $("#col-{0}-row-{1}".f(colId, row)).html(value);
}
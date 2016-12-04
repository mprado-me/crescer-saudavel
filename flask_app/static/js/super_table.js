var show_actions = "Exibir ações <span class='glyphicon glyphicon-menu-down'></span>";
var hide_actions = "Ocultar ações <span class='glyphicon glyphicon-menu-up'></span>";

$(document).ready(function () {
    $('[data-toggle="tooltip"]').tooltip();
    $('form.filter-container input.sort-method').attr("value", $('select.sort-method').val());
});

$("button.expand-actions").on('click', function () {
    var actionButton = $(this);
    var collapsibleRow = $("#{0}".f(actionButton.attr("target_id")));
    if( collapsibleRow.is(":visible") ){
        actionButton.html(show_actions)
    }
    else {
        actionButton.html(hide_actions)
    }
    collapsibleRow.toggle(150);
});

$(".filter-item select").each(function(){
    selectField = $(this);
    label = selectField.siblings("label");
    selectField.css("min-width", "{0}px".f(label.width()+10));
});


$('select.sort-method').on('change', function () {
    select = $(this);
    $('form.filter-container input.sort-method').attr("value", select.val());
    $("form.filter-container input[type='submit']").click();
});
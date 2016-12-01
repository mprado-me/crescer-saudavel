$(document).ready(function () {
    $('[data-toggle="tooltip"]').tooltip();
    $('form.filter-container input.sort-method').attr("value", $('select.sort-method').val());

});

$(".collapsible-row").each(function () {
    var collapsibleRow = $(this);
    var actionButton = $("#{0}".f(collapsibleRow.attr("action-btn-id")));
    collapsibleRow.on('hide.bs.collapse', function () {
        actionButton.html("Exibir ações <span class='glyphicon glyphicon-menu-down'></span>")
    });
    collapsibleRow.on('show.bs.collapse', function () {
        actionButton.html("Ocultar ações <span class='glyphicon glyphicon-menu-up'></span>")
    });
});

$(".filter-item select").each(function(){
    selectField = $(this);
    label = selectField.siblings("label");
    selectField.css("min-width", "{0}px".f(label.width()+10));
});


$('select.sort-method').on('change', function () {
    select = $(this);
    console.log(select.val());
    $('form.filter-container input.sort-method').attr("value", select.val());
    $("form.filter-container input[type='submit']").click();
});
$(document).ready(function () {
    $('[data-toggle="tooltip"]').tooltip();
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
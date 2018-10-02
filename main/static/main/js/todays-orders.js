$(document).ready(function () {
    
    $('#orders-submenu')
        .show()
        .children().children(':first').addClass('active');
    
});

$(document).on('click', '.order-modal-btn', function (e) {
    
    var btn = $(this),
        order = orders[Number.parseInt(btn.parent().parent().data('pk'))];
        
    var element = ``;
    
    $.each(order.items, function (index, item) {
        element += `
        <h3>x${ item.count } ${ item.name }<span style="float:left">${ item.cost.toFixed(2) } جنيه</span></h3>
        `;
    });
    
    element += `
    <hr><h3>الاجمالى<span style="float:left">${ order.total_cost.toFixed(2) } جنيه</span></h3>
    `;
    
    $('#order-body').html(element);
    
});

$(document).on('click', '.remove-order-item', function (e) {
    
    var pk = $(this).attr('data-pk'),
        parent = $(this).parent().parent(),
        serialNumber = parent.children(':first').text();
    
    $.ajax({
        url: 'ajax/remove-order/',
        data: {
            pk: pk
        },

        success: function (data) {

            parent.fadeOut(300, function () {
                $(this).remove();
            });

            iziToast.success({
                title: 'نجاح',
                message: 'تمت الحذف بنجاح',
                position: 'topRight',
                zindex: 99999
            });

        }
    });  
});
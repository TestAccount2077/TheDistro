$(document).on('click', '#add-client-btn', function (e) {
    
    var name = $('#name').val(),
        phone = $('#phone').val(),
        address = $('#address').val(),
        order = $('#order').val();
    
    if (!name || !phone || !address || !order) {
        
        iziToast.error({
            title: 'خطأ',
            message: 'يرجى ملأ الحقول الخالية',
            position: 'topRight',
            zindex: 99999
        });
        
        return;
        
    }
    
    var data = {
        name,
        phone,
        address,
        order
    };
    
    $.ajax({
        url: 'ajax/add-client/',
        data: data,
        success: function (data) {
            
            iziToast.success({
                title: 'نجاح',
                message: 'تمت الاضافة بنجاح',
                position: 'topRight',
                zindex: 99999
            });
            
            $('#add-client-modal').modal('hide');
            
            var client = data.client,
                element = `
                <tr data-pk="${ client.pk }">
                    <td>${ client.name }</td>
                    <td>${ client.phone }</td>
                    <td>${ client.address }</td>
                    <td>${ client.order }</td>
                    <td></td>
                    <td><img src="static/images/remove.png" class="icon remove-client-item" data-pk="${ client.pk }"></td>
                </tr>
            `;
            
            var lastElement = $('#client-table tbody tr:last')
            
            lastElement.remove();
            
            $('#client-table tbody').append(element);
            $('#client-table tbody').append(lastElement);
            
        }
    });
    
});

$(document).ready(function () {
    
    $('#orders-submenu')
        .show()
        .children().children(':nth-child(2)').addClass('active');
    
    $('#new-order-modal').modal({backdrop: 'static', keyboard: false});
    $('#new-order-modal').modal('show');
    
});

$(document).on('click', '#inquire-client-btn', function (e) {
    
    var phone = $('#phone').val();
    
    if (!phone) {
        
        iziToast.error({
            title: 'خطأ',
            message: 'هذا الحقل مطلوب',
            position: 'topRight',
            zindex: 99999
        });
        
        return;
        
    }
    
    $.ajax({
        url: '/ajax/inquire-client/',
        data: {
            phone
        },
        
        success: function (data) {
            
            $('#name, #address, #menu-a').slideDown();
            $('#menu-a').css('display', 'block');
            
            if (data.not_found) {
                
                iziToast.info({
                    title: 'معلومات',
                    message: 'هذا العميل غير موجود. يرجى اضافة بياناته',
                    position: 'topRight',
                    zindex: 99999
                });
                
            }
            
            else {
                
                iziToast.info({
                    title: 'معلومات',
                    message: 'هذا العميل موجود. يرجى مراجعة طلباته السابقة لتحسين الخدمة',
                    position: 'topRight',
                    zindex: 99999
                });
                
                $('#name').val(data.client.name);
                $('#address').val(data.client.address);
                
            }
        }
    });
    
});

$(document).on('click', '#menu-a', function () {
    
    var name = $('#name').val(),
        phone = $('#phone').val(),
        address = $('#address').val();
    
    var url = `/order-menu/?name=${ name }&phone=${ phone }&address=${ address }`;
    
    location.href = url;
    
});

$(document).on('click', '#create-order', function() {
    
    $.ajax({
        
        url: '/ajax/create-order/',
        
        data: {
            items: JSON.stringify(items),
            data: JSON.stringify(data)
        },
        
        success: function (data) {
            
            socket.send(JSON.stringify(data));
            
            iziToast.success({
                title: 'نجاح',
                message: 'تم عمل الأوردر بنجاح',
                position: 'topRight',
                zindex: 99999
            });
            
            $('#name, #address, #menu-a, #order-list').slideUp();
            
            $('#name, #phone, #address').val('');
            
            $('#create-order')
                .attr('id', 'inquire-client-btn')
                .text('استعلام')
                .removeClass('btn-success')
                .addClass('btn-primary');
            
        }
    });
});

$(document).on('keypress', '#phone', function (e) {
    
    if (e.which === 13 && !$('#name').is(':visible')) {
        $('#inquire-client-btn').click();
    }
    
});
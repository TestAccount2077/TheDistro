$(document).ready(function () {
    
    
});

$(document).on('click', '#proceed', function (e) {
    
    var counts = 0,
        invalidCount = 0,
        items = [];
    
    $('.item-name').each(function () {
        
        var element = $(this),
            name = element.text(),
            count = element.next().val();
        
        if (!isNumeric(count)) {
            
            counts++;
            invalidCount++;
            
        }
        
        else if (count) {
            
            items.push({
                name,
                count
            });
            
            counts++;
            
        }
        
    });
    
    console.log(counts, invalidCount)
    
    if (!counts) {
        
        iziToast.error({
            title: 'خطأ',
            message: 'يجب اختيار صنف واحد على الأقل',
            position: 'topRight',
            zindex: 99999
        });
        
        return;
        
    }
    
    if (invalidCount) {
        
        iziToast.error({
            title: 'خطأ',
            message: 'العدد يجب أن يكون رقميا',
            position: 'topRight',
            zindex: 99999
        });
        
        return;
    }
    
    var url = `/new-order/?items=${ JSON.stringify(items) }&data=${ JSON.stringify(REQUEST_DATA) }`;
    
    location.href = url;
    
});
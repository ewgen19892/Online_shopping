$(document).ready(function(){
    var form = $('#form_buying_product');


    function basketUpdating(product_id, nmb, url, is_delete) {
        var data = {};
        data.product_id = product_id;
        data.nmb = nmb;
        var csrf_token = $('.wrapper-content [name="csrfmiddlewaretoken"]').val();
        data["csrfmiddlewaretoken"] = csrf_token;

        if (is_delete)
            data['is_delete'] = true;
        var url = url;
        // var url = form.attr("action");
        $.ajax({
            url: url,
            type: 'POST',
            data: data,
            cache: true,
            success: function (data) {
                console.log('OK');
                $('#basket_total_amount').text('('+data.products_total_price+')'+'USD');
                cls = '.product_in_basket_'+product_id;
                $(cls).html('');
                $('#total_order_amount').text(data.products_total_price+' USD');
                    // $('.basket-items ul').html("");
                    // $.each(data.products, function(k, v){
                    //     $('.basket-items ul').append('<li>' +v.name+' * '+ v.nmb + ' = ' + v.total_price + ' USD  ' +
                    //         '<a class="delete-item" href="" data-product_id="'+v.id+'">x</a>'+
                    //         '</li>');
                    // })
                // }
                if (data.products_total_price == undefined){
                       $('#basket_total_amount').text('('+0+')'+'USD');
                       $('#total_order_amount').text(0+' USD');
                }
            },
            error: function(){
                console.log('error')
            }
        });
    }

    form.on('submit', function(e){
        console.log('from product');
        e.preventDefault();
        var nmb = $('#number').val();
        var submit_btn = $('#submit_btn');
        var product_id = submit_btn.data("product_id");
        var url = form.attr("action");
        // var product_price = submit_btn.data('price');
        // var sum_product_price = product_price * nmb;
        // var products_total_price = submit_btn.data('products_total_price');

        basketUpdating(product_id, nmb, url, is_delete=false)

    });

    $(document).on('submit','#add_to_basket_product', function(e){
        console.log('from home');
        e.preventDefault();
        var submit_btn = $('#submit_btn');
        var product_id = $(this).data('product_id');
        // var product_id = submit_btn.data("product_id");
        // var product_id = submit_btn.$(this).data("product_id");
        var nmb = submit_btn.data("nmb");
        var url = $('#add_to_basket_product').attr("action");

        basketUpdating(product_id, nmb, url, is_delete=false);

    });

    // function showingBasket() {
    //     $('.basket-items').removeClass('hidden')
    // }

    // $('.basket-container').on('click', function(e){
    //     e.preventDefault();
    //     $('.basket-items').removeClass('hidden');
    // });
    //
    // $('.basket-container').mouseover(function(){
    //     $('.basket-items').removeClass('hidden');
    // });

    // $('.basket-container').mouseout(function(){
    //     $('.basket-items').addClass('hidden');
    // });

    $(document).on('click', '.delete-item', function(e){
        e.preventDefault();
        product_id = $(this).data('product_id');
        nmb = 0;
        url = '/basket_adding/';
        // var submit_btn = $('#submit_btn');
        // var products_total_price = submit_btn.data('products_total_price');
        basketUpdating(product_id, nmb, url, is_delete=true)
    });


    function calculatingBasketAmount() {
        var total_order_amount = 0;
        $('.total-product-in-basket-amount').each(function () {
            total_order_amount += parseFloat($(this).text());
        });
        $('#total_order_amount').text(total_order_amount.toFixed(2)+' USD');
        $('#basket_total_amount').text('('+total_order_amount.toFixed(2)+')'+'USD');

    }

    $(document).on('change', ".product-in-basket-nmb", function(){
        current_nmb = $(this).val();
        var current_tr = $(this).closest('tr');
        var current_price = parseFloat(current_tr.find('.product-price').text()).toFixed(2);
        var total_amount = parseFloat(current_nmb*current_price).toFixed(2);
        current_tr.find('.total-product-in-basket-amount').text(total_amount);
        calculatingBasketAmount();
    });

    // calculatingBasketAmount();
});
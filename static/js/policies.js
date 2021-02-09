$(document).ready(function () {
    // Adding HTML special characters
    $('#table-policies').find('th').each(function () {
        if ($(this).attr('class') && $(this).attr('class').includes('asc')) {
            $(this).find('a').append('<span> &#11015;</span>');
        } else if ($(this).attr('class') && $(this).attr('class').includes('desc')) {
            $(this).find('a').append($("<span> &#11014;</span>"));
        }
    });

    // Submit and reset use keyup event: Enter and Delete keys.
    $('#policies-filter').find('input').on('keyup', function (event) {
        // Cancel the default action
        event.preventDefault();
        if (event.keyCode === 13) {
            $('#policies-filter').find(':submit').click()
        } else if (event.keyCode === 46) {
            $('#policies-filter').find(':reset').click()
        }
    })

    // Reset (Clear inputs)
    $('#policies-filter').find(':reset').on('click', function (e) {
        e.preventDefault();
        $('#policies-filter').find(':input[type="number"]').val('');
        $('#policies-filter').find(':input[type="text"]').val('');
    })
});

// Update sms message dialog
$("#update-sms-dialog-customer, #update-sms-dialog-number, #update-sms-dialog-end-date").on('change input',
    function () {
        const policy = {
            customer: $('#update-sms-dialog-customer').val(),
            number: $('#update-sms-dialog-number').val(),
            end_date: $('#update-sms-dialog-end-date').val()
        }
        const formats = gettext("%(customer)s, insurance policy %(number)s expires on %(end_date)s");
        let messageText = interpolate(formats, policy, true);
        $('#update-sms-dialog-message-sms').val(messageText)
    })

// From Django doc
function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

const csrftoken = getCookie('csrftoken');
const urlMessageCreate = $('#message-sms-url').attr('data-url');

function getDataAjax(url) {
    let result = '';
    $.ajax({
        method: 'GET',
        url: url,
        async: false
    })
        .done(function (data) {
            result = data;
        })
        .fail(function (data) {
            result = data;
            console.log("error");
        })
    return result;
}

function bsmodals_custom_confirm(title, msg_body, msg_extra, callback, callback_update, yes_text = gettext("Yes"),
                                 yes_style = "btn-primary", no_text = gettext("No"), no_style = "btn-secondary",
                                 update_text = gettext("Update"), update_style = "btn-danger") {
    // displays the confirm modal box with the given title and message
    let modal = $('#custom-confirm-dialog');
    modal.find('#custom-confirm-dialog-title').html(title);
    modal.find('#custom-confirm-dialog-msg-body').html(msg_body);
    modal.find('#custom-confirm-dialog-msg-extra').html(msg_extra);
    modal.find('#custom-confirm-dialog-yes').attr('class', 'btn ' + yes_style);
    modal.find('#custom-confirm-dialog-yes').html(yes_text);
    modal.find('#custom-confirm-dialog-no').attr('class', 'btn ' + no_style);
    modal.find('#custom-confirm-dialog-no').html(no_text);
    modal.find('#custom-confirm-dialog-update').attr('class', 'btn ' + update_style);
    modal.find('#custom-confirm-dialog-update').html(update_text);

    // register call backs on Yes/No buttons
    let click_id = 'click.custom-confirm-dialog';
    let button = modal.find('#custom-confirm-dialog-yes')
    button.off(click_id).on(click_id, () => {
        callback(true);
        modal.modal('hide');
    });

    button = modal.find('#custom-confirm-dialog-no')
    button.off(click_id).on(click_id, () => {
        callback(false);
        modal.modal('hide');
    });

    button = modal.find('#custom-confirm-dialog-update')
    button.off(click_id).on(click_id, () => {
        callback(false);
        callback_update(true);
        modal.modal('hide');
    });

    // show dialog
    modal.modal();
}

// Updating the insurance policy
$("table.table > tbody > tr").on('click', 'td', function (event) {
    let yes = '&#9899;';
    let no = '&#10060;';
    let td = $(this);
    let thisTdClass = td.attr('class');
    let resultAfterTheCall = ['is_reinsured', 'is_reinsured_another_company', 'is_impossible_to_call',
        'is_called_will_insure', 'is_called_will_not_insure'];

    let numberPolicy = td.parent('tr').find('td.number').text();

    if (resultAfterTheCall.includes(thisTdClass)) {
        bsmodals_confirm(gettext('Policy') + ' ' + numberPolicy + ' ' + gettext('update'),
            gettext('Are you sure you want to update the policy?'), function (result) {
                if (result) {
                    let dataUrlPolicy = td.parent('tr').attr('data-url');
                    let data = getDataAjax(dataUrlPolicy);

                    data[thisTdClass] = td.find('span').attr('class') !== 'true';

                    $.ajax({
                        method: 'PUT',
                        url: dataUrlPolicy,
                        beforeSend: function (xhr) {
                            xhr.setRequestHeader("X-CSRFToken", csrftoken)
                        },
                        data: data,
                    })
                        .done(function (data, status, jqXHR) {
                            //{ #console.log('jqXHR: ', jqXHR.status); }
                            if (td.find('span').is('.true')) {
                                td.find('span').removeClass('true').addClass('false');
                                td.find('span').empty().append(no);
                            } else {
                                td.find('span').removeClass('false').addClass('true');
                                td.find('span').empty().append(yes);
                            }

                            const formats = gettext("The policy %s was update successfuly!");
                            const text = interpolate(formats, [numberPolicy]);
                            showAlertMessage(text, 'alert-success');
                        })
                        .fail(function (data) {
                            bsmodals_error(data.statusText, "btn-warning");
                        })
                }
            }, yes_text = gettext('YES'), yes_style = 'btn-success', no_text = gettext('NO'), no_style = 'btn-secondary'
        );
    }
});

// Sending SMS message
$("table.table > tbody > tr > td > button.send_sms").on('click', function (event, message) {
    const buttonSendSms = $(this);
    const formats = gettext("%(customer)s, insurance policy %(number)s expires on %(end_date)s");

    let policy = {
        id: buttonSendSms.parents('tr').attr('data-id'),
    }
    if (message) {
        policy.customer = $('#update-sms-dialog-customer').val();
        policy.number = $('#update-sms-dialog-number').val();
        policy.end_date = $('#update-sms-dialog-end-date').val();
        policy.message_sms = message
    } else {
        customer = buttonSendSms.parents('tr').find('td.customer').text();
        customerArr = customer.split(' ');
        policy.customer = customerArr.length === 3 ? customerArr[1] + ' ' + customerArr[2] : customer;

        policy.number = buttonSendSms.parents('tr').find('td.number').text();
        policy.end_date = buttonSendSms.parents('tr').find('td.end_date').text();
        policy.message_sms = interpolate(formats, policy, true)
    }

    $('#update-sms-dialog-close').click(function () {
        buttonSendSms.trigger("click");
    });

    $('#update-sms-dialog-ok').click(function () {
        let msgAfterUpdate = $('#update-sms-dialog-message-sms').val();
        buttonSendSms.trigger('click', msgAfterUpdate);
    });

    bsmodals_custom_confirm(gettext('Send SMS message'), policy.message_sms,
        gettext('Are you sure you want to send the SMS messages?'),
        function (result) {
            if (result) {
                $.ajax({
                    method: 'POST',
                    url: urlMessageCreate,
                    beforeSend: function (xhr) {
                        xhr.setRequestHeader("X-CSRFToken", csrftoken)
                    },
                    data: {
                        "body": policy.message_sms,
                        "insurance_policy": policy.id
                    },
                })
                    .done(function (data, status, jqXHR) {
                            // { #console.log('jqXHR: ', jqXHR.status); # }
                            var text = gettext('The message was sent successfuly') + '!';
                            showAlertMessage(text, 'alert-success');

                            // Adding 1 to quantity SMS
                            var quantity_sms = buttonSendSms.find('span').text();
                            buttonSendSms.find('span').text(parseInt(quantity_sms) + 1)
                            buttonSendSms.find('span').removeClass('badge-light')
                            buttonSendSms.find('span').addClass('badge-success')
                        }
                    )
                    .fail(function (data) {
                        // bsmodals_error(data.statusText, "btn-warning");
                        var text = data.statusText.charAt(0).toUpperCase() + data.statusText.slice(1) + '. ' + gettext("The message wasn't sent") + '!';
                        showAlertMessage(text, 'alert-danger');
                    })
            }
        },
        function () {
            let customConfirmDialog = new FormModal('update-sms-dialog');
            customConfirmDialog.show(policy);
        }
        , yes_text = gettext('OK'), yes_style = 'btn-success', no_text = gettext('CLOSE'), no_style = 'btn-secondary',
        update_text = gettext('UPDATE'), update_style = 'btn-warning'
    );
});

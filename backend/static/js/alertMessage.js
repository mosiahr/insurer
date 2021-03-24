var divMessage = `<div class="alert alert-success alert-dismissible fade show d-block alert-message" data-dismiss="alert" role="alert">
            <text></text>
            <button type="button" class="close" data-dismiss="alert" aria-label="Close">
                <span aria-hidden="true">&times;</span>
            </button>
        </div>`

function changeTopDivMessage(arrAlertMessage, beginTop, addTop) {
    arrAlertMessage.each(function (i, el) {
        const sumTop = beginTop + i * addTop
        $(el).offset({top: sumTop})
    });
}

function showAlertMessage(text, classAlert, beginTop = 60, addTop = 52, timeout=10000) {
    const divMassage = $(divMessage);
    divMassage.find('text').text(text);
    divMassage.addClass(classAlert);

    // Adding an alert message
    $('#wrapper-messages').append(divMassage);

    let arrAlertMessage = $('#wrapper-messages').find('.alert-message');
    changeTopDivMessage(arrAlertMessage, beginTop, addTop);

    // Re change message top
    divMassage.on('closed.bs.alert', function () {
        arrAlertMessage = $('#wrapper-messages').find('.alert-message');
        changeTopDivMessage(arrAlertMessage, beginTop, addTop);
    })

    // An alert message is closing after timeout
    setTimeout(function () {
        arrAlertMessage = $('#wrapper-messages').find('.alert-message');
        changeTopDivMessage(arrAlertMessage, beginTop, addTop);
        divMassage.alert('close')
    }, timeout);
}

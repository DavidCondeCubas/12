odoo.define('crm.lead.contactus.form', require => {

    require('web.core');

    function checkEmail() {
            const re = /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
            if !(re.test(String($('[name="email_from"]').val()).toLowerCase())){
                $('[name="email_from"]').val('');
                alert('Email incorrecto, intentelo nuevamente.')
            }
        }

    $(document).ready(() => {
        $('[name="email_from"]').on('change', checkEmail);
    });

});
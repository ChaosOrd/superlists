var initialize = function (navigator, user, token, urls) {
    $('#id_login').on('click', function () { 
        navigator.id.request();
    });

    navigator.id.watch({
        loggedInUser: user,
        onlogin: function(assertion) {
            var deffered = $.post(
                urls['login'],
                { assertion: assertion, csrfmiddlewaretoken: token }
            );
            deffered.done(function () { window.location.reload(); })
            deffered.fail(function () { navigator.id.logout(); });
        },
        onlogout: function () {}
    });
};

window.Superlists = {
    Accounts: {
        initialize: initialize
    }
};

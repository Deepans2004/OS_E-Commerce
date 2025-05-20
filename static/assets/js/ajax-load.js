$(document).ready(function () {
    const cache = {};

    function loadPage(url) {
        if (cache[url]) {
            // Load from cache
            $('#content-container').html(cache[url]);
            console.log('Loaded from cache:', url);
        } else {
            // AJAX load and cache it
            $.ajax({
                url: url,
                headers: { 'X-Requested-With': 'XMLHttpRequest' },
                success: function (data) {
                    cache[url] = data; // Cache the response
                    $('#content-container').html(data);
                    console.log('Loaded from server:', url);
                },
                error: function () {
                    $('#content-container').html('<p>Error loading page.</p>');
                }
            });
        }
    }

    // Load index content initially (optional)
    loadPage('/');

    // Intercept click on nav links for about/contact and load via AJAX
    $('nav a').on('click', function (e) {
        const href = $(this).attr('href');

        // Prevent full page reload for these pages
        if (href === 'core/about/' || href === 'core/contact/') {
            e.preventDefault();
            loadPage(href);
            // Update browser URL (optional)
            history.pushState(null, '', href);
        }
    });

    // Handle browser back/forward buttons to reload cached content
    window.onpopstate = function () {
        loadPage(location.pathname);
    };
});

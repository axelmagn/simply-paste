define(['jquery'], function($) {
    var getLanguages;

    /**
     *  Wrapper of $.getJSON with success callback for the language
     *  api endpoint
     */
    getLanguages = function(success) {
        return $.getJSON('/api/snippets/languages/', success);
    }

    return {
        "getLanguages": getLanguages
    }
});

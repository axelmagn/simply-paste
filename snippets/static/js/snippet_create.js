/**
 * Module: snippet_create
 *
 * main module loaded for snippet create views
 * provides a javascript interface for creating and pushing snippets
 *
 */
requirejs(["jquery", "util/editor"], function($, editor_util) {
    // init vars
    var snippetPush, 
        remoteSnippet = {}, 
        init,
        elements = {},
        elementPaths,
        getPageElements,
        showSpinner,
        hideSpinner,
        syncPush,
        updateUI,
        getLocalSnippet,
        spinnerSelector = "#loading-spinner",
        languageSelector = "#language-choice",
        popoverSelector = "#snippet-popover",
        editor;

    // location of all the template includes we will use
    elementPaths = {
        'spinner': '/static/html/spinner.html',
        // 'popover': '/static/html/popover.html'
    };

    /**
     * Set up the app on startup
     */
    init = function () {
        // start editor
        editor = editor_util.init("editor");
    }


    /**
     * Push a snippet object to the server
     *
     * TODO: replace hardcoded api endpoints with more dynamic system
     */
    snippetPush = function( snippet ) {
        // TODO: show spinner
        showSpinner();
        $.ajax({
            dataType:   "json",
            url:        "/api/snippets/push/",
            data:       snippet,
            success: function ( data ) {
                // store remote state
                remoteSnippet = data;
                // update ui
                updateUI();
            },
            error: function ( jqXHR, textStatus ) {
                // parse error message
                // show error message
            }, 
            complete: function () {
                // hide spinner
                hideSpinner();
                // sync
                syncPush()
            }
        });
    }
    showSpinner = function () {
        $(spinnerSelector).show();
    };
    hideSpinner = function () {
        $(spinnerSelector).hide();
    };

    /** 
     * Function: getLocalSnippet
     *
     * Parse local snippet object from content
     *
     * Returns:
     *
     *      Object
     */
    getLocalSnippet = function () {
        return {
            'content':    editor.getContent(),
            'language':   $( languageSelector ).val()
        };

    }

    /**
     * Function: getDisplayUrl
     *
     * Get display url
     *
     * Returns: 
     *
     *      string or undefined
     */
    getDisplayUrl = function () {
        return remoteSnippet.display_url;
    }



    /**
     * Function: syncPush
     *
     * Push local content to remote if remote has different content 
     */
    syncPush = function () {
        var localSnippet;

        // compare relevant fields
        localSnippet = getLocalSnippet();
        var synced = true;
        for( var field in localSnippet) {
            localValue = localSnippet[field];
            remoteValue = remoteSnippet[field];
            if ( localValue !== remoteValue ) {
                synced = false;
            }
        }

        // if not synced, push local to remote
        if( synced !== true ) {
            snippetPush( localSnippet );
        }


    };
    updateUI = function () {};

    init();

    
});

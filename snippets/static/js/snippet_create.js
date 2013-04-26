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
        elements,
        syncPush,
        updateUI,
        getLocalSnippet,
        editor;


    /**
     * Set up the app on startup
     *
     */
    init = function () {
        // start editor
        editor = editor_util.init("editor");
        elements = {
            'spinner': $('#loading-spinner'),
            'displayUrl': $('#display-url'),
            'langSelector': $("#lang-selector")
        };
        elements.spinner.hide();
        elements.displayUrl.hide();
        elements.langSelector.hide();
        editor.on("change", function () {
            syncPush();
            updateUI();
        });
    }


    /**
     * Push a snippet object to the server
     *
     * TODO: replace hardcoded api endpoints with more dynamic system
     */
    snippetPush = function( snippet ) {
        // TODO: show spinner
        elements.spinner.show();
        $.ajax({
            type:       "POST",
            dataType:   "json",
            url:        "/api/snippets/push/",
            data:       snippet,
            success: function ( data ) {
                // store remote state
                console.log( data );
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
                elements.spinner.hide();
                // sync
                // syncPush();
            }
        });
    }

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
            'content':    editor.getValue(),
            'language':   elements.langSelector.find('select').val()
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
    updateUI = function () {
        // display url
        displayUrlVal = remoteSnippet.display_url;
        elements.displayUrl.html('<a href="'+displayUrlVal+'">'+displayUrlVal+'</a>');
        if( displayUrlVal !== undefined ) {
            elements.displayUrl.show();
        } else {
            elements.displayUrl.hide();
        }

        // language
        editorContent = editor.getValue();
        if( editorContent !== '' ) {
            elements.langSelector.show();
        } else {
            elements.langSelector.hide();
        }
    };

    init();

    
});

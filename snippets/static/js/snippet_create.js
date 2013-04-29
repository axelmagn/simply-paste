/**
 * Module: snippet_create
 *
 * main module loaded for snippet create views
 * provides a javascript interface for creating and pushing snippets
 *
 */
requirejs(["jquery",    "util/editor",  "util/snippet_api"], 
 function($,            editor_util,    api) {
    // init ars
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
        editor.on("change", function () {
            syncPush();
            updateUI();
        });
        api.getLanguages(function (data) {
            var items = [];

            $.each(data, function(index, val) {
                var lang_id = val[0], 
                    lang_name = val[1];
                items.push('<option value="' + lang_id + '" '+ ( lang_id == 'text' ? 'selected' : '' ) +'>' + lang_name + '</li>');
            });

            langs = $('<select/>', {
                'class': 'language',
                html: items.join('')
            })

            elements.langSelector.html(langs);
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
        elements.displayUrl.html('<form action="'+displayUrlVal+'" method="get" class="navbar-form pull-left"> <input value="'+displayUrlVal+'" type="text" class="span3"><button type="submit" class="btn">GO</button></form>');
        /*
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
        */
    };

    init();

    
});

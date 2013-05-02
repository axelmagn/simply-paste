/**
 * Module: snippet_create
 *
 * main module loaded for snippet create views
 * provides a javascript interface for creating and pushing snippets
 *
 */
requirejs(["jquery",    "util/editor",  "util/snippet_api", "bootstrap"], 
 function($,            editor_util,    api,                bootstrap) {
    // init ars
    var snippetPush, 
        remoteSnippet = {}, 
        init,
        elements,
        syncPush,
        updateUI,
        getLocalSnippet,
        isPushing = false,
        errorFlag = false,
        errorMessage,
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
            'langSelector': $("#lang-selector"),
            'errorIcon': $("#error-icon")
        };
        editor.on("change", function () {
            syncPush();
        });
        elements.langSelector.on("change", function( data ) {
            syncPush();
            lang = elements.langSelector.find("select").val();
            editor.getSession().setMode("ace/mode/"+lang);
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

        // update the ui
        updateUI();
    }


    /**
     * Push a snippet object to the server
     *
     * TODO: replace hardcoded api endpoints with more dynamic system
     */
    snippetPush = function( snippet ) {
        isPushing = true;
        updateUI();
        $.ajax({
            type:       "POST",
            dataType:   "json",
            url:        "/api/snippets/push/",
            data:       snippet,
            success: function ( data ) 
            {
                // cannot set in complete due to race conditions
                isPushing = false;
                // store remote state
                remoteSnippet = data;
                // sync again to keep remote content up to date
                syncPush();
            },
            error: function ( jqXHR, textStatus ) 
            {
                // cannot set in complete due to race conditions
                isPushing = false;
                // TODO
                // parse error message
                // show error message
                errorFlag = true;
            }, 
            complete: function () {
                updateUI();
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
        if( synced !== true && localSnippet.content != '' && !isPushing ) {
            isPushing = true;
            snippetPush( localSnippet );
        } else {
            isPushing = false;
        }



    };

    /** 
     * Function: updateUI
     *
     * Make any ui changes to reflect current state
     */
    updateUI = function () {
        // display url if we have a remote snippet to point to
        displayUrlVal = remoteSnippet.display_url;
        if( displayUrlVal !== undefined )
        {
            elements.displayUrl.html('<form class="navbar-form pull-left"> <input value="'+displayUrlVal+'" type="text" class="span3"></form><a href="'+displayUrlVal+'" class="btn">GO</a>');
        }

        // spinner correlates to currently pushing a snippet to server
        if( isPushing ) 
        {
            elements.spinner.show();
        } 
        else 
        {
            elements.spinner.hide();
        }

        if( errorFlag )
        {
            elements.errorIcon.show();
        }
        else
        {
            elements.errorIcon.hide();
        }
    };

    init();

    
});

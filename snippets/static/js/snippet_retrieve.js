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
        editor.setReadOnly( true );
        // read elements
        elements = {
        };
        // set language
    }


    init();

    
});


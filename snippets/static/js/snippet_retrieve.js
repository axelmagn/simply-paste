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
            'language': $('#lang-display')
        };
        // set language
        lang = elements.language.html();
        editor.getSession().setMode("ace/mode/"+lang);
    }


    init();

    
});


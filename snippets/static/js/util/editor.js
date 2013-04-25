define(["ace/ace"], function(ace) {
    var init;

    /**
     * Initialize editor with theme and language
     *
     */
    init = function(editor_id, editor_theme, editor_lang) {
        // init vars
        var editor, mode_prefix, theme_prefix;
        mode_prefix     = "ace/mode/";
        theme_prefix    = "ace/theme/";
        

        // parameter defaults
        editor_theme = typeof editor_theme !== 'undefined' ? editor_theme : "monokai";
        editor_lang = typeof editor_lang !== 'undefined' ? editor_lang : "text";

        // stitch paths
        editor_theme_path = theme_prefix + editor_theme;
        editor_lang_path = mode_prefix + editor_lang;

        // start editor
        editor = ace.edit(editor_id);
        // set theme
        editor.setTheme(editor_theme_path);
        // set language
        editor.getSession().setMode(editor_lang_path);
        return editor;
    }

    return {"init": init};
});

require(["ace/ace"], function($) {
    //the jquery.alpha.js and jquery.beta.js plugins have been loaded.
    $(function() {
        var editor = ace.edit("editor");
        editor.setTheme("ace/theme/monokai");
        // editor.getSession().setMode("ace/mode/javascript");
    });
});

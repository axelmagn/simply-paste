requirejs(["ace/ace"], function(ace) {
    var editor = ace.edit("editor");
    editor.setTheme("ace/theme/monokai");
    // editor.getSession().setMode("ace/mode/javascript");
    editor.insert("Inserted text Muthafucka!");
    window['editor'] = editor;
});

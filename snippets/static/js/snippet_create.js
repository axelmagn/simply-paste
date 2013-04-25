requirejs(["ace/ace", "util/editor", "util/snippet_api"], function(ace, editor, api) {
    // init vars

    // start editor
    editor.init("editor");

    // get api
    console.log(api.responseJSON);
});

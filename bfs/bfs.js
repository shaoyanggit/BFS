console.log("start bfs.js");

function initialize(){
    console.log("start initialization")
    var tree;
    chrome.bookmarks.getTree(function(tree) {
        console.log(tree);
        // TODO iterate tree nodes and send to server
    });
}

chrome.runtime.onInstalled.addListener(initialize)
console.log("add runtime.onInstalled listener successfully");

function handleCreated(id, bookmarkInfo) {
    console.log(`New bookmark ID: ${id}`);
    console.log(`New bookmark URL: ${bookmarkInfo.url}`);
    // TODO send new bookmarks to server
}
  
chrome.bookmarks.onCreated.addListener(handleCreated);

function suggest(suggestResults){
    ;
}

chrome.omnibox.onInputChanged.addListener(function(text,suggest){
    // TODO open connection and send query
}); 

console.log("end bfs.js");

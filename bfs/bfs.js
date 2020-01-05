function initialize(){

    let list=[];
    let queue=[];
    chrome.bookmarks.getTree(function(tree) {
        
        for(let i=0;i<tree.length;i++)
        queue.push(tree[i]);
        
        while(queue.length!=0){
            let node=queue.shift();
            
            if(node.children!=null){ // folder
                let children=node.children;
                for(let i=0;i<children.length;i++)
                queue.push(children[i]);
            }
            else if(node.url!=null){ // bookmark
                list.push({'url': node.url, 'title': node.title});
            }
            else{ // seperator
                ;
            }
        }
        list_json = JSON.stringify(list);
        send(list_json);
    });
    
    // send to server
    function send(list_json) {
        let xhttp=new XMLHttpRequest();
        xhttp.open("POST","http://127.0.0.1:2020",true);
        xhttp.setRequestHeader("Content-Type","text/plain");
        xhttp.send(list_json);
    }

}

chrome.runtime.onInstalled.addListener(initialize)

function handleCreated(id, bookmarkInfo) {

    let xhttp=new XMLHttpRequest();
    xhttp.open("POST","http://127.0.0.1:2020/new",true);
    xhttp.setRequestHeader("Content-Type","text/plain");
    xhttp.send(JSON.stringify({'title': bookmarkInfo.title, 'url': bookmarkInfo.url}));
}
  
chrome.bookmarks.onCreated.addListener(handleCreated)

chrome.omnibox.onInputChanged.addListener(function(text,suggest){
    let xhttp=new XMLHttpRequest();
    xhttp.open("GET","http://127.0.0.1:2020/search?query="+text,true);
    xhttp.onload=function(){
        let result = JSON.parse(this.responseText);
        suggestList=[];
        for(let i=0;i<result.length;i=i+1){
            let suggestion = {};
            suggestion.content=result[i].url;
            suggestion.description=result[i].title;
            suggestList.push(suggestion);
        }
        suggest(suggestList);
    }
    xhttp.send(null);
}); 

chrome.omnibox.onInputEntered.addListener(function(url){
    chrome.tabs.update(null,{url:url});
});
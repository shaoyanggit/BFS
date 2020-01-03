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
                list.push(node);
            }
            else{ // seperator
                ;
            }
        }
    });
    
    // send to server

    let xhttp=new XMLHttpRequest();
    xhttp.open("POST","http://127.0.0.1:2020",true);
    xhttp.setRequestHeader("Content-Type","text/plain");

    list.forEach(function(item,index,array){
        xhttp.send(item.url);
    });

}

chrome.runtime.onInstalled.addListener(initialize)

function handleCreated(id, bookmarkInfo) {

    let xhttp=new XMLHttpRequest();
    xhttp.open("POST","http://127.0.0.1:2020",true);
    xhttp.setRequestHeader("Content-Type","text/plain");
    xhttp.send(bookmarkInfo.url);
}
  
chrome.bookmarks.onCreated.addListener(handleCreated)

chrome.omnibox.onInputChanged.addListener(function(text,suggest){
    let xhttp=new XMLHttpRequest();
    xhttp.open("GET","http://127.0.0.1:2020",true);
    xhttp.onload=function(){
        let suggestion=new SuggestResult();
        suggestion.content=this.responseText;
        suggestion.description="Suggestion from BFS";
        suggest(suggestion);
    }
    console.log('add bookmark');
    XPathResult.send(null);
}); 

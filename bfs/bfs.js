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


function debounce(fn, delay) {
    // 定时器，用来 setTimeout
    var timer

    // 返回一个函数，这个函数会在一个时间区间结束后的 delay 毫秒时执行 fn 函数
    return function () {
        chrome.omnibox.setDefaultSuggestion({
            description: 'Searching...',
        })
        // 保存函数调用时的上下文和参数，传递给 fn
        var context = this
        var args = arguments

        // 每次这个返回的函数被调用，就清除定时器，以保证不执行 fn
        clearTimeout(timer)

        // 当返回的函数被最后一次调用后（也就是用户停止了某个连续的操作），
        // 再过 delay 毫秒就执行 fn
        timer = setTimeout(function () {
        fn.apply(context, args)
        }, delay)
    }
}

function encodeXml(s) {
    var holder = document.createElement('div');
    holder.textContent = s;
    return holder.innerHTML;
}

function getSearchResult(text,suggest){
    let xhttp=new XMLHttpRequest();
    xhttp.open("GET","http://127.0.0.1:2020/search?query="+text,true);
    xhttp.onload=function(){
        let result = JSON.parse(this.responseText);
        if(result.length == 0) {
            chrome.omnibox.setDefaultSuggestion({
                description: 'Result not found',
            })
        } else {
            chrome.omnibox.setDefaultSuggestion({
                description: 'Found result!',
            })
            suggestList=[];
            for(let i=0;i<result.length;i=i+1){
                let suggestion = {};
                suggestion.content=result[i].url;
                suggestion.description=encodeXml(result[i].title);
                suggestList.push(suggestion);
            }
            suggest(suggestList);
        }
    }
    xhttp.send(null);
}

chrome.omnibox.onInputChanged.addListener(debounce(getSearchResult, 500)) 

chrome.omnibox.onInputEntered.addListener(function(url){
    chrome.tabs.update(null,{url:url});
});
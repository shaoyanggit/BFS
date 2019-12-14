tree=browser.bookmarks.getTree(); // TODO doesn't work
console.log("Hello, JavaScript!"); // for debugging

// walk the bookmark tree
// get a list of bookmarks
// TODO test
function walkTree(tree){
    
    let list=[];
    let queue=[];
    queue.push(tree);

    while(queue.length!=0){

        let node=queue.shift();

        if(node.type==="folder"){
            let children=node.children;
            for(let i=0;i<children.length;i++){
                queue.push(children[i]);
            }
        }
        else if(node.type==="bookmark"){
            list.push(node);
        }
        else{ // node.type==="seperator"
            // nothing to do
        }
    }
    
    return list;
}

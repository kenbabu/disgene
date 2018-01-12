    function clearMe()
    {
    $("#clear").on("click", function () { $("#search").val(null).trigger("change"); });
    }
    
    function calculateSimilarity()
    {
    $("#calculate").on("click", function () { $("#search").val('id').trigger("change"); });
    
    }
    
// Check if a list is empty.  
    function isListEmpty(lst)
    {
        if (typeof lst !== 'undefined' && lst.length > 0)
            return false;
        else
            return true;
    }
    
    function leastCommonAncestor(a, b)
    {
        if (a === b) return a;
        var ls1 = [1,2,3,4,5,9],
             ls2 = [1,2,3,6,7,8];
        
        
//        console.log(ls1);
        
        var aNodes = ls1.reverse();
//        console.log(aNodes);
        var bNodes = ls2.reverse();
        
        var aNode = aNodes.pop();
        var bNode = bNodes.pop();
        var sharedNode = null;
        

        while (aNode === bNode && !isListEmpty(aNodes) && !isListEmpty(bNodes))
        {
            sharedNode = aNode;
            aNode = aNodes.pop();
            bNode = bNodes.pop();
        }
        return sharedNode;
    }
    
//    Clear a search 
    function clearAll(d) {
        d.class = "";
        if (d.children)
            d.children.forEach(clearAll);
        else if (d._children)
            d._children.forEach(clearAll);
}

    
    
	//basically a way to get the path to an object
	function searchTree(obj,search,path){
		if(obj.jina.toString() === search){ //if search is found return, add the object to the path and return it
			path.push(obj);
//            console.log(path);
			return path;
		}
		else if(obj.children || obj._children){ //if children are collapsed d3 object will have them instantiated as _children
			var children = (obj.children) ? obj.children : obj._children;
			for(var i=0;i<children.length;i++){
				path.push(obj);// we assume this path is the right one
				var found = searchTree(children[i],search,path);
				if(found){// we were right, this should return the bubbled-up path from the first if statement
//                    console.log(obj.jina)
					return found;
				}
				else{//we were wrong, remove this parent from the path and continue iterating
					path.pop();
				}
			}
		}
		else{//not the right object, return false so it will continue to iterate in the loop
			return false;
		}
	}

	function extract_select2_data(node,leaves,index){
	        if (node.children && node.children.length>0){
	            for(var i = 0;i<node.children.length;i++){
	                index = extract_select2_data(node.children[i],leaves,index)[0];
	            }
	        }
	        else {
	            leaves.push({id:++index,text:node.jina.toString(), topology:node.Similarity });
	        }
	        return [index, leaves];
	}

	var div = d3.select("body")
		.append("div") // declare the tooltip div
		.attr("class", "tooltip")
		.style("opacity", 0);

	var margin = {top: 20, right: 120, bottom: 20, left: 120},
		width = $(document).width() - margin.right - margin.left,
		height = $(document).height() - margin.top - margin.bottom;

	var i = 0,
		duration = 750,
		root,
		select2_data;

	var diameter = 960;

	var tree = d3.layout.tree()
		.size([height, width]);

	var diagonal = d3.svg.diagonal()
		.projection(function(d) { return [d.y, d.x]; });

	var zoom = d3.behavior.zoom()
		.scaleExtent([0.5, 10]);
	var svg = d3.select("body").append("svg")
		.attr("width", width + margin.right + margin.left)
		.attr("height", height + margin.top + margin.bottom)
	  	.append("g")
	//	.attr("transform", "translate(" + margin.left + "," + margin.top + ")") 
		.call(d3.behavior.zoom().on("zoom", function() {
		svg.attr("transform", "translate("+ d3.event.translate +")" + " scale(" + d3.event.scale + ")")
		}));



	//recursively collapse children
	function collapse(d) {
		if (d.children) {
			d._children = d.children;
			d._children.forEach(collapse);
			d.children = null;
		}
	}

	// Toggle children on click.
	function click(d) {
		if (d.children) {
			d._children = d.children;
			d.children = null;
	  	}
	  	else{
			d.children = d._children;
			d._children = null;
	  	}
		update(d);
//        console.log("You clicked "+ d.name + "Depth: " + d.depth +" Similarity: "+d.Similarity);
	}
    
    
    
    
    
	function openPaths(paths){
		for(var i =0;i<paths.length;i++){
			if(paths[i].id !== "1"){//i.e. not root
                if (paths[i].class != 'common_ancestor')
				paths[i].class = 'found';
				if(paths[i]._children){ //if children are hidden: open them, otherwise: dont do anything
					paths[i].children = paths[i]._children;
	    			paths[i]._children = null;
				}
				update(paths[i]);
			}
		}
	}
    

var paths1 = null;
var paths2 = null;
    
var Dsim = function(path1, path2){
    console.log(path1.pop().Similarity);
    console.log("Least Common Ancestor "+findLeastCommonAncestor());
    
    
    
    
//    return parseFloat(-Math.log(Math.max(path1.pop().Similarity, path2.pop().Similarity))).toFixed(3);

};
  function findLeastCommonAncestor(){
    if (paths1===null || paths2===null)
      return;
    var prev=null;
    console.log("checking2");
    console.log(paths1);
    for (var i=0;i<paths1.length;i++){
      if (paths1[i]!=paths2[i]){
        if (prev!=null){
          prev.class = "common_ancestor";    
          var lcaSim= Math.log(prev.Similarity);
          var compSim= Math.log(Math.max(paths1.pop().Similarity,paths2.pop().Similarity));
        console.log(lcaSim);
          
//          console.log((prev.Similarity)/Math.min(1,2));
//            var Dsim =parseFloat((Math.log(prev.Similarity)/-(Math.log(Math.max(paths1.pop().Similarity,paths2.pop().Similarity ) )).toFixed(3);
           
        }
        return;
      }
      prev = paths1[i];
    }
  }
    
// document.getElementById("disease_sim").innerHTML="<b>Disease Similarity: "+Dsim(paths1, paths2) +"</b>";
    
// DOtestjson.json
	d3.json("./data/myfile.json", function(error,values){
		root = values;
		select2_data = extract_select2_data(values,[],0)[1];// Could be improved
		
        
		root.x0 = height / 2;
		root.y0 = 0;
		root.children.forEach(collapse);
		update(root);
		//init search box
		$("#search").select2({
            placeholder: 'Select disease 1',
            multiple: true,
			data: select2_data,
            allowClear: true,
            maximumSelectionSize: 2,
            minimumResultsForSearch: Infinity,
            closeOnSelect: true,
			containerCssClass: "search"
           
		});
        
        $("#search2").select2({
            placeholder: 'Select disease 2',
            multiple: true,
			data: select2_data,
            allowClear: true,
            maximumSelectionSize: 2,
            minimumResultsForSearch: Infinity,
            closeOnSelect: true,
			containerCssClass: "search"
           
		});
	});
    
	//attach search box listener
	$("#search").on("select2-selecting", function(e) {
        
		paths1 = searchTree(root,e.object.text,[]);
		if(typeof(paths1) !== "undefined" ){
            findLeastCommonAncestor();
			openPaths(paths1);  
           
		}
		else{
			alert(e.object.text+" not found!");
		}
        
	})
    
    $("#search2").on("select2-selecting", function(e) {
       
		paths2 = searchTree(root,e.object.text,[]);
		if(typeof(paths2) !== "undefined" ){
            findLeastCommonAncestor();
			openPaths(paths2);   
		}
		else{
			alert(e.object.text+" not found!");
		}
        
	})
    
    
   
	d3.select(self.frameElement).style("height", "800px");

	function update(source) {
		// Compute the new tree layout.
		var nodes = tree.nodes(root).reverse(),
		links = tree.links(nodes);

		// Normalize for fixed-depth.
		nodes.forEach(function(d) { d.y = d.depth * 180; });

		// Update the nodes¦
		var node = svg.selectAll("g.node")
			.data(nodes, function(d) { return d.id || (d.id = ++i); });

		// Enter any new nodes at the parent's previous position.
		var nodeEnter = node.enter().append("g")
			.attr("class", "node")
			.attr("transform", function(d) { return "translate(" + source.y0 + "," + source.x0 + ")"; })
//            .on("click", function(d) { return alert(d.name + " was clicked!"); })
            .on("click", click)
			.on("mouseover", function(d) {
        		div.transition()
          			.duration(200)
          			.style("opacity", .9);
        		div .html(
             d.name + "<br/>" +"Topology Score: "+d.Similarity+"<br/>"+
            "Name: " + d.jina + "<br/>"
            )
          .style("left", (d3.event.pageX) + "px")
          .style("top", (d3.event.pageY - 40) + "px");
        })
      .on("mouseout", function(d) {
        div.transition()
          .duration(500)
          .style("opacity", 0);
        });
			
//create node graphic
		nodeEnter.append("circle")
			.attr("r", 1e-6)
			.style("fill", function(d) { return d._children ? "lightsteelblue" : "#fff"; });
//Create node labels
		nodeEnter.append("text")
			.attr("x", function(d) { return d.children || d._children ? -10 : 10; })
			.attr("dy", ".35em")
			.attr("text-anchor", function(d) { return d.children || d._children ? "end" : "start"; })
			.text(function(d) { return d.jina; });
			
	var div = d3.select("body").append("div")	
    			.attr("class", "tooltip")				
    			.style("opacity", 0);		
			
			
// 			.style("fill-opacity", 1e-6);

		// Transition nodes to their new position.
		var nodeUpdate = node.transition()
			.duration(duration)
			.attr("transform", function(d) { return "translate(" + d.y + "," + d.x + ")"; });

		nodeUpdate.select("circle")
//			.attr("r", 4.5)
            .attr("r", function(d) {
                if(d.class === "common_ancestor"){
                    return 10;
                }
                else
//                    console.log(d.children.length);
                    return  4.5;
            })
			.style("fill", function(d) {
				if(d.class === "common_ancestor"){
					return "#41ff36"; //green
				}
                else if(d.class === "found"){
					return "#ff4136"; //red;
				}
				else if(d._children){
					return "lightsteelblue";
				}
				else{
					return "#fff";
				}
			})
			.style("stroke", function(d) {
				if(d.class === "found" ){
					return "#ff4136"; //red
				}
            // || d.class === "common_ancestor"
		});

		nodeUpdate.select("text")
			.style("fill-opacity", 1);

		// Transition exiting nodes to the parent's new position.
		var nodeExit = node.exit().transition()
			.duration(duration)
			.attr("transform", function(d) { return "translate(" + source.y + "," + source.x + ")"; })
			.remove();

		nodeExit.select("circle")
			.attr("r", 1e-6);

		nodeExit.select("text")
			.style("fill-opacity", 1e-6);

		// Update the links
		var link = svg.selectAll("path.link")
			.data(links, function(d) { return d.target.id; });

		// Enter any new links at the parent's previous position.
		link.enter().insert("path", "g")
			.attr("class", "link")
			.attr("d", function(d) {
				var o = {x: source.x0, y: source.y0};
				return diagonal({source: o, target: o});
			});

		// Transition links to their new position.
		link.transition()
			.duration(duration)
			.attr("d", diagonal)
            .style("stroke-width", function(d){
                if(d.target.class === "found" || d.target.class === "common_ancestor"){
                    return "3px";
                }
            })
        // Colour paths of found nodes
			.style("stroke",function(d){
//				if(d.target.class === "found" || d.target.class === "common_ancestor"){
                if(d.target.class === "found" ){
					return "#ff4136";
                }
                else if(d.target.class === "common_ancestor"){
                    return "#ff4136";
				}
			});

		// Transition exiting nodes to the parent's new position.
		link.exit().transition()
			.duration(duration)
			.attr("d", function(d) {
				var o = {x: source.x, y: source.y};
				return diagonal({source: o, target: o});
			})
			.remove();

		// Stash the old positions for transition.
		nodes.forEach(function(d) {
			d.x0 = d.x;
			d.y0 = d.y;
		  });
	}


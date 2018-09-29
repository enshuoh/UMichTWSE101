

Reveal.addEventListener( 'fragmentshown', function( event ) {
    var p = event.fragment.getAttribute('data-tmt');
    if (p === "LCS-example") {
        var dom_A = document.getElementById("LCS-example-A");
        var dom_B = document.getElementById("LCS-example-B");
        var A = dom_A.innerHTML;
        var B = dom_B.innerHTML;
        
        console.log(A, B);
    }
	// event.fragment = the fragment DOM element
});

Reveal.addEventListener( 'fragmenthidden', function( event ) {
    var p = event.fragment.getAttribute('data-tmt');
    if (p === "LCS-example") {
        
    }
	// event.fragment = the fragment DOM element
});


// LCS Example
Reveal.addEventListener( 'ready', function( event ) {
	// event.currentSlide, event.indexh, event.indexv
    var t = $("#LCS-example-table").find("td");
    
    for (var i = 0; i < t.length; i++) {
        var elem = $(t[i]);
        var txt = elem.text();
        if (!(txt >= "0" && txt <= "9")) continue;
            
        var val = parseInt(txt);
        var c = ['#FFF', '#FED', '#FDC', '#FCB', '#FBA', '#FA9'];
        elem.css('background-color', c[val]);
        
        $(t[i]).mouseenter(function(e) {
            $(this).css('backgroundColor', '#FF3');
        }).mouseleave(function(e) {
            var val = parseInt($(this).text());
            $(this).css('backgroundColor', c[val]);
        });
    }
} );

// Typesetting Problem
Reveal.addEventListener( 'ready', function( event ) {
	// event.currentSlide, event.indexh, event.indexv
    $(".typesetting-example").css('backgroundColor', '#FDA').css('display', 'flex').css('flex-wrap', 'wrap');
    var contents = $(".typesetting-example");
    for (var i = 0; i < contents.length; i++) {
        var cont = $(contents[i]);
        var parts = $.map(cont.html().split(' '), function(v) {
        var t = $('<span />', {html: v});
        t.css('backgroundColor', '#FFF').css('display', 'inline-block').css('paddingRight', '12px');
        return t;
        });
        cont.empty().append(parts);
    }
} );

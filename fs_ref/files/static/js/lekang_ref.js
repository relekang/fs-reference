function References(domain, lang_label, content_holder) {
    this.domain = domain;
    this.lang_label = lang_label;
    this.content_holder = $(content_holder);
    this.get();
}

References.prototype.get = function () {
    var url = "http://" + this.domain + '/' + this.lang_label + "/api/references/";
    window.console.log(url);
    var ref = this;
    $.ajax({
        url: url,
        dataType:"jsonp",
        success:function (data) {
            ref.fill(data);
        },
        error:function (xhr, ajaxOptions, thrownError) {
            window.console.log('Could not retrieve references');
        }
    });
};

References.prototype.fill = function (data) {

    data = data.sort(function (a, b) {
        var A = a.market.toLowerCase(), B = b.market.toLowerCase()
        if (A < B) return -1;
        if (A > B) return 1;
        return 0;
    });

    this.content_holder.html('<article class="row-fluid"></article>');
    var output = '<ul class="thumbnails">';
    var menu = '<div style="margin: 0 10px 20px 10px;">';
    var market = '';

    for (var i = 0; i < data.length; i++) {
        if (data[i].market != market) {
            output += '<li class="title" style="list-style-type:none;" id="' + data[i].market.toLowerCase().replace(' ','') + '"><h2 style="font-size:18px">' + data[i].market + '</h2></li>';
            menu += '<a href="#' + data[i].market.toLowerCase().replace(' ','') + '" style="margin:6px;padding:4px;color:black;font-size:18px;">' + data[i].market + '</a>';
            market = data[i].market;
        }
        output += '<li class="thumbnail" style="width:200px; height:240px; text-align: center;">';
        output += '<a href="http://'+ this.domain + data[i].url + '" target="_blank">';
        output += '<img src="http://' + this.domain + data[i].list_image + '" style="width: 200px; height:200px;"><br/>';
        output += data[i].title;
        output += '</a>';
        output += '</li>';
    }

    output += '</ul>';
    menu += '</div>';
    $("article.row-fluid", this.content_holder).append(menu);
    $("article.row-fluid", this.content_holder).append(output);

}


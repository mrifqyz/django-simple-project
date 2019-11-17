$(document).on({
    ajaxStart: function () {
        $('.none').css('display', 'block');
    },
    ajaxStop: function () {
        $('.none').css('display', 'none');
    }
});

function countChanger(num) {
    if (num == "") return 10;
    else return num;
}

$(document).ready(function () {
    $('.form-inline').submit(function (event) {
        let count = $(".numbox").val();
        count = countChanger(count);

        let searchItem = $('.btn-search').prev().prev().val();
        let urlItem = "https://www.googleapis.com/books/v1/volumes?q=" + searchItem + "&maxResults=" + count;

        $.ajax({
            async: true,
            type: 'GET',
            url: urlItem,
            dataType: 'json',
            success: function (searchRes) {
                $('.status-container').next().addClass('none');
                $('.status-container').removeClass('none');
                let bookShelf = searchRes.items;

                $('tbody').empty();

                for (i = 0; i < count; i++) {
                    let book = bookShelf[i].volumeInfo;
                    var num = $('<td>').text(i + 1);
                    var name = $('<td>').text(book.title);

                    if ('publisher' in book == false) var publisher = $('<td>').text('-');
                    else var publisher = $('<td>').text(book.publisher);

                    if ('pageCount' in book == false) var pageCount = $('<td>').text("-");
                    else var pageCount = $('<td>').text(book.pageCount);

                    if ('authors' in book == false) var authors = $('<td>').text("-");
                    else var authors = $('<td>').text(book.authors);

                    if ('categories' in book == false) var categories = $('<td>').text("-");
                    else var categories = $('<td>').text(book.categories);

                    if ('imageLinks' in book == false)
                        var img = $('<td>').text("-");
                    else {
                        if ('smallThumbnail' in book.imageLinks == false)
                            var img = $('<td>').append($('<img>').attr({
                                'src': book.imageLinks.thumbnail
                            }));
                        else
                            var img = $('<td>').append($('<img>').attr({
                                'src': book.imageLinks.smallThumbnail
                            }));
                    }

                    var tr = $('<tr>').append(num, name, authors,
                        pageCount, publisher, categories, img);

                    $('tbody').append(tr);

                }
            },
            error: function () {
                $('.status-container').next().addClass('none');
                alert("Mohon maaf terjadi kesalahan. Coba ulangi lagi ya!");
            },
            type: 'GET',
        })
        event.preventDefault();
    })

});
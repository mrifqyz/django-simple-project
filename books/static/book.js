$(document).on({
    ajaxStart: function() {
        $('.none').css('display', 'block');
      },
      ajaxStop: function(){
        $('.none').css('display', 'none');
      }
});

$(document).ready(function () {


    $('.form-inline').submit(function(event){
            let searchItem = $('.btn-search').prev().val();
            let urlItem = "https://www.googleapis.com/books/v1/volumes?q="+searchItem;
  
            $.ajax({
                async: true,
                type:'GET',
                url:urlItem,
                dataType:'json',
                success:function(searchRes){
                    $('.status-container').next().addClass('none');
                    $('.status-container').removeClass('none');

                  let bookShelf = searchRes.items;

                  $('tbody').empty();
                  for(i = 0; i<10;i++){
                      if(bookShelf[i]==undefined)
                        continue;
                        else{
                            let book = bookShelf[i].volumeInfo;
                            var toBeAppendNum = $('<td>').text(i+1);
                            var toBeAppendName = $('<td>').text(book.title);

                            if('publisher' in book == null) var toBeAppendPub = $('<td>').text('-');
                            else var toBeAppendPub = $('<td>').text(book.publisher);

                            var toBeAppendPub = $('<td>').text(book.publisher);
                            var toBeAppendCount = $('<td>').text(book.pageCount);
      
                            if('authors'in book == false) var toBeAppendAuth =  $('<td>').text("-");
                            else var toBeAppendAuth = $('<td>').text(book.authors[0]);
      
                            var toBeAppendISBN = $('<td>').text(book.categories);

                            if('imageLinks' in book == false)
                                var toBeImage = $('<td>').text("-");
                            else{
                                if('smallThumbnail' in book.imageLinks == false) 
                                var toBeImage = $('<td>').append($('<img>').attr({'src':book.imageLinks.thumbnail}));
                                else
                                var toBeImage = $('<td>').append($('<img>').attr({'src':book.imageLinks.smallThumbnail}));
                            }
      
                            var tr = $('<tr>').append(toBeAppendNum, toBeAppendName, toBeAppendAuth,
                              toBeAppendCount, toBeAppendPub, toBeAppendISBN, toBeImage);
      
                          $('tbody').append(tr);
                        }
                  }
                },
                error:function(){
                    $('.status-container').next().addClass('none');
                    alert("Mohon maaf terjadi kesalahan. Coba ulangi lagi ya!");
                },
                type: 'GET',
            })    
        event.preventDefault();
    })

});
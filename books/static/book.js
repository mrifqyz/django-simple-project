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
        $(".btn-search").click(function(){
            let searchItem = $(this).prev().val();
            let urlItem = "https://www.googleapis.com/books/v1/volumes?q="+searchItem;
  
            $.ajax({
                type:'GET',
                url:urlItem,
                dataType:'json',
                success:function(searchRes){
                  let bookShelf = searchRes.items;
                //   if($(".result").children().length>0){
                //       $(".result").html("");
                //   }
                  for(i = 0; i<10;i++){
                      let book = bookShelf[i].volumeInfo;
                  }
                }
            })    
        });
        event.preventDefault();
    })
});
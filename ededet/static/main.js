$(document).on({
    ajaxStart: function() {
        $('.none').css('display', 'block');
      },
      ajaxStop: function(){
        $('.none').css('display', 'none');
      }
});

$(document).ready(function () {

    $('input[type=checkbox]').change(function(){
        var changeableElement = ["a", "h1", "p", "td", "th", 'li']
        if ($(this).is(':checked')) {
            for(i=0;i<changeableElement.length;i++){
                $(changeableElement[i]).addClass("text-light");
            }
            $('body').removeClass("bg-light").addClass("bg-dark");
            $('.btn-border').addClass("btn-border-rev");
            $('.form-style').addClass("border-white");
            $('.icon16').addClass("fill-white");
            $('.icon24').addClass("fill-white");
            $('.accordion').removeClass('bg-dark').addClass("bg-light");
            $('.ac-i').removeClass('text-light').addClass('text-dark');
            $('.ac-s').removeClass('fill-white');
        }else{
            for(i=0;i<changeableElement.length;i++){
                $(changeableElement[i]).removeClass("text-light");
            }
            $('body').removeClass("bg-dark").addClass("bg-light");
            $('.btn-border').removeClass("btn-border-rev");
            $('.form-style').removeClass("border-white");
            $('.icon16').removeClass("fill-white");
            $('.icon24').removeClass("fill-white");
            $('.accordion').removeClass("bg-light").addClass('bg-dark');
            $('.ac-i').removeClass('text-dark').addClass('text-light');
            $('.ac-s').addClass('fill-white');
        }
    });

    $('.accordion').each(function () {
        $(this).click(function(){
            var $this = $(this);
            var maxHeight = $this.next().css('max-height');
            console.log("yuhu, max-heightnya itu " + maxHeight);
            if($this.next().css('max-height')=='0px'){
                var nextHeight = $this.next().prop('scrollHeight') + 'px';
                $this.next().css('max-height', nextHeight);
                console.log('executed if');
            }else{  
                $this.next().css('max-height', '');
                console.log('executed else');
            }
        });
      });
});
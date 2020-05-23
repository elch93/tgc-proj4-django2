$(function () {

    //carousell code
    let n = 0;
    showSlide(n);

    function showSlide(x) {
        for (let i = 0; i < $(".mycarousel").length; i++) {
            $(".mycarousel").eq(i).hide();
            $(".cindicator").eq(i).css("background-color", "grey");
            $(".cindicator").eq(i).mouseover(function () {
                $(this).css("background-color", "gold");
            });
            $(".cindicator").eq(i).mouseout(function () {
                $(this).css("background-color", "grey");
            });
        }



        $(".mycarousel").eq(x).show();
        $(".cindicator").eq(x).css("background-color", "white");
        $(".cindicator").eq(x).mouseover(function () {
            $(this).css("background-color", "gold");
        });
        $(".cindicator").eq(x).mouseout(function () {
            $(this).css("background-color", "white");
        });
    }

    $("#next").click(function () {
        if (n == $(".mycarousel").length - 1) {
            n = -1;
        }
        showSlide(n += 1);
    });

    $("#prev").click(function () {
        if (n == 0) {
            n = $(".mycarousel").length;
        }
        showSlide(n -= 1);
    });

    for (let i = 0; i < $(".mycarousel").length; i++) {
        $(".cindicator").eq(i).click(function () {
            showSlide(i);
        });
    }
    //carousel code end
})
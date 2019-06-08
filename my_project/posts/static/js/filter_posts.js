(function () {
    'use strict';

    function init(e) {
        var submit = document.getElementById('submit');
        var input_text = document.getElementById('input_search');

        function filterPosts(filter_text) {
            var posts = document.getElementsByClassName('post');
            var len = posts.length;
            for (var j = 0; j < len; j++) {
                tags = posts[j].getElementsByTagName("h4")[0].innerHTML.substring(6).replace(/\s+/g, '').split(",");

                var filters = filter_text.replace(/\s+/g, '').split(",");

                posts[j].classList.add("hide");

                for (var k = 0; k < filters.length; k++) {
                    if (!(tags.includes(filters[k]))) {
                    } else {
                        posts[j].classList.remove("hide");
                    }
                }
            }
        }

        submit.addEventListener("click", function (e) {
            e.preventDefault();
            filterPosts(input_text.value);
        }, false);
    }
    window.addEventListener("DOMContentLoaded", init, false);
})();

!(function (r) {
    "use strict";
    "object" == typeof module && "object" == typeof module.exports ? (module.exports = r(require("jquery"))) : r(jQuery);
})(function ($) {
    "use strict";
    var r = {
        bgVertical: function (r, t) {
            return r.css({ "background-position": "center " + -t + "px" });
        },
        bgHorizontal: function (r, t) {
            return r.css({ "background-position": -t + "px center" });
        },
        vertical: function (r, t, o) {
            return (
                "none" === o ? (o = "") : !0,
                r.css({ "-webkit-transform": "translateY(" + t + "px)" + o, "-moz-transform": "translateY(" + t + "px)" + o, transform: "translateY(" + t + "px)" + o, transition: "transform linear", "will-change": "transform" })
            );
        },
        horizontal: function (r, t, o) {
            return (
                "none" === o ? (o = "") : !0,
                r.css({ "-webkit-transform": "translateX(" + t + "px)" + o, "-moz-transform": "translateX(" + t + "px)" + o, transform: "translateX(" + t + "px)" + o, transition: "transform linear", "will-change": "transform" })
            );
        },
    };
    $.fn.paroller = function (t) {
        var o = $(window).height(),
            n = $(document).height(),
            t = $.extend({ factor: 0, type: "background", direction: "vertical" }, t);
        return this.each(function () {
            var a = !1,
                e = $(this),
                i = e.offset().top,
                c = e.outerHeight(),
                l = e.data("paroller-factor"),
                s = e.data("paroller-type"),
                u = e.data("paroller-direction"),
                offVal = e.data("paroller-offset"),
                f = l ? l : t.factor,
                d = s ? s : t.type,
                h = u ? u : t.direction,
                p = Math.round(i * f),
                g = Math.round((i - o / 2 + c) * f),
                m = e.css("transform");
            "background" == d ? ("vertical" == h ? r.bgVertical(e, p) : "horizontal" == h && r.bgHorizontal(e, p)) : "foreground" == d && ("vertical" == h ? r.vertical(e, g, m) : "horizontal" == h && r.horizontal(e, g, m));
            var b = function () {
                a = !1;
            };

            if (typeof offVal !== 'undefined') {

            	i = parseInt(offVal);
            }

            $(window)
                .on("scroll", function () {
                    if (!a) {
                        var t = $(this).scrollTop();

                        (n = $(document).height()),
                            (p = Math.round((i - t) * f)),
                            (g = Math.round((i - o / 2 + c - t) * f)),
                            "background" == d
                                ? "vertical" == h
                                    ? r.bgVertical(e, p)
                                    : "horizontal" == h && r.bgHorizontal(e, p)
                                : "foreground" == d && n >= t && ("vertical" == h ? r.vertical(e, g, m) : "horizontal" == h && r.horizontal(e, g, m)),
                            window.requestAnimationFrame(b),
                            (a = !0);
                    }
                })
                .trigger("scroll");
        });
    };
});

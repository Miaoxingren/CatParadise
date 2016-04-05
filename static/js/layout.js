CATPARADISE = {}

CATPARADISE.addEvent = function(target, type, listener) {
    if (target.addEventListener) {
        target.addEventListener(type, listener, false);
    } else if (target.attachEvent) {
        target.attachEvent('on' + type, listener);
    } else {
        target['on' + type] = listener;
    }
};

CATPARADISE.classHandler = (function () {
    var hasClass = function (target, classname) {
            return target.className.indexOf(classname) !== -1;
        },

        addClass = function(target, classnames) {
            var classes = classnames.split(' ');
                i = 0,
                max = classes.length;
            for (; i < max; i += 1) {
                if (!hasClass(target, classes[i])) {
                    target.className += " " + classes[i];
                }
            }
        },

        removeClass = function(target, classnames) {
            var classes = classnames.split(' ');
                i = 0,
                max = classes.length;
            for (; i < max; i += 1) {
                if (hasClass(target, ' ' + classes[i])) {
                    target.className = target.className.replace(' ' + classes[i], "");
                } else if (hasClass(target, classes[i])) {
                    target.className = target.className.replace(classes[i], "");
                }   
            }
        };

    return {
        hasClass: hasClass,
        addClass: addClass,
        removeClass: removeClass
    };
})();

(function(){
    CATPARADISE.addEvent(window, 'scroll', function() {
        var scrollTop = document.body.scrollTop || document.documentElement.scrollTop || window.pageYOffset || 0,
            nav = document.querySelector('#main header > div.container-fluid'),
            navImg = document.querySelector('#main .navbar-brand img');
        if (scrollTop > 0) {
            if (navImg.src.indexOf('logo-32.png') === -1) {
                navImg.src = 'static/images/logo-32.png';
            }
            CATPARADISE.classHandler.addClass(nav, 'navbar-bg');
        } else {
            if (navImg.src.indexOf('logo-32-light.png') === -1) {
                navImg.src = 'static/images/logo-32-light.png';
            }
            CATPARADISE.classHandler.removeClass(nav, 'navbar-bg');
        }
    });
})();


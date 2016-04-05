
window.onload = function () {
    var breedLeft = document.querySelector('#cat-breeds .breed-left'),
        breedRight = document.querySelector('#cat-breeds .breed-right'),
        breedLImg = document.querySelector('#cat-breeds .breed-left img'),
        breedRImg = document.querySelector('#cat-breeds .breed-right img'),
        breedLSpan = document.querySelector('#cat-breeds .breed-left .icon'),
        breedRSpan = document.querySelector('#cat-breeds .breed-right .icon');
    CATPARADISE.addEvent(breedLeft, 'mouseover', function() {
        breedLSpan.style.color = 'red';
        CATPARADISE.classHandler.removeClass(breedLImg, 'img-small');
        CATPARADISE.classHandler.addClass(breedLImg, 'img-big');
    });
    CATPARADISE.addEvent(breedLeft, 'mouseout', function() {
        breedLSpan.style.color = 'blue';
        CATPARADISE.classHandler.removeClass(breedLImg, 'img-big');
        CATPARADISE.classHandler.addClass(breedLImg, 'img-small');
    });
    CATPARADISE.addEvent(breedRight, 'mouseover', function() {
        breedRSpan.style.color = 'red';
        CATPARADISE.classHandler.removeClass(breedRImg, 'img-small');
        CATPARADISE.classHandler.addClass(breedRImg, 'img-big');
    });
    CATPARADISE.addEvent(breedRight, 'mouseout', function() {
        breedRSpan.style.color = 'blue';
        CATPARADISE.classHandler.removeClass(breedRImg, 'img-big');
        CATPARADISE.classHandler.addClass(breedRImg, 'img-small');
    });
}

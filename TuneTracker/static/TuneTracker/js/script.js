 document.addEventListener('DOMContentLoaded', function () {
     
    var toggleButton = document.getElementById('toggleButton');
    var songList = document.getElementById('songList');

     
    if (toggleButton && songList) {
        toggleButton.addEventListener('click', function () {
             
            songList.classList.toggle('hidden');
        });
    }
});

//第一次放歌随机放,chrome不可用
var musicInit = document.getElementById("bgmc");
var initList = ["CHRONOS RECORD - Mallku(原曲：年中梦中の好奇心).mp3", "DELA - mirror.mp3", "himmel - 未梦.mp3", "ばんばんしー - 秋姉妹のなく顷に.mp3", "凛 - Ayakashi set 16 ~ さくらさくら.mp3", "灰澈 - 星茶会.mp3", "灰澈 - 春之行.mp3", "灰澈 - 森林.mp3", "神乃木製作所 - あしたの幻想郷(3 years arrange) (神々が恋した幻想郷).mp3", "神乃木製作所 - 踊る水飞沫 ~ Irish Session (踊る水飞沫).mp3"];
var numnum = parseInt(Math.random() * (initList.length));
var textInit = document.getElementById("np");
musicInit.src = "audio/";
musicInit.src += initList[numnum];

textInit.innerText = numnum;
var playing = 0;
//以后每次歌曲结束都随机放新的
function fuc() {

    var songList = ["CHRONOS RECORD - Mallku(原曲：年中梦中の好奇心).mp3", "DELA - mirror.mp3", "himmel - 未梦.mp3", "ばんばんしー - 秋姉妹のなく顷に.mp3", "凛 - Ayakashi set 16 ~ さくらさくら.mp3", "灰澈 - 星茶会.mp3", "灰澈 - 春之行.mp3", "灰澈 - 森林.mp3", "神乃木製作所 - あしたの幻想郷(3 years arrange) (神々が恋した幻想郷).mp3", "神乃木製作所 - 踊る水飞沫 ~ Irish Session (踊る水飞沫).mp3"];
    var te = document.getElementById("np");
    var nowPlaying = parseInt(te.innerText);
    var numnum = parseInt(Math.random() * (songList.length));
    while (numnum == nowPlaying) {
        numnum = parseInt(Math.random() * (songList.length));
    }

    te.innerText = numnum;
    var au = document.getElementById("bgmc");
    au.src = "{0}{1}".format("audio/", songList[numnum]);
    au.play();
}

function pauseAndPlay() {
    if (playing == 1) {
        musicInit.pause();
        playing = 0;
    } else {
        musicInit.play();
        playing = 1;
    }
}
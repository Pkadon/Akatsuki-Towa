label avg25142:

scene placeholderbackground
window show
with fade_in
play sfx2 "other_7092.ogg"
c0 '[textdict[1210444]]'
$ update_portrait('oc002_01 14', 'p2', [mid(-3), light], 5)
play sfxvoice "avg_vocal_ch08.ogg"
c23 '[textdict[1210445]]'
hide p2
$ update_portrait('oc001_01 8', 'p1', [mid(-2), light], 5)
c13 '[textdict[1210446]]'
hide p1
$ update_portrait('oc002_01 5', 'p2', [mid(-3), light], 5)
play sfxvoice "avg_vocal_ch07.ogg"
c23 '[textdict[1210447]]'
hide p2
$ update_portrait('oc001_01 4', 'p1', [mid(-2), light], 5)
play sfxvoice "avg_vocal_na10.ogg"
c13 '[textdict[1210448]]'
hide p1
$ update_portrait('oc002_01 14', 'p2', [mid(-3), light], 5)
play sfxvoice "avg_vocal_ch04.ogg"
c23 '[textdict[1210449]]'
hide p2
$ update_portrait('oc001_01 17', 'p1', [mid(-2), light], 5)
c13 '[textdict[1210450]]'
menu:
    extend ""
    "[textdict[1210451]]":
        call avg25144
    "[textdict[1210452]]":
        call avg25145
    "[textdict[1210453]]":
        call avg25143
return
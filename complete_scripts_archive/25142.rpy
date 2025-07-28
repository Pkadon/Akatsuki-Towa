label avg25142:

stop music
scene placeholderbackground
$ update_narrator('c0')
window show
with fade_in
play sfx2 "other_7092.ogg"
c0 '[convertstrid(1210444)]'
$ update_portrait('oc002_01 14', 'p2', [mid(-3), light], 6)
play sfxvoice "avg_vocal_ch08.ogg"
c23 '[convertstrid(1210445)]'
hide p2
$ update_portrait('oc001_01 8', 'p1', [mid(-2), light], 6)
c13 '[convertstrid(1210446)]'
hide p1
$ update_portrait('oc002_01 5', 'p2', [mid(-3), light], 6)
play sfxvoice "avg_vocal_ch07.ogg"
c23 '[convertstrid(1210447)]'
hide p2
$ update_portrait('oc001_01 4', 'p1', [mid(-2), light], 6)
play sfxvoice "avg_vocal_na10.ogg"
c13 '[convertstrid(1210448)]'
hide p1
$ update_portrait('oc002_01 14', 'p2', [mid(-3), light], 6)
play sfxvoice "avg_vocal_ch04.ogg"
c23 '[convertstrid(1210449)]'
hide p2
$ update_portrait('oc001_01 17', 'p1', [mid(-2), light], 6)
c13 '[convertstrid(1210450)]'
menu:
    extend ""
    "[textdict[1210451]]":
        call avg25144
    "[textdict[1210452]]":
        call avg25145
    "[textdict[1210453]]":
        call avg25143
return
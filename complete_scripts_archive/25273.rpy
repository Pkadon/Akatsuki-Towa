label avg25273:

stop music
scene placeholderbackground
$ update_portrait('oc001_01 19', 'p1', [mid(-2), light], 5)
$ update_narrator('c13')
window show
with fade_in
play sfx2 "other_7079.ogg"
c13 '[convertstrid(1211040)]'
hide p1
$ update_portrait('oc002_01 12', 'p2', [mid(-3), light], 5)
play sfx2 "other_7077.ogg"
play sfxvoice "avg_vocal_ch11.ogg"
c23 '[convertstrid(1211041)]'
hide p2
$ update_portrait('oc001_01 18', 'p1', [mid(-2), light], 5)
c13 '[convertstrid(1211042)]'
menu:
    extend ""
    "[textdict[1214998]]":
        call avg25274
    "[textdict[1214996]]":
        call avg25275
return
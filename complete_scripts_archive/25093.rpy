label avg25093:

stop music
scene placeholderbackground
$ update_portrait('oc002_01 21', 'p2', [mid(-3), light], 6)
$ update_narrator('c23')
window show
with fade_in
play sfx2 "other_7079.ogg"
c23 '[convertstrid(1210263)]'
hide p2
$ update_portrait('oc001_01 3', 'p1', [mid(-2), light], 6)
play sfxvoice "avg_vocal_na07.ogg"
c13 '[convertstrid(1210264)]'
hide p1
$ update_portrait('oc002_01 9', 'p2', [mid(-3), light], 6)
play sfx2 "fight_6024.ogg"
c23 '[convertstrid(1210265)]'
menu:
    extend ""
    "[textdict[1214998]]":
        call avg25094
    "[textdict[1215000]]":
        call avg25026
return
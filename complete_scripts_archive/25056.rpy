label avg25056:

stop music
scene placeholderbackground
$ update_portrait('oc001_01 18', 'p1', [mid(-2), light], 6)
$ update_narrator('c13')
window show
with fade_in
play sfxvoice "avg_vocal_na15.ogg"
c13 '[convertstrid(1210163)]'
hide p1
$ update_portrait('oc002_01 2', 'p2', [mid(-3), light], 6)
play sfxvoice "avg_vocal_ch12.ogg"
c23 '[convertstrid(1210164)]'
hide p2
$ update_portrait('oc001_01 4', 'p1', [mid(-2), light], 6)
c13 '[convertstrid(1210165)]'
menu:
    extend ""
    "[textdict[1214997]]":
        call avg25057
    "[textdict[1215000]]":
        call avg25026
return
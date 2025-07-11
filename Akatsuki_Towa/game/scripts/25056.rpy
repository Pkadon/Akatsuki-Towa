label avg25056:

scene placeholderbackground
$ update_portrait('oc001_01 18', 'p1', [mid(-2), light], 5)
window show
with fade_in
play sfxvoice "avg_vocal_na15.ogg"
c13 '[textdict[1210163]]'
hide p1
$ update_portrait('oc002_01 2', 'p2', [mid(-3), light], 5)
play sfxvoice "avg_vocal_ch12.ogg"
c23 '[textdict[1210164]]'
hide p2
$ update_portrait('oc001_01 4', 'p1', [mid(-2), light], 5)
c13 '[textdict[1210165]]'
menu:
    extend ""
    "[textdict[1214997]]":
        call avg25057
    "[textdict[1215000]]":
        call avg25026
return
label avg25069:

scene placeholderbackground
$ update_portrait('oc002_01 2', 'p2', [mid(-3), light], 5)
window show
with fade_in
play sfxvoice "avg_vocal_ch12.ogg"
c23 '[textdict[1210220]]'
hide p2
$ update_portrait('oc001_01 4', 'p1', [mid(-2), light], 5)
c13 '[textdict[1210221]]'
menu:
    extend ""
    "[textdict[1214997]]":
        call avg25070
    "[textdict[1215000]]":
        call avg25026
return
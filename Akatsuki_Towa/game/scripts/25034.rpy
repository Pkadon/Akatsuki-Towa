label avg25034:

scene placeholderbackground
$ update_portrait('oc001_01 2', 'p1', [mid(-2), light], 5)
window show
with fade_in
c13 '[textdict[1210087]]'
hide p1
$ update_portrait('oc002_01 2', 'p2', [mid(-3), light], 5)
play sfxvoice "avg_vocal_ch12.ogg"
c23 '[textdict[1210088]]'
hide p2
$ update_portrait('oc001_01 4', 'p1', [mid(-2), light], 5)
c13 '[textdict[1210089]]'
hide p1
$ update_portrait('oc002_01 12', 'p2', [mid(-3), light], 5)
c23 '[textdict[1210090]]'
hide p2
$ update_portrait('oc001_01 18', 'p1', [mid(-2), light], 5)
c13 '[textdict[1210091]]'
menu:
    extend ""
    "[textdict[1214997]]":
        call avg25035
    "[textdict[1215000]]":
        call avg25026
return
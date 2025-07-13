label avg25061:

stop music
scene placeholderbackground
$ update_portrait('uc001_01 2', 'p2004', [mid(-2), light], 5)
$ update_narrator('c20043')
window show
with fade_in
c20043 '[textdict[1210177]]'
hide p2004
$ update_portrait('uc001_02 1', 'p2005', [mid(6), light], 5)
c20053 '[textdict[1210178]]'
hide p2005
$ update_portrait('oc002_01 2', 'p2', [mid(-3), light], 5)
play sfx2 "other_7004.ogg"
play sfxvoice "avg_vocal_ch12.ogg"
c23 '[textdict[1210179]]'
$ update_portrait('oc002_01 5', 'p2', [mid(-3), light], 5)
play sfxvoice "avg_vocal_ch07.ogg"
c23 '[textdict[1210180]]'
menu:
    extend ""
    "[textdict[1214997]]":
        call avg25062
    "[textdict[1215000]]":
        call avg25026
return
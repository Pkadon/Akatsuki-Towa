label avg25102:

stop music
scene placeholderbackground
$ update_portrait('oc002_01 2', 'p2', [mid(-3), light], 5)
$ update_narrator('c23')
window show
with fade_in
play sfxvoice "avg_vocal_ch12.ogg"
c23 '[textdict[1210286]]'
hide p2
play sfx2 "other_7051.ogg"
c20073 '[textdict[1210287]]'
$ update_portrait('oc001_01 2', 'p1', [mid(-2), light], 5)
c13 '[textdict[1210288]]'
hide p1
c20073 '[textdict[1210289]]'
menu:
    extend ""
    "[textdict[1214995]]":
        call avg25103
    "[textdict[1215000]]":
        call avg25000
return
label avg25017:

stop music
scene placeholderbackground
$ update_portrait('oc002_01 9', 'p2', [mid(-3), light], 5)
window show
with fade_in
c23 '[textdict[1210036]]'
hide p2
$ update_portrait('oc001_01 9', 'p1', [mid(-2), light], 5)
play sfx2 "other_7079.ogg"
c13 '[textdict[1210037]]'
hide p1
$ update_portrait('oc002_01 4', 'p2', [mid(-3), light], 5)
c23 '[textdict[1210038]]'
menu:
    extend ""
    "[textdict[1214998]]":
        call avg25027
    "[textdict[1215000]]":
        call avg25026
return
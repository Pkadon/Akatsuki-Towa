label avg12121:

play music "ED6104.ogg"
scene avg_bg_038
$ update_portrait('oc001_01 2', 'p1', [r(-2), light], 5)
$ update_narrator('c13')
window show
with fade_in
play sfx2 "other_7044.ogg"
c13 '[textdict[1128217]]'
$ update_portrait('oc001_01 2', 'p1', [r(-2), dark], 5)
c9581 '[textdict[1128218]]'
c9591 '[textdict[1128219]]'
$ update_portrait('oc001_01 1', 'p1', [r(-2), light], 5)
c13 '[textdict[1128220]]'
$ update_portrait('oc001_01 1', 'p1', [r(-2), dark], 5)
c9591 '[textdict[1128221]]'
c9591 '[textdict[1128222]]'
hide p1
$ update_portrait('oc002_01 18', 'p2', [r(-3), light], 5)
c23 '[textdict[1128223]]'
$ update_portrait('oc002_01 18', 'p2', [r(-3), dark], 5)
c9591 '[textdict[1128224]]'
$ update_portrait('oc002_01 2', 'p2', [r(-3), light], 5)
c23 '[textdict[1128225]]'
$ update_portrait('oc002_01 2', 'p2', [r(-3), dark], 5)
c9591 '[textdict[1128226]]'
c9591 '[textdict[1128227]]'
c9591 '[textdict[1128228]]'
c9591 '[textdict[1128229]]'
c9591 '[textdict[1128230]]'
menu:
    extend ""
    "[textdict[1100001]]":
        call avg12123
    "[textdict[1100002]]":
        call avg12122
return
label avg12366:

play music "ed7124.ogg"
scene avg_bg_059
$ update_portrait('oc002_01 14', 'p2', [r(-3), light], 5)
window show
with fade_in
play sfx2 "other_7021.ogg"
c23 '[textdict[1133805]]'
$ update_portrait('oc002_01 14', 'p2', [r(-3), dark], 5)
c10961 '[textdict[1133806]]'
$ update_portrait('oc002_01 12', 'p2', [r(-3), r_shake, light], 5)
c23 '[textdict[1133807]]'
$ update_portrait('oc002_01 12', 'p2', [r(-3), dark], 5)
c10961 '[textdict[1133808]]'
$ update_portrait('oc002_01 10', 'p2', [r(-3), light], 5)
c23 '[textdict[1133809]]'
hide p2
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 5)
c13 '[textdict[1133810]]'
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
c10961 '[textdict[1133811]]'
c10961 '[textdict[1133812]]'
$ update_portrait('oc001_01 1', 'p1', [r(-2), light], 5)
c13 '[textdict[1133813]]'
$ update_portrait('oc001_01 1', 'p1', [r(-2), dark], 5)
c10961 '[textdict[1133814]]'
c10961 '[textdict[1133815]]'
hide p1
$ update_portrait('oc002_01 2', 'p2', [r(-3), light], 5)
c23 '[textdict[1133816]]'
$ update_portrait('oc002_01 2', 'p2', [r(-3), dark], 5)
c10961 '[textdict[1133817]]'
c10961 '[textdict[1133818]]'
$ update_portrait('oc002_01 5', 'p2', [r(-3), light], 5)
play sfx2 "common_quest.ogg"
c23 '[textdict[1133819]]'
return
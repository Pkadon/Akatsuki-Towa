label avg20070:

play music "ed7150.ogg"
scene avg_bg_018
window show
with fade_in
$ update_portrait('oc001_01 2', 'p1', [r_entrance(-2), light], 5)
play sfx2 "other_7064.ogg"
c13 '[textdict[1003886]]'
hide p1
c6483 '[textdict[1003887]]'
c6491 '[textdict[1003888]]'
c6503 '[textdict[1003889]]'
$ update_portrait('oc001_01 7', 'p1', [r(-2), light], 5)
play sfxvoice "avg_vocal_na02.ogg"
c13 '[textdict[1003890]]'
$ update_portrait('oc001_01 7', 'p1', [r(-2), dark], 5)
$ update_portrait('oc004_01 8', 'p4', [l(-5), light, flip], 6)
play sfxvoice "avg_vocal_li17.ogg"
c41 '[textdict[1003891]]'
hide p4
hide p1
with fade
play sfx2 "other_7021.ogg"
c0 '[textdict[1003892]]'
play sfx2 "other_7004.ogg"
c6491 '[textdict[1003893]]'
$ update_portrait('oc001_01 1', 'p1', [r(-2), light], 5)
c13 '[textdict[1003894]]'
$ update_portrait('oc001_01 1', 'p1', [r(-2), dark], 5)
c6491 '[textdict[1003895]]'
c6491 '[textdict[1003896]]'
c6491 '[textdict[1003897]]'
hide p1
$ update_portrait('oc002_01 17', 'p2', [r(-3), light], 5)
c23 '[textdict[1003898]]'
$ update_portrait('oc002_01 17', 'p2', [r(-3), dark], 5)
play sfx2 "other_7021.ogg"
c6511 '[textdict[1003899]]'
c6511 '[textdict[1003900]]'
c6511 '[textdict[1003901]]'
c6491 '[textdict[1003902]]'
hide p2
$ update_portrait('oc001_01 10', 'p1', [r(-2), light], 5)
c13 '[textdict[1003903]]'
$ update_portrait('oc001_01 1', 'p1', [r(-2), light], 5)
c13 '[textdict[1003904]]'
return
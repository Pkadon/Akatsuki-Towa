label avg1117:

play music "ed7200.ogg"
scene placeholderbackground
$ update_portrait('oc004_01 13', 'p4', [l(-5), light, flip], 6)
$ update_narrator('c41')
window show
with fade_in
c41 '[textdict[2102897]]'
$ update_portrait('oc004_01 13', 'p4', [l(-5), dark, flip], 6)
$ update_portrait('oc001_01 10', 'p1', [r(-2), light], 5)
c13 '[textdict[2102898]]'
hide p4
hide p1
play sfx2 "other_7004.ogg"
c0 '[textdict[2102899]]'
play sfx2 "other_7004.ogg"
c0 '[textdict[2102900]]'
$ update_portrait('oc001_01 22', 'p1', [r(-2), light], 5)
c13 '[textdict[2102901]]'
$ update_portrait('oc001_01 22', 'p1', [r(-2), dark], 5)
$ update_portrait('oc004_01 1', 'p4', [l(-5), light, flip], 6)
c41 '[textdict[2102902]]'
$ update_portrait('oc004_01 1', 'p4', [l(-5), dark, flip], 6)
$ update_portrait('oc001_01 5', 'p1', [r(-2), light], 5)
c13 '[textdict[2102903]]'
hide p4
$ update_portrait('oc001_01 5', 'p1', [r(-2), dark], 5)
$ update_portrait('st004_01 6', 'p204', [l(4), light, flip], 6)
c2041 '[textdict[2102904]]'
hide p1
$ update_portrait('st004_01 6', 'p204', [l(4), dark, flip], 6)
$ update_portrait('sca15_01 5', 'p23', [r(9), light], 5)
c233 '[textdict[2102905]]'
$ update_portrait('sca15_01 1', 'p23', [r(9), light], 5)
c233 '[textdict[2102906]]'
return
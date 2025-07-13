label avg1116:

play music "ed7200.ogg"
scene placeholderbackground
$ update_portrait('oc004_01 13', 'p4', [l(-5), light, flip], 6)
$ update_narrator('c41')
window show
with fade_in
c41 '[textdict[2102890]]'
$ update_portrait('oc004_01 13', 'p4', [l(-5), dark, flip], 6)
$ update_portrait('oc001_01 1', 'p1', [r(-2), light], 5)
c13 '[textdict[2102891]]'
$ update_portrait('oc001_01 22', 'p1', [r(-2), light], 5)
c13 '[textdict[2102892]]'
hide p4
$ update_portrait('oc001_01 22', 'p1', [r(-2), dark], 5)
$ update_portrait('st004_01 6', 'p204', [l(4), light, flip], 6)
c2041 '[textdict[2102893]]'
hide p1
$ update_portrait('st004_01 6', 'p204', [l(4), dark, flip], 6)
c9773 '[textdict[2102894]]'
hide p204
$ update_portrait('oc004_01 21', 'p4', [l(-5), light, flip], 6)
c41 '[textdict[2102895]]'
return
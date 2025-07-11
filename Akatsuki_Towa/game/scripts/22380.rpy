label avg22380:

play music "ed7304.ogg"
scene placeholderbackground
window show
with fade_in
play sfx2 "other_7079.ogg"
c0 '[textdict[1133976]]'
$ update_portrait('oc001_01 3', 'p1', [mid(-2), light], 5)
c13 '[textdict[1133977]]'
hide p1
$ update_portrait('oc004_01 2', 'p4', [mid(-5), light], 5)
c43 '[textdict[1133978]]'
hide p4
$ update_portrait('oc003_01 2', 'p3', [mid(-6), light], 5)
c33 '[textdict[1133979]]'
hide p3
$ update_portrait('oc002_01 4', 'p2', [mid(-3), light], 5)
play sfx2 "fight_6024.ogg"
c23 '[textdict[1133980]]'
hide p2
$ update_portrait('oc001_01 20', 'p1', [mid(-2), light], 5)
c13 '[textdict[1133981]]'
hide p1
$ update_portrait('oc002_01 9', 'p2', [mid(-3), light], 5)
c23 '[textdict[1133982]]'
return
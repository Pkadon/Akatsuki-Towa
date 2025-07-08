label avg20059:
stop music

play music "ed7151.ogg"
scene placeholderbackground
$ update_portrait('oc001_01 4', 'p1', [mid(-2), light], 5)
window show
with fade_in
c13 '[textdict[1002986]]'
hide p1
$ update_portrait('oc002_01 5', 'p2', [mid(-3), light], 5)
c23 '[textdict[1002987]]'
hide p2
$ update_portrait('oc003_01 4', 'p3', [mid(-6), light], 5)
c33 '[textdict[1002988]]'
hide p3
play sfx2 "other_7071.ogg"
c4973 '[textdict[1002989]]'
c4973 '[textdict[1002990]]'
$ update_portrait('oc001_01 9', 'p1', [mid(-2), light], 5)
play sfxvoice "avg_vocal_na08.ogg"
c13 '[textdict[1002991]]'
hide p1
c4973 '[textdict[1002992]]'
c4973 '[textdict[1002993]]'
$ update_portrait('oc002_01 3', 'p2', [mid(-3), light], 5)
play sfx2 "other_7073.ogg"
c23 '[textdict[1002994]]'
hide p2
$ update_portrait('oc001_01 4', 'p1', [mid(-2), light], 5)
c13 '[textdict[1002995]]'
return
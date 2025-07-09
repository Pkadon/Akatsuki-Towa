label avg10736:
stop music

play music "ed7511.ogg"
scene avg_bg_038
$ update_portrait('oc003_01 9', 'p3', [l(-6), light, flip], 6)
window show
with fade_in
c31 '[textdict[1172583]]'
$ update_portrait('oc003_01 9', 'p3', [l(-6), dark, flip], 6)
$ update_portrait('oc001_01 20', 'p1', [r(-2), light], 5)
c13 '[textdict[1172584]]'
hide p3
hide p1
c0 '[textdict[1172585]]'
$ update_portrait('oc001_01 19', 'p1', [r(-2), light], 5)
c13 '[textdict[1172586]]'
hide p1
c0 '[textdict[1172587]]'
$ update_portrait('oc001_01 19', 'p1', [r(-2), light], 5)
c13 '[textdict[1172588]]'
$ update_portrait('oc001_01 19', 'p1', [r(-2), dark], 5)
$ update_portrait('oc003_01 21', 'p3', [l(-6), light, flip], 6)
c31 '[textdict[1172589]]'
hide p3
hide p1
c0 '[textdict[1172590]]'
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 5)
c13 '[textdict[1172591]]'
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
$ update_portrait('oc003_01 9', 'p3', [l(-6), light, flip], 6)
c31 '[textdict[1172592]]'
$ update_portrait('oc003_01 9', 'p3', [l(-6), dark, flip], 6)
$ update_portrait('oc001_01 20', 'p1', [r(-2), light], 5)
c13 '[textdict[1172593]]'
hide p3
hide p1
play sfx2 "other_7085.ogg"
c0 '[textdict[1172594]]'
return
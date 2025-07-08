label avg26033:
stop music

scene placeholderbackground
$ update_portrait('oc001_01 7', 'p1', [mid(-2), light], 5)
window show
with fade_in
c13 '[textdict[1215719]]'
hide p1
$ update_portrait('oc002_01 5', 'p2', [mid(-3), light], 5)
c23 '[textdict[1215720]]'
hide p2
$ update_portrait('oc001_01 8', 'p1', [mid(-2), light], 5)
c13 '[textdict[1215721]]'
hide p1
$ update_portrait('oc002_01 6', 'p2', [mid(-3), light], 5)
c23 '[textdict[1215722]]'
hide p2
play sfx2 "other_7002.ogg"
c0 '[textdict[1215753]]'
c0 '[textdict[1215723]]'
c0 '[textdict[1215724]]'
c0 '[textdict[1215725]]'
return
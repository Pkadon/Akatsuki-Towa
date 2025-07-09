label avg24520:
stop music

scene placeholderbackground
$ update_portrait('oc002_01 10', 'p2', [r(-3), light], 5)
window show
with fade_in
c23 '[textdict[1206042]]'
$ update_portrait('oc002_01 10', 'p2', [r(-3), dark], 5)
$ update_portrait('oc001_01 10', 'p1', [l(-2), light, flip], 6)
c11 '[textdict[1206043]]'
$ update_portrait('oc001_01 10', 'p1', [l(-2), dark, flip], 6)
$ update_portrait('oc002_01 5', 'p2', [r(-3), light], 5)
c23 '[textdict[1206044]]'
return
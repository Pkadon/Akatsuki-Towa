label avg24037:
stop music

scene placeholderbackground
$ update_portrait('oc001_01 1', 'p1', [mid(-2), light], 5)
window show
with fade_in
c13 '[textdict[1200148]]'
hide p1
$ update_portrait('oc002_01 2', 'p2', [mid(-3), light], 5)
c23 '[textdict[1200149]]'
hide p2
$ update_portrait('oc001_01 11', 'p1', [mid(-2), light], 5)
c13 '[textdict[1200150]]'
return
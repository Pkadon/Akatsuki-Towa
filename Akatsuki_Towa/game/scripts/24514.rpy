label avg24514:
stop music

scene placeholderbackground
$ update_portrait('oc001_01 2', 'p1', [mid(-2), light], 5)
window show
with fade_in
c13 '[textdict[1206036]]'
hide p1
$ update_portrait('oc002_01 10', 'p2', [mid(-3), light], 5)
c23 '[textdict[1206037]]'
hide p2
$ update_portrait('oc001_01 10', 'p1', [mid(-2), light], 5)
c13 '[textdict[1206038]]'
return
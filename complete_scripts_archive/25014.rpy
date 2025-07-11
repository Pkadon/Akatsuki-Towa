label avg25014:

stop music
scene placeholderbackground
$ update_portrait('oc002_01 2', 'p2', [mid(-3), light], 5)
window show
with fade_in
c23 '[textdict[1210026]]'
hide p2
$ update_portrait('oc001_01 2', 'p1', [mid(-2), light], 5)
play sfx2 "common_tag_2.ogg"
c13 '[textdict[1210027]]'
hide p1
$ update_portrait('oc002_01 1', 'p2', [mid(-3), light], 5)
c23 '[textdict[1210028]]'
hide p2
$ update_portrait('oc001_01 1', 'p1', [mid(-2), light], 5)
c13 '[textdict[1210029]]'
return
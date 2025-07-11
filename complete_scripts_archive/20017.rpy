label avg20017:

play music "ED6101.ogg"
scene placeholderbackground
$ update_portrait('oc001_01 11', 'p1', [mid(-2), light], 5)
window show
with fade_in
play sfx2 "other_7017.ogg"
c13 '[textdict[1001028]]'
$ update_portrait('oc001_01 1', 'p1', [mid(-2), light], 5)
play sfx2 "other_7064.ogg"
c13 '[textdict[1001029]]'
$ update_portrait('oc001_01 10', 'p1', [mid(-2), light], 5)
c13 '[textdict[1001030]]'
hide p1
$ update_portrait('oc002_01 1', 'p2', [mid(-3), light], 5)
c23 '[textdict[1001031]]'
return
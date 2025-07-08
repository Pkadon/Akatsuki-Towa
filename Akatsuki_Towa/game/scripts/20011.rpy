label avg20011:
stop music

play music "ed7150.ogg"
scene placeholderbackground
window show
with fade_in
c0 '[textdict[1000499]]'
c0 '[textdict[1000500]]'
$ update_portrait('oc001_01 2', 'p1', [mid(-2), light], 5)
c13 '[textdict[1000501]]'
hide p1
$ update_portrait('oc001_01 1', 'p1', [mid(-2), light], 5)
c13 '[textdict[1000502]]'
return
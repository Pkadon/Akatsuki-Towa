label avg20009:

play music "ed7150.ogg"
scene placeholderbackground
$ update_portrait('oc002_01 2', 'p2', [mid(-3), light], 5)
$ update_narrator('c23')
window show
with fade_in
c23 '[textdict[1000491]]'
hide p2
$ update_portrait('oc001_01 2', 'p1', [mid(-2), light], 5)
play sfx2 "other_7004.ogg"
c13 '[textdict[1000492]]'
return
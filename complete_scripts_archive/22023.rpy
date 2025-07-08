label avg22023:
stop music

play music "ed7105.ogg"
scene placeholderbackground
$ update_portrait('oc001_01 18', 'p1', [mid(-2), light], 5)
window show
with fade_in
play sfx2 "common_cancel.ogg"
c13 '[textdict[1120012]]'
hide p1
$ update_portrait('sc049_01 1', 'p56', [mid(-8), light], 5)
c563 '[textdict[1120013]]'
return
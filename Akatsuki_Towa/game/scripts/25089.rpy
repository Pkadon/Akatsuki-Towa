label avg25089:
stop music

scene placeholderbackground
$ update_portrait('oc001_01 6', 'p1', [mid(-2), light], 5)
window show
with fade_in
c13 '[textdict[1210254]]'
hide p1
$ update_portrait('uc001_01 1', 'p587', [mid(-2), light], 5)
play sfx2 "common_35rewardholy.ogg"
c5873 '[textdict[1210255]]'
return
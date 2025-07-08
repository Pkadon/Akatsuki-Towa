label avg29025:
stop music

play music "ED6104.ogg"
scene avg_bg_027
$ update_portrait('oc001_01 18', 'p1', [mid(-2), light], 5)
window show
with fade_in
play sfx2 "common_cancel.ogg"
c13 '[textdict[1120012]]'
return
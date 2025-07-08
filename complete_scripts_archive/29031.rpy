label avg29031:
stop music

play music "ED6104.ogg"
scene avg_bg_027
$ update_portrait('oc001_01 20', 'p1', [mid(-2), light], 5)
window show
with fade_in
play sfx2 "common_select.ogg"
play sfxvoice "avg_vocal_na23.ogg"
c13 '[textdict[1214992]]'
return
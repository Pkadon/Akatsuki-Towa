label avg12231:
stop music

play music "ed7105.ogg"
scene avg_bg_023
window show
with fade_in
play sfx2 "common_select.ogg"
c6891 '[textdict[1121115]]'
$ update_portrait('oc001_01 5', 'p1', [r(-2), light], 5)
play sfxvoice "bcv_oc001_com_01.ogg"
c13 '[textdict[1121116]]'
return
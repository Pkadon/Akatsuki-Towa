label avg12231:

play music "ed7105.ogg"
scene avg_bg_023
$ update_narrator('c6891')
window show
with fade_in
play sfx2 "common_select.ogg"
c6891 '[convertstrid(1121115)]'
$ update_portrait('oc001_01 5', 'p1', [r(-2), light], 6)
play sfxvoice "bcv_oc001_com_01.ogg"
c13 '[convertstrid(1121116)]'
return
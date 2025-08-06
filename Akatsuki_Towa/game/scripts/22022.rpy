label avg22022:

play music "ed7105.ogg"
scene avg_bg_023
$ update_portrait('sc049_01 6', 'p56', [l(-8), light, flip], 6)
$ update_narrator('c561')
window show
with fade_in
play sfx2 "common_select.ogg"
c561 '[convertstrid(1120010)]'
$ update_portrait('sc049_01 6', 'p56', [l(-8), dark, flip], 5)
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
play sfx2 "fight_6024.ogg"
play sfxvoice "bcv_oc001_com_01.ogg"
c13 '[convertstrid(1120011)]'
return
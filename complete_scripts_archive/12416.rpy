label avg12416:

play music "ed6564.ogg"
scene avg_bg_004
$ update_portrait('oc004_01 1', 'p4', [l(-5), light, flip], 6)
$ update_narrator('c41')
window show
with fade_in
play sfxvoice "avg_vocal_li03.ogg"
c41 '[convertstrid(1142756)]'
return
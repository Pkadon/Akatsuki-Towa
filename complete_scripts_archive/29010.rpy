label avg29010:

$ play_music("ed7300.ogg")
scene avg_bg_071
$ update_narrator('c21')
$ update_portrait('oc002_01 5', 'p2', [l(-3), light, flip], 6)
window show
with fade_in
$ update_portrait('oc002_01 5', 'p2', [l(-3), l_shake, light, flip], 6)
play sfxvoice "avg_vocal_ch07.ogg"
c21 '[convertstrid(1007041)]'
$ update_portrait('oc002_01 5', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc001_01 6', 'p1', [r(-2), light], 6)
play sfxvoice "avg_vocal_na16.ogg"
c13 '[convertstrid(1007042)]'
return
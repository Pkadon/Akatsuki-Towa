label avg10677:

$ play_music("ed7564.ogg")
scene avg_bg_050
$ update_narrator('c0')
window show
with fade_in
c0 '[convertstrid(1166333)]'
c0 '[convertstrid(1166334)]'
c0 '[convertstrid(1166335)]'
c0 '[convertstrid(1166336)]'
scene avg_bg_070
$ update_portrait('oc008_01 1', 'p8', [l(-5), light, flip], 6)
$ update_narrator('c81')
with fade
c81 '[convertstrid(1166337)]'
$ update_portrait('oc008_01 1', 'p8', [l(-5), light, flip], 6)
c81 '[convertstrid(1166338)]'
$ update_portrait('oc008_01 1', 'p8', [l(-5), light, flip], 6)
c81 '[convertstrid(1166339)]'
$ update_portrait('oc008_01 5', 'p8', [l(-5), light, flip], 6)
play sfxvoice "avg_vocal_ai02b.ogg"
c81 '[convertstrid(1166340)]'
$ update_portrait('oc008_01 6', 'p8', [l(-5), light, flip], 6)
c81 '[convertstrid(1166341)]'
hide p8
play sfxvoice "avg_vocal_ai07.ogg"
c0 '[convertstrid(1166342)]'
return
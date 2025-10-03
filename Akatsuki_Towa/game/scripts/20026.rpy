label avg20026:

$ play_music("ed7150.ogg")
scene avg_bg_022
$ update_narrator('c5413')
window show
with fade_in
c5413 '[convertstrid(1001662)]'
c5413 '[convertstrid(1001663)]'
c5413 '[convertstrid(1001664)]'
c5421 '[convertstrid(1001665)]'
$ update_portrait('oc002_01 2', 'p2', [r(-3), light], 6)
play sfxvoice "avg_vocal_ch12.ogg"
c23 '[convertstrid(1001666)]'
$ update_portrait('oc002_01 2', 'p2', [r(-3), dark], 5)
$ update_portrait('oc001_01 10', 'p1', [l(-2), light, flip], 6)
play sfxvoice "avg_vocal_na20.ogg"
c11 '[convertstrid(1001667)]'
return
label avg20129:

$ play_music("ed7103.ogg")
scene avg_bg_019
$ update_portrait('oc001_01 10', 'p1', [r(-2), light], 6)
$ update_narrator('c13')
window show
with fade_in
play sfxvoice "avg_vocal_na20.ogg"
c13 '[convertstrid(1100004)]'
$ update_portrait('oc001_01 10', 'p1', [r(-2), dark], 5)
$ update_portrait('sc044_01 1', 'p51', [l(-7), light, flip], 6)
c511 '[convertstrid(1006632)]'
return
label avg12418:

$ play_music("ed6564.ogg")
scene avg_bg_004
$ update_portrait('oc003_01 2', 'p3', [l(-6), light, flip], 6)
$ update_narrator('c31')
window show
with fade_in
play sfxvoice "avg_vocal_ro10.ogg"
c31 '[convertstrid(1142760)]'
return
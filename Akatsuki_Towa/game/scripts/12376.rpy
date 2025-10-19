label avg12376:

$ play_music("ed9999.ogg")
scene avg_bg_058
$ update_portrait('oc002_01 4', 'p2', [l(-3), light, flip], 6)
$ update_narrator('c21')
window show
with fade_in
play sfx2 "common_cancel.ogg"
c21 '[convertstrid(1134077)]'
return
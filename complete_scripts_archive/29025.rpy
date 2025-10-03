label avg29025:

$ play_music("ED6104.ogg")
scene avg_bg_027
$ update_portrait('oc001_01 18', 'p1', [mid(-2), light], 6)
$ update_narrator('c13')
window show
with fade_in
play sfx2 "common_cancel.ogg"
c13 '[convertstrid(1120012)]'
return
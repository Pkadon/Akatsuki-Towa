label avg29040:

play music "ED6104.ogg"
scene avg_bg_027
$ update_portrait('oc001_01 1', 'p1', [mid(-2), light], 6)
$ update_narrator('c13')
window show
with fade_in
play sfxvoice "bcv_oc001_win_02.ogg"
c13 '[convertstrid(1100021)]'
return
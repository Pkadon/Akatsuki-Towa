label avg12103:

play music "ed7111.ogg"
scene avg_bg_047
$ update_portrait('oc005_01 1', 'p5', [r(-6), light], 6)
$ update_narrator('c53')
window show
with fade_in
play sfx2 "common_cancel.ogg"
play sfxvoice "avg_vocal_ji02.ogg"
c53 '[convertstrid(1128018)]'
return
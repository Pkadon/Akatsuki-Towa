label avg12417:

play music "ed6564.ogg"
scene avg_bg_004
$ update_portrait('oc002_01 5', 'p2', [l(-3), light, flip], 6)
$ update_narrator('c21')
window show
with fade_in
play sfxvoice "avg_vocal_ch07.ogg"
c21 '[textdict[1142758]]'
return
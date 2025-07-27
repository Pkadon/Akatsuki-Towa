label avg20030:

play music "ed7150.ogg"
scene placeholderbackground
$ update_portrait('oc004_01 1', 'p4', [mid(-5), light], 5)
$ update_narrator('c43')
window show
with fade_in
play sfxvoice "avg_vocal_li06.ogg"
c43 '[convertstrid(1002138)]'
return
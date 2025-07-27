label avg20026:

play music "ed7150.ogg"
scene placeholderbackground
$ update_narrator('c5413')
window show
with fade_in
c5413 '[convertstrid(1001662)]'
c5413 '[convertstrid(1001663)]'
c5413 '[convertstrid(1001664)]'
c5423 '[convertstrid(1001665)]'
$ update_portrait('oc002_01 2', 'p2', [mid(-3), light], 5)
play sfxvoice "avg_vocal_ch12.ogg"
c23 '[convertstrid(1001666)]'
hide p2
$ update_portrait('oc001_01 10', 'p1', [mid(-2), light], 5)
play sfxvoice "avg_vocal_na20.ogg"
c13 '[convertstrid(1001667)]'
return
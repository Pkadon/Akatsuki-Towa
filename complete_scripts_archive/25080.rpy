label avg25080:

stop music
scene placeholderbackground
$ update_portrait('oc001_01 20', 'p1', [mid(-2), light], 6)
$ update_narrator('c13')
window show
with fade_in
play sfx2 "common_select.ogg"
play sfxvoice "avg_vocal_na24.ogg"
c13 '[convertstrid(1210098)]'
return
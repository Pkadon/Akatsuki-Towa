label avg22131:

stop music
scene placeholderbackground
$ update_portrait('oc002_01 3', 'p2', [mid(-3), light], 5)
$ update_narrator('c23')
window show
with fade_in
c23 '[convertstrid(1128267)]'
hide p2
$ update_portrait('oc001_01 8', 'p1', [mid(-2), light], 5)
c13 '[convertstrid(1128268)]'
hide p1
$ update_portrait('oc003_01 8', 'p3', [mid(-6), light], 5)
play sfxvoice "avg_vocal_ro13.ogg"
c33 '[convertstrid(1128269)]'
return
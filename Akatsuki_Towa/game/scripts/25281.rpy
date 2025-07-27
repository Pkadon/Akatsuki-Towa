label avg25281:

stop music
scene placeholderbackground
$ update_portrait('oc001_01 18', 'p1', [mid(-2), light], 5)
$ update_narrator('c13')
window show
with fade_in
play sfx2 "common_tag_2.ogg"
c13 '[convertstrid(1211064)]'
hide p1
$ update_portrait('oc002_01 10', 'p2', [mid(-3), light], 5)
play sfxvoice "avg_vocal_ch20.ogg"
c23 '[convertstrid(1211065)]'
hide p2
$ update_portrait('oc001_01 2', 'p1', [mid(-2), light], 5)
c13 '[convertstrid(1211066)]'
hide p1
$ update_portrait('oc002_01 21', 'p2', [mid(-3), light], 5)
c23 '[convertstrid(1211067)]'
return
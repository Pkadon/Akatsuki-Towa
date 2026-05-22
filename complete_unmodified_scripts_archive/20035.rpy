label avg20035:

$ play_music("ED6505.ogg")
scene avg_bg_027
$ update_narrator('c0')
window show
with fade_in
c0 '[convertstrid(1007702)]'
$ update_portrait('oc001_01 2', 'p1', [r(-2), light], 6)
c13 '[convertstrid(1002273)]'
hide p1
$ update_portrait('oc002_01 8', 'p2', [r(-3), light], 6)
c23 '[convertstrid(1002274)]'
$ update_portrait('oc002_01 8', 'p2', [r(-3), dark], 5)
c5531 '[convertstrid(1002275)]' with shake
$ update_portrait('oc002_01 12', 'p2', [r(-3), r_shake, light], 6)
play sfxvoice "avg_vocal_ch11.ogg"
c23 '[convertstrid(1002276)]'
hide p2
$ update_narrator('c2401')
with fade
$ update_portrait('st041_01 4', 'p240', [l_entrance(-1), light, flip], 6)
c2401 '[convertstrid(1002277)]'
$ update_portrait('st041_01 4', 'p240', [l(-1), dark, flip], 5)
$ update_portrait('st050_01 2', 'p257', [r(-11), light], 6)
c2573 '[convertstrid(1002278)]'
$ update_portrait('st050_01 5', 'p257', [r(-11), light], 6)
c2573 '[convertstrid(1002279)]'
$ update_portrait('st050_01 5', 'p257', [r(-11), dark], 5)
$ update_portrait('st041_01 2', 'p240', [l(-1), light, flip], 6)
c2401 '[convertstrid(1002280)]'
hide p257
$ update_portrait('st041_01 2', 'p240', [l(-1), dark, flip], 5)
$ update_portrait('oc002_01 2', 'p2', [r_entrance(-3), light], 6)
c23 '[convertstrid(1002281)]'
$ update_portrait('oc002_01 2', 'p2', [r(-3), dark], 5)
$ update_portrait('st041_01 4', 'p240', [l(-1), light, flip], 6)
c2401 '[convertstrid(1002282)]'
$ update_portrait('st041_01 1', 'p240', [l(-1), light, flip], 6)
c2401 '[convertstrid(1002283)]'
$ update_portrait('st041_01 1', 'p240', [l(-1), dark, flip], 5)
$ update_portrait('oc002_01 6', 'p2', [r(-3), light], 6)
c23 '[convertstrid(1002284)]'
$ update_portrait('oc002_01 6', 'p2', [r(-3), dark], 5)
$ update_portrait('st041_01 1', 'p240', [l(-1), light, flip], 6)
c2401 '[convertstrid(1002285)]'
$ update_portrait('st041_01 3', 'p240', [l(-1), light, flip], 6)
c2401 '[convertstrid(1002286)]'
hide p240
hide p2
$ update_portrait('oc001_01 8', 'p1', [r(-2), light], 6)
$ update_narrator('c13')
with fade
c13 '[convertstrid(1002287)]'
$ update_portrait('oc001_01 8', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 1', 'p2', [l(-3), light, flip], 6)
c21 '[convertstrid(1002288)]'
hide p1
$ update_portrait('oc002_01 1', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc003_01 5', 'p3', [r(-6), light], 6)
c33 '[convertstrid(1002289)]'
return